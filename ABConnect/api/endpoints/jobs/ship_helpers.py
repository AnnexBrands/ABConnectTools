from __future__ import annotations

""" help create shipments and send labels
"""

import logging
import json
from typing import Dict, Iterable, List, Optional, Tuple, Any
from decimal import Decimal
from ABConnect.api.endpoints.base import BaseEndpoint

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _try_parse_json(s: str):
    try:
        return json.loads(s)
    except (json.JSONDecodeError, TypeError):
        return None


def _norm(code: str) -> str:
    return (code or "").upper()


def _is_usps(code: str) -> bool:
    return _norm(code).startswith("USPS")


def _extract_triples(
    rates: Iterable[Dict[str, Any]],
) -> List[Tuple[str, Optional[str], Decimal]]:
    """Extract (carrierCode, account, price) triples with normalized code and Decimal price, filtering malformed rows."""
    triples: List[Tuple[str, Optional[str], Decimal]] = []
    for r in rates or ():
        code = r.get("carrierCode")
        account = r.get("usedCarrierAccountCode")
        price = r.get("price")
        if not code or price is None:
            continue
        triples.append((_norm(code), account, Decimal(str(price))))
    return triples


def _first_non_usps(
    triples: List[Tuple[str, Optional[str], Decimal]],
) -> Optional[Tuple[str, Optional[str], Decimal]]:
    return next((t for t in triples if not _is_usps(t[0])), None)


class ShipHelper(BaseEndpoint):
    def __init__(self):
        super().__init__()
        # Avoid circular import issues
        from ABConnect.api.endpoints.jobs.freightproviders import (
            JobFreightProvidersEndpoint,
        )
        from ABConnect.api.endpoints.jobs.shipment import JobShipmentEndpoint

        self.freight = JobFreightProvidersEndpoint()
        self.shipment = JobShipmentEndpoint()

    def _get_if_parcel(self, job_display_id: str):
        """ """
        logger.info(f"Fetching freight providers for job ID: {job_display_id}")

        freight = self.freight.get_freightproviders(job_display_id, only_active="true")

        if len(freight) > 1:
            logger.error("Multiple providers active -- aborting")
            raise Exception("Only one provider may be active")

        data = freight[0]
        obtainNFMJobState = data.get("obtainNFMJobState")
        data["obtainNFMJobState"] = _try_parse_json(obtainNFMJobState)

        if all(
            [
                data.get("optionIndex") == 3,
                data.get("shipmentAccepted") is False,
            ]
        ):
            return data

    def _get_choices(
        self, job_display_id: str, ensure_provider: Optional[str] = None
    ) -> Tuple[str, Dict[str, List[Optional[str] | Decimal]]]:
        """
        Build a minimal choice set from rate quotes:
        - Return the first (lowest) rate.
        - If the first is USPS, also include the first non-USPS (enables UPS/FedEx switch).
        - If `ensure_provider` is given and not already included, include that carrier's rate too.
        Returns (ratesKey, dict) where dict maps carrierCode -> [account or None, price].
        """
        ensure = _norm(ensure_provider) if ensure_provider else None

        rq = self.shipment.get_shipment_ratequotes(job_display_id)
        rates = rq.get("rates") or []
        triples = _extract_triples(rates)

        if not triples:
            logger.warning(
                "No rate quotes for job %s; returning empty choice set.", job_display_id
            )
            return rq.get("ratesKey", ""), {}

        # Always include the first (lowest) rate.
        first_code, first_account, first_price = triples[0]
        choices: Dict[str, List[Optional[str] | Decimal]] = {
            first_code: [first_account, first_price]
        }

        # If caller specifically wants that provider and it's already first, we're done.
        if ensure and ensure == first_code:
            return rq["ratesKey"], choices

        # If first is USPS, include the first non-USPS (if any).
        if _is_usps(first_code):
            non_usps = _first_non_usps(triples)
            if non_usps:
                code2, account2, price2 = non_usps
                choices[code2] = [account2, price2]

        # If ensure_provider is requested but not present yet, add its rate if available.
        if ensure and ensure not in choices:
            ensured = next((t for t in triples if t[0] == ensure), None)
            if ensured:
                code3, account3, price3 = ensured
                choices[code3] = [account3, price3]

        return rq["ratesKey"], choices
