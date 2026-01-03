"""Examples of getting model classes from string names.

This demonstrates various approaches to resolve model class names (strings)
to actual Pydantic model classes for validation and type checking.
"""

from typing import Optional, Type
from ABConnect import models
from ABConnect.routes import SCHEMA


# =============================================================================
# APPROACH 1: Simple getattr (recommended for most cases)
# =============================================================================

def get_model(name: str) -> Type:
    """Get a model class by name.

    Args:
        name: Model class name (e.g., 'ContactDetails')

    Returns:
        The model class

    Raises:
        AttributeError: If model doesn't exist
    """
    return getattr(models, name)


# =============================================================================
# APPROACH 2: Safe lookup with None fallback
# =============================================================================

def get_model_or_none(name: str) -> Optional[Type]:
    """Get a model class by name, returning None if not found."""
    return getattr(models, name, None)


# =============================================================================
# APPROACH 3: Get model from SCHEMA route definition
# =============================================================================

def get_response_model_for_route(resource: str, method: str) -> Optional[Type]:
    """Get the response model class for a SCHEMA route.

    Args:
        resource: Resource name (e.g., 'CONTACTS', 'COMPANIES')
        method: HTTP method (e.g., 'GET', 'POST')

    Returns:
        Model class or None if not defined

    Example:
        >>> model = get_response_model_for_route('CONTACTS', 'GET')
        >>> model.__name__
        'ContactDetails'
    """
    route = SCHEMA.get(resource, {}).get(method)
    if not route or not route.response_model:
        return None
    return getattr(models, route.response_model, None)


# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == '__main__':
    # Example 1: Direct model access
    print("=== Direct Model Access ===")
    ContactDetails = get_model('ContactDetails')
    print(f"ContactDetails: {ContactDetails}")

    # Example 2: Safe lookup
    print("\n=== Safe Lookup ===")
    model = get_model_or_none('ContactDetails')
    print(f"Found: {model}")
    missing = get_model_or_none('NonExistentModel')
    print(f"Missing: {missing}")

    # Example 3: From SCHEMA
    print("\n=== From SCHEMA Route ===")
    contacts_model = get_response_model_for_route('CONTACTS', 'GET')
    print(f"CONTACTS GET response model: {contacts_model}")

    # Example 4: Validate data against model
    print("\n=== Model Validation ===")
    sample_data = {
        "id": 123,
        "fullName": "John Doe",
        "contactDisplayId": 456
    }
    contact = ContactDetails.model_validate(sample_data)
    print(f"Validated contact: {contact.full_name} (ID: {contact.contact_display_id})")