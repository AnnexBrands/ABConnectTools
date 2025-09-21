"""Utility functions for API operations.

Provides common functionality used across multiple endpoints.
"""

from typing import Union, Optional
from .endpoints.base import BaseEndpoint


def resolve_company_identifier(company: Union[str, None], endpoint: BaseEndpoint) -> Optional[str]:
    """Resolve a company code or ID to a company UUID.

    This is a DRY helper that handles the common pattern of accepting either
    a company code (e.g., 'LIVE') or UUID and resolving it to a UUID for API calls.

    Args:
        company: Company code (e.g., 'LIVE') or UUID. If None, returns None.
        endpoint: BaseEndpoint instance to use for cache lookups

    Returns:
        Company UUID string, or None if company is None

    Raises:
        ValueError: If company code not found in cache or invalid format

    Examples:
        # With UUID (passes through)
        uuid = resolve_company_identifier('cf8085ed-b2f2-e611-9f52-00155d426802', endpoint)

        # With code (resolves via cache)
        uuid = resolve_company_identifier('LIVE', endpoint)

        # With None (passes through)
        uuid = resolve_company_identifier(None, endpoint)  # Returns None
    """
    if company is None:
        return None

    # Determine if it's a UUID (contains dashes and is 36 chars) or code
    if is_uuid := '-' in company and len(company) == 36:
        return company

    company_id = endpoint.get_cache(company)
    if not company_id or company_id.strip() in ("", "null"):
        raise ValueError(f"Company with code '{company}' not found in cache")
    return company_id.strip()



def resolve_company_id_param(company: Union[str, None], endpoint: BaseEndpoint) -> dict:
    """Resolve company parameter and return as companyId parameter dict.

    Helper function that resolves a company identifier and returns it in the
    format expected by API endpoints that require a companyId parameter.

    Args:
        company: Company code or UUID. If None, returns empty dict.
        endpoint: BaseEndpoint instance to use for cache lookups

    Returns:
        Dictionary with companyId parameter, or empty dict if company is None

    Examples:
        # Returns {'companyId': 'cf8085ed-b2f2-e611-9f52-00155d426802'}
        params = resolve_company_id_param('LIVE', endpoint)

        # Returns {}
        params = resolve_company_id_param(None, endpoint)
    """
    company_id = resolve_company_identifier(company, endpoint)
    if company_id:
        return {"companyId": company_id}
    return {}