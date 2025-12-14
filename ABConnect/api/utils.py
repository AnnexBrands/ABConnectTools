"""Utility functions for API operations.

Provides common functionality used across multiple endpoints.
"""

from typing import Union, Optional
from .endpoints.base import BaseEndpoint


def resolve_company_identifier(company: Union[str, None], endpoint: BaseEndpoint) -> Optional[str]:
    """Resolve a company code or ID to a company UUID.
    """

    company_id = endpoint.get_cache(company)
    if not company_id or company_id.strip() in ("", "null"):
        raise ValueError(f"Company with code '{company}' not found in cache")
    return company_id.strip()
