# ABConnectTools Modernization: Schema-First API Implementation

## Context
<project_overview>
ABConnectTools is a Python package that currently uses dynamic endpoint generation from swagger.json to provide access to 223+ API endpoints. We need to modernize this into a professional, type-safe, well-documented package following schema-first principles.
</project_overview>

<current_architecture>
- Dynamic endpoint generation from `ABConnect/base/swagger.json`
- Existing modules: Builder, Quoter, Loader, API
- Some Pydantic models already in use
- Documentation at abconnecttools.readthedocs.io
</current_architecture>

<transformation_goal>
Convert from dynamic generation to explicit, typed, well-tested API implementation with:
- Pydantic models for ALL swagger schemas
- Endpoint modules organized by swagger tags
- Comprehensive test coverage
- Auto-generated documentation with examples
- Professional error handling and validation
</transformation_goal>

## Implementation Requirements

### 1. Project Structure Analysis
<analysis_tasks>
1. Parse `ABConnect/base/swagger.json` to extract:
   - All swagger tags (for module organization)
   - All schema definitions (for Pydantic models)
   - All endpoints and their request/response schemas
   - All error responses and status codes

2. Analyze current codebase structure:
   - Existing models and their usage patterns
   - Current endpoint implementation patterns
   - Test structure and coverage
   - Documentation organization
</analysis_tasks>

### 2. Schema Implementation
<schema_requirements>
For each swagger schema definition:

**File**: `models/{tag}/{schema_name}.py`
```python
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union
from datetime import datetime

class RegistrationModel(BaseModel):
    """User registration request model.
    
    Based on swagger schema: RegistrationModel
    Example usage in docs and tests.
    """
    email: str = Field(..., description="User email address")
    password: str = Field(..., min_length=8, description="User password")
    # ... all fields with proper types, validation, descriptions
    
    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "secure_password123"
            }
        }
    
    @validator('email')
    def validate_email(cls, v):
        # Custom validation logic
        return v
```

**Requirements**:
- All swagger properties mapped to Pydantic fields
- Proper type annotations (List, Optional, Union, etc.)
- Field descriptions from swagger documentation
- Validation rules from swagger constraints
- Example data in Config.schema_extra
- Custom validators for business logic
</schema_requirements>

### 3. Endpoint Implementation
<endpoint_requirements>
For each swagger tag, create: `endpoints/{tag}.py`

```python
from typing import Optional, List
from ..models.{tag} import {ModelName}
from ..core.client import APIClient
from ..core.exceptions import ABConnectError, ValidationError

class {TagName}Endpoints:
    """
    {Tag description from swagger}
    
    Handles all API operations related to {tag}.
    """
    
    def __init__(self, client: APIClient):
        self.client = client
    
    async def register_user(
        self, 
        registration_data: RegistrationModel
    ) -> UserResponseModel:
        """
        Register a new user account.
        
        Args:
            registration_data: User registration information
            
        Returns:
            UserResponseModel: Created user information
            
        Raises:
            ValidationError: Invalid registration data
            ABConnectError: API error response
            
        Example:
            >>> client = ABConnectClient()
            >>> registration = RegistrationModel(email="test@example.com", password="secure123")
            >>> user = await client.account.register_user(registration)
        """
        try:
            # Validate input using Pydantic
            registration_data.validate()
            
            # Make API call with proper error handling
            response = await self.client.post(
                "/api/account/register",
                json=registration_data.dict()
            )
            
            # Parse and validate response
            return UserResponseModel.parse_obj(response.json())
            
        except ValidationError as e:
            raise ValidationError(f"Invalid registration data: {e}")
        except APIException as e:
            raise ABConnectError(f"Registration failed: {e}")
```

**Requirements**:
- Type hints for all parameters and return values
- Comprehensive docstrings with examples
- Proper error handling and custom exceptions
- Input validation using Pydantic models
- Response parsing and validation
- Async/await pattern for all API calls
</endpoint_requirements>

### 4. Example Data Generation
<example_requirements>
For each model, create: `examples/{tag}.py`

```python
from ..models.{tag} import {ModelName}

# Realistic example data for documentation and testing
REGISTRATION_EXAMPLE = RegistrationModel(
    email="john.doe@company.com",
    password="SecurePassword123!",
    first_name="John",
    last_name="Doe",
    company="Acme Corp"
)

# Multiple examples for different scenarios
REGISTRATION_EXAMPLES = {
    "basic": REGISTRATION_EXAMPLE,
    "minimal": RegistrationModel(email="user@test.com", password="password123"),
    "complete": RegistrationModel(
        email="admin@enterprise.com",
        password="ComplexPassword456!",
        first_name="Admin",
        last_name="User",
        company="Enterprise Inc",
        phone="+1-555-0123"
    )
}
```

**Requirements**:
- Realistic, professional example data
- Multiple scenarios (minimal, typical, complete)
- Consistent naming conventions
- No placeholder strings like "string" or "example@example.com"
- Examples that would work in real API calls
</example_requirements>

### 5. Test Implementation
<testing_requirements>
For each endpoint module: `tests/endpoints/test_{tag}.py`

