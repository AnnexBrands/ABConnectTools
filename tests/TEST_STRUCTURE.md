# Test Suite Structure Plan

Following our constitution and matching the ABConnect package structure.

## Running Tests

### Individual Test Files
```bash
# Constitution compliance
python -m tests.test_constitution

# Swagger endpoint implementation check with tree output
python -m tests.api.swagger.test_all_swagger_endpoints_have_implementations

# Swagger compliance and coverage
python -m tests.api.swagger.test_compliance

# Swagger synchronization (reveals server gaps)
python -m tests.api.swagger.test_sync

# Core API functionality
python -m tests.api.test_api

# Builder functionality
python -m tests.builder.test_api_request_builder

# Quoter functionality
python -m tests.quoter.test_quoter
python -m tests.quoter.test_quick_quote
python -m tests.quoter.test_quote_request

# Loader functionality
python -m tests.loader.test_file_loader
```

### Module Groups
```bash
# All API tests
python -m unittest discover tests/api

# All builder tests
python -m unittest discover tests/builder

# All quoter tests
python -m unittest discover tests/quoter

# All loader tests
python -m unittest discover tests/loader

# All swagger tests
python -m unittest discover tests/api/swagger
```

### Comprehensive Test Runs
```bash
# All tests
python -m unittest discover tests

# Constitution and critical checks
python -m tests.test_constitution
python -m tests.api.swagger.test_all_swagger_endpoints_have_implementations

# Gap detection (critical for API evolution)
python -m tests.api.swagger.test_sync
```

### Visual Output Tests
```bash
# Tree structure of endpoint implementations
python -m tests.api.swagger.test_all_swagger_endpoints_have_implementations

# Swagger compliance report
python -m tests.api.swagger.test_compliance
```

## Complete Test Directory Structure

