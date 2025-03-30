import logging
import urllib.parse
from typing import Optional
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.common import FormId, FormType, BolType, to_file_dict

logging.basicConfig(level=logging.INFO)


class FormsEndpoint(BaseEndpoint):
    def _get_bol_params(self, jobid: int, seq: BolType) -> dict:
        """
        0: house
        2: pickup
        5: LTL (special case - if last mile, the carrier bol)
        6: delivery
        56: Carrier - want 5 if exists, else 6
        """
        shipmentplans = self._r.call("GET", "api/job/%s/form/shipments" % jobid)
        candidates = (
            [5, 6] if seq == BolType.CARRIER else [seq.value]
        )  # results ordered so 5 precedes 6

        for plan in shipmentplans:
            if plan.get("sequenceNo") in candidates:
                return {"jobid": jobid, "shipmentPlanID": plan.get("jobShipmentID")}

    def get_bill_of_lading(self, jobid, boltype: BolType) -> dict:
        url_params = self._get_bol_params(jobid, boltype)
        bol_url = (
            "job/%(jobid)s/form/BillOfLading?ProviderOptionIndex=&shipmentPlanID=%(shipmentPlanID)s"
            % url_params
        )
        response = self._r.call("GET", bol_url, raw=True)

        return to_file_dict(
            response,
            jobid,
            boltype.name,
        )

    def get_bol(self, jobid) -> dict:
        return self.get_bill_of_lading(jobid, BolType.CARRIER)

    def get_hbl(self, jobid) -> dict:
        return self.get_bill_of_lading(jobid, BolType.HOUSE)

    def get_pbl(self, jobid) -> dict:
        return self.get_bill_of_lading(jobid, BolType.PICKUP)

    def get_dbl(self, jobid) -> dict:
        return self.get_bill_of_lading(jobid, BolType.DELIVERY)

    def get_form(
        self,
        jobid: int,
        formid: FormId,
        formtype: Optional[FormType] = None,
        spid: Optional[str] = None,
    ) -> dict:
        """base function to get forms"""
        base_url = "job/%s/form/%s" % (jobid, formid.value)
        get_params = {
            "type": formtype.value if formtype else None,
            "shipmentPlanID": spid,
        }
        query_string = urllib.parse.urlencode(
            {k: v for k, v in get_params.items() if v is not None}
        )
        url = f"{base_url}?{query_string}" if query_string else base_url

        response = self._r.call("GET", url, raw=True)
        return to_file_dict(
            response,
            jobid,
            formid.name,
        )