```python
import pytest
from unittest.mock import AsyncMock, patch
from ..examples.{tag} import REGISTRATION_EXAMPLES
from ..models.{tag} import RegistrationModel
from ..endpoints.{tag} import {TagName}Endpoints
from ..core.exceptions import ValidationError, ABConnectError

class Test{TagName}Endpoints:
    
    @pytest.fixture
    def mock_client(self):
        return AsyncMock()
    
    @pytest.fixture
    def {tag}_endpoints(self, mock_client):
        return {TagName}Endpoints(mock_client)
    
    @pytest.mark.asyncio
    async def test_register_user_success(self, {tag}_endpoints, mock_client):
        """Test successful user registration."""
        # Arrange
        registration_data = REGISTRATION_EXAMPLES["basic"]
        expected_response = {"id": 123, "email": registration_data.email}
        mock_client.post.return_value.json.return_value = expected_response
        
        # Act
        result = await {tag}_endpoints.register_user(registration_data)
        
        # Assert
        assert result.id == 123
        assert result.email == registration_data.email
        mock_client.post.assert_called_once_with(
            "/api/account/register",
            json=registration_data.dict()
        )
    
    @pytest.mark.asyncio
    async def test_register_user_validation_error(self, {tag}_endpoints):
        """Test registration with invalid data raises ValidationError."""
        # Arrange
        invalid_data = RegistrationModel(email="invalid-email", password="123")
        
        # Act & Assert
        with pytest.raises(ValidationError):
            await {tag}_endpoints.register_user(invalid_data)
    
    def test_registration_model_schema_validation(self):
        """Test that example data validates against schema."""
        for name, example in REGISTRATION_EXAMPLES.items():
            # Should not raise any exception
            RegistrationModel.validate(example.dict())
```

**Requirements**:
- Test all endpoint methods
- Test both success and failure scenarios
- Test schema validation with examples
- Mock external dependencies
- Use pytest fixtures and async testing
- Comprehensive assertions
- Clear test naming and documentation
</testing_requirements>

### 6. Documentation Generation
<documentation_requirements>
For each tag: `docs/api/{tag}.rst`

```rst
{Tag Name} API
==============

.. automodule:: abconnecttools.endpoints.{tag}
   :members:
   :undoc-members:
   :show-inheritance:

Models
------

.. automodule:: abconnecttools.models.{tag}
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------

Registration Example
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from abconnecttools import ABConnectClient
   from abconnecttools.models.account import RegistrationModel
   
   # Create client
   client = ABConnectClient(api_key="your_key")
   
   # Prepare registration data
   registration = RegistrationModel(
       email="user@company.com",
       password="SecurePassword123!",
       first_name="John",
       last_name="Doe"
   )
   
   # Register user
   user = await client.account.register_user(registration)
   print(f"Created user: {user.email}")

API Reference
-------------

.. automethod:: abconnecttools.endpoints.{tag}.{TagName}Endpoints.register_user
```

**Requirements**:
- Auto-generated from docstrings
- Include working code examples
- Link to models and schemas
- Show both simple and complex usage
- Include error handling examples
</documentation_requirements>

## Implementation Guidelines

### Code Quality Standards
<quality_standards>
- Type hints for all functions, methods, and variables
- Comprehensive docstrings following Google/NumPy style
- Error handling for all external calls
- Input validation using Pydantic
- Consistent naming conventions (PEP 8)
- No hardcoded values (use configuration)
- Logging for debugging and monitoring
- Performance considerations (async, caching)
</quality_standards>

### Best Practices
<best_practices>
1. **Schema First**: Always start with Pydantic models
2. **Validation**: Validate all inputs and outputs
3. **Error Handling**: Provide clear, actionable error messages
4. **Documentation**: Code should be self-documenting
5. **Testing**: Aim for >95% test coverage
6. **Performance**: Use async/await, connection pooling
7. **Security**: Validate all inputs, handle secrets properly
8. **Maintainability**: Clear separation of concerns
</best_practices>

### Migration Strategy
<migration_strategy>
1. **Backward Compatibility**: Keep existing API working
2. **Deprecation Warnings**: For old patterns
3. **Migration Guide**: Step-by-step upgrade instructions
4. **Dual Support**: Both old and new APIs during transition
5. **Gradual Rollout**: Module-by-module migration
</migration_strategy>

## Deliverables

<deliverables>
1. **Parsed swagger analysis** with complete schema and endpoint inventory
2. **Generated Pydantic models** for all swagger schemas
3. **Typed endpoint modules** organized by swagger tags
4. **Comprehensive test suite** with >95% coverage
5. **Professional example data** for all models
6. **Auto-generated documentation** with working examples
7. **Migration tools and guides** for smooth transition
8. **Performance benchmarks** comparing old vs new implementation
</deliverables>

## Success Criteria

<success_criteria>
- All 223+ endpoints have typed implementations
- 100% of swagger schemas converted to Pydantic models
- >95% test coverage across all modules
- Documentation builds without errors
- All examples in docs are executable
- Performance equal or better than current implementation
- Zero breaking changes to public API during transition
- Professional code quality suitable for enterprise use
</success_criteria>

---

**Note**: This is a large-scale refactoring project. Approach it systematically:
1. Start with swagger analysis and planning
2. Implement one tag/module completely as a template
3. Use code generation where appropriate
4. Test thoroughly at each step
5. Document as you build, not after

The goal is to transform this from a dynamic, loosely-typed package into a professional, enterprise-grade API client with full type safety, comprehensive testing, and excellent documentation.