```
tests/
├── base_test.py                         # Base test classes (ABConnectTestCase, EndpointTestCase, ModelTestCase)
├── test_constitution.py                 # Constitution compliance tests
├── test_cli.py                          # CLI command tests
├── test_generic_endpoints.py            # Generic endpoint functionality tests
├── TEST_STRUCTURE.md                    # This documentation file
│
├── api/                                 # Tests for ABConnect.api module
│   ├── __init__.py                      # API test exports and base classes
│   ├── test_api.py                      # ABConnectAPI main class tests
│   ├── test_response_mapper.py          # ResponseMapper functionality tests
│   ├── test_query_builder.py            # QueryBuilder functionality tests
│   │
│   ├── swagger/                         # Swagger compliance and synchronization tests
│   │   ├── __init__.py                  # SwaggerEndpointChecker and utilities
│   │   ├── test_compliance.py           # Swagger compliance verification
│   │   ├── test_coverage.py             # Coverage metrics and gap analysis
│   │   └── test_sync.py                 # Swagger synchronization tests
│   │
│   ├── endpoints/                       # Tests for each API endpoint
│   │   ├── __init__.py                  # Endpoint test exports
│   │   ├── base_endpoint_test.py        # Base class for endpoint tests
│   │   ├── test_account.py              # Account endpoint tests
│   │   ├── test_address.py              # Address endpoint tests
│   │   ├── test_admin.py                # Admin endpoint tests
│   │   ├── test_companies.py            # Companies endpoint tests
│   │   ├── test_company.py              # Single company endpoint tests
│   │   ├── test_contacts.py             # Contacts endpoint tests
│   │   ├── test_dashboard.py            # Dashboard endpoint tests
│   │   ├── test_documents.py            # Documents endpoint tests
│   │   ├── test_e_sign.py               # E-signature endpoint tests
│   │   ├── test_email.py                # Email endpoint tests
│   │   ├── test_job.py                  # Job endpoint tests
│   │   ├── test_jobintacct.py           # Job integration tests
│   │   ├── test_lookup.py               # Lookup endpoint tests
│   │   ├── test_note.py                 # Notes endpoint tests
│   │   ├── test_notifications.py        # Notifications endpoint tests
│   │   ├── test_reports.py              # Reports endpoint tests
│   │   ├── test_rfq.py                  # RFQ endpoint tests
│   │   ├── test_shipment.py             # Shipment endpoint tests
│   │   ├── test_SmsTemplate.py          # SMS template endpoint tests
│   │   ├── test_users.py                # Users endpoint tests
│   │   ├── test_Values.py               # Values endpoint tests
│   │   ├── test_v2.py                   # V2 API endpoint tests
│   │   ├── test_v3.py                   # V3 API endpoint tests
│   │   ├── test_views.py                # Views endpoint tests
│   │   └── test_webhooks.py             # Webhooks endpoint tests
│   │
│   └── models/                          # Tests for Pydantic models
│       ├── __init__.py                  # Model test exports
│       ├── base_model_test.py           # Base class for model tests
│       ├── test_account_models.py       # Account-related models
│       ├── test_address_models.py       # Address-related models
│       ├── test_company_models.py       # Company-related models
│       ├── test_contact_models.py       # Contact-related models
│       ├── test_document_models.py      # Document-related models
│       ├── test_job_models.py           # Job-related models
│       ├── test_lookup_models.py        # Lookup-related models
│       ├── test_shared_models.py        # Shared/common models
│       └── test_user_models.py          # User-related models
│
├── builder/                             # Tests for ABConnect.Builder module
│   ├── __init__.py                      # BuilderTestCase base class
│   ├── test_api_request_builder.py      # APIRequestBuilder core functionality
│   ├── test_transformations.py          # Data transformation tests
│   ├── test_templates.py                # JSON template validation tests
│   └── test_request_patterns.py         # Request pattern tests
│
├── quoter/                              # Tests for ABConnect.Quoter module
│   ├── __init__.py                      # QuoterTestCase base class
│   ├── test_quoter.py                   # Quoter main class tests
│   ├── test_quick_quote.py              # Quick quote (qq) functionality
│   ├── test_quote_request.py            # Quote request (qr) functionality
│   └── test_pricing_engine.py           # Pricing calculation tests
│
└── loader/                              # Tests for ABConnect.Loader module
    ├── __init__.py                      # LoaderTestCase base class
    ├── test_file_loader.py              # FileLoader main functionality
    ├── test_csv_loading.py              # CSV file format support
    ├── test_json_loading.py             # JSON file format support
    ├── test_xlsx_loading.py             # Excel file format support
    └── test_encoding_detection.py       # Character encoding tests
```

## Why Each Component Is Needed

### Constitution Tests (`test_constitution.py`)
**Purpose**: Enforces our development constitution principles across the entire codebase.
- Validates docs → tests → code workflow compliance
- Ensures 1:1 relationship between endpoints and swagger.json
- Prevents violating files (like _enhanced.py duplicates)
- Validates that all swagger endpoints have implementations
- Ensures endpoint-model pairing requirements

### Swagger Tests (`api/swagger/`)
**Purpose**: Critical for maintaining API consistency and revealing gaps between server and wrapper.

#### `test_compliance.py`
- Validates that all swagger.json endpoints have corresponding implementation files
- Checks endpoint coverage metrics (currently 100%)
- Identifies orphaned endpoint files not in swagger

#### `test_sync.py` (moved from test_swagger_sync.py)
- Tests swagger synchronization functionality with remote server
- Validates local swagger.json is current with latest server specification
- **Critical**: Reveals gaps between latest server swagger and our wrapper
- Ensures we don't miss new API endpoints or changes
- Prevents version drift between server API and client implementation

#### `test_coverage.py` (future)
- Analyzes swagger coverage gaps
- Reports missing model mappings
- Tracks API evolution over time

### API Tests (`api/`)
**Purpose**: Validates the core API client functionality that everything else depends on.

