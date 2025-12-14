"""Utility functions for API operations.

Provides common functionality used across multiple endpoints.
"""

from typing import Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .endpoints.base import BaseEndpoint


def resolve_company_identifier(company: Union[str, None], endpoint: "BaseEndpoint") -> Optional[str]:
    """Resolve a company code or ID to a company UUID.

    Args:
        company: Company code (e.g., '16023SC') or UUID
        endpoint: Endpoint instance with access to cache

    Returns:
        Company UUID string

    Raises:
        ValueError: If company code not found in cache
    """
    if company is None:
        return None

    # If it looks like a UUID already, return as-is
    if len(company) == 36 and company.count('-') == 4:
        return company

    # Otherwise look up in cache
    company_id = endpoint.get_cache(company)
    if not company_id or company_id.strip() in ("", "null"):
        raise ValueError(f"Company with code '{company}' not found in cache")
    return company_id.strip()


def resolve_company_id_param(
    company: Union[str, None],
    endpoint: "BaseEndpoint"
) -> Optional[Dict[str, Any]]:
    """Resolve company identifier to a companyId query parameter dict.

    Args:
        company: Company code (e.g., '16023SC') or UUID, or None
        endpoint: Endpoint instance with access to cache

    Returns:
        Dict with companyId param, or None if no company provided
    """
    if company is None:
        return None

    company_uuid = resolve_company_identifier(company, endpoint)
    if company_uuid:
        return {"companyId": company_uuid}
    return None