#### Main API Tests
- `test_api.py`: Core ABConnectAPI client functionality
- `test_response_mapper.py`: Pydantic model casting system
- `test_query_builder.py`: Query building and filtering capabilities

#### Endpoint Tests (`api/endpoints/`)
**Purpose**: One test file per swagger endpoint group, ensuring complete coverage.
- Each endpoint test validates CRUD operations, error handling, and specific features
- Tests convenience methods like `companies.get(code)`
- Validates cache integration and model casting
- Tests endpoint-specific business logic

#### Model Tests (`api/models/`)
**Purpose**: Validates Pydantic model functionality grouped by domain.
- Model validation and serialization
- Field validation rules and constraints
- Model relationship testing
- JSON schema compliance

### Builder Tests (`builder/`)
**Purpose**: Validates dynamic API request construction from templates.
- `test_api_request_builder.py`: Core nested path updates with dot notation
- `test_transformations.py`: Data transformation for Regular vs 3PL jobs
- `test_templates.py`: JSON template validation and loading
- Critical for quote generation and job booking workflows

### Quoter Tests (`quoter/`)
**Purpose**: Validates quote generation engine that integrates Builder and API.
- `test_quoter.py`: Main quoter class and integration testing
- `test_quick_quote.py`: Fast quote generation (qq mode)
- `test_quote_request.py`: Full quote with booking capability (qr mode)
- Tests auto-booking functionality and pricing breakdowns

### Loader Tests (`loader/`)
**Purpose**: Validates robust file loading with format auto-detection.
- `test_file_loader.py`: Core loading functionality
- Format-specific tests for CSV, JSON, Excel
- Character encoding detection (critical for international data)
- Error handling for malformed files

## Inheritance Hierarchy

### Primary Base Classes (base_test.py)

1. **ABConnectTestCase**
   - Foundation for all tests
   - Provides swagger spec loading, project paths, common assertions
   - Constitution compliance helpers (assertEndpointExists, assertModelExists)

2. **EndpointTestCase** ← ABConnectTestCase
   - Base for all endpoint tests
   - Swagger compliance validation
   - Documentation and example requirements

3. **ModelTestCase** ← ABConnectTestCase
   - Base for all model tests
   - Pydantic validation and serialization helpers

### Module-Specific Base Classes

4. **BaseEndpointTest** (api/endpoints/) ← EndpointTestCase
   - API client setup and request helpers
   - Standard CRUD test patterns

5. **BaseModelTest** (api/models/) ← ModelTestCase
   - Model instantiation and validation helpers
   - JSON schema testing

6. **BuilderTestCase** (builder/) ← ABConnectTestCase
   - Template loading and path assertion helpers
   - Request building validation

7. **QuoterTestCase** (quoter/) ← ABConnectTestCase
   - Sample quote data creation
   - Price breakdown validation helpers

8. **LoaderTestCase** (loader/) ← ABConnectTestCase
   - Temporary file creation for testing
   - Format-specific validation helpers

## Test Naming Convention

- `test_<module>.py` - Tests for main module functionality
- `test_<feature>.py` - Tests for specific features within a module
- `test_<endpoint>_models.py` - Tests for models related to an endpoint domain
- All test classes start with `Test` (e.g., `TestCompaniesEndpoint`)
- All test methods start with `test_` (e.g., `test_get_by_code`)

## Critical Integration Points

1. **Swagger Sync** → Constitution Tests → Endpoint Tests
   - Swagger sync reveals new server endpoints
   - Constitution tests catch missing implementations
   - Endpoint tests validate functionality

2. **Builder** → Quoter Integration
   - Builder creates request templates
   - Quoter uses Builder for quote requests
   - Both tested independently and together

3. **API Client** → All Endpoint Tests
   - Central API client must work for all endpoint tests
   - Response mapping affects all model tests
   - Authentication flows affect all integration tests

This structure ensures comprehensive coverage while maintaining our constitutional principles and revealing any gaps between our wrapper and the evolving server API.