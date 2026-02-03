# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## CONSTITUTION

Development follows a plan of add docs, add tests, write code, pass tests, review/improve.

**API Endpoint Organization:**
- All endpoints are organized by their API path
- Endpoints and models maintain a 1:1 relationship with swagger.json
- Swagger tests alert when manual endpoint creation is needed (endpoints are not auto-generated)
- Each endpoint requires:
  - Corresponding Pydantic models
  - Example usage in documentation
  - Unit tests
  - Endpoint implementation

**Four-Way Harmony Requirement:**
For each API endpoint/path, maintain consistency across:
1. **Sphinx Documentation** (`docs/`) - API reference and examples
2. **Example Files** (`examples/`) - Working code demonstrations
3. **Unit Tests** (`tests/`) - Comprehensive test coverage
4. **Implementation** (`ABConnect/api/endpoints/` + `ABConnect/api/models/`) - Actual code

When adding a new endpoint:
- Create example file showing Python API, CLI (without raw), and curl usage
- Add unit tests covering all endpoint methods
- Update sphinx docs with model documentation
- Ensure Pydantic models have descriptive __repr__ methods
- Verify CLI suggestions use friendly/tagged methods, not raw API calls

## Virtual Environment

**IMPORTANT**: Create and activate a virtual environment before running any Python or pip commands:
```bash
python -m venv .venv
source .venv/bin/activate
```

All Python and pip commands should be run within the activated virtual environment to ensure correct dependencies and isolation.

## Development Commands

### Installation
```bash
# Install in development mode with all dependencies
pip install -e .[dev]

# Install documentation dependencies
pip install -e .[docs]
```

### Testing
```bash
pytest                          # Run all tests (uses .env.staging automatically)
pytest tests/test_api.py        # Run specific test file
pytest -v                       # Run tests with verbose output
python -m pytest tests/        # Alternative test runner
```

### Environment Configuration
Tests automatically use `.env.staging` configuration. To run with production config:
```bash
ABC_ENVIRONMENT=production pytest  # Force production environment
```

Create `.env.staging` from the sample:
```bash
cp .env.sample .env.staging
# Edit .env.staging with staging credentials
```

Required environment variables:
- `ABCONNECT_USERNAME`: API username
- `ABCONNECT_PASSWORD`: API password  
- `ABC_CLIENT_ID`: Client ID for API access
- `ABC_CLIENT_SECRET`: Client secret for API access
- `ABC_ENVIRONMENT`: 'staging' or 'production' (defaults to production)

### Documentation
```bash
# Build Sphinx documentation locally
cd docs
make html                       # Build HTML docs to _build/html/
make clean                      # Clean build directory
make html                       # Rebuild from scratch

# Serve documentation locally (port 8080 to avoid Django collision)
make serve                      # Static server at http://localhost:8080
make livehtml                   # Live reload server (auto-rebuild on changes)

# Check for broken links and references
make linkcheck                  # Verify all external links

# Generate API documentation (when swagger.json changes)
python generate_api_docs_enhanced.py  # Regenerate API docs from swagger
```

Documentation is hosted at: https://abconnecttools.readthedocs.io

**Daily Documentation Workflow:**
1. Activate virtual environment: `source .venv/bin/activate`
2. Make code changes with proper docstrings
3. Update relevant .rst files if needed
4. Build docs locally: `cd docs && make html`
5. Review changes in `_build/html/index.html`
6. Run tests to ensure examples work: `pytest`
7. Push changes (ReadTheDocs auto-rebuilds)

### Building and Publishing
```bash
python -m build                 # Build distribution packages
twine upload dist/*             # Upload to PyPI (requires credentials)
```

## Code Architecture

ABConnect is a Python package for Annex Brands data processing and API interactions, structured in four main modules:

### Core Modules

#### Builder (`ABConnect.Builder`)
`APIRequestBuilder` class dynamically constructs API requests from static JSON templates in `base/` directory. Key features:
- Supports nested path updates via dot notation
- Handles transformations for both Regular and 3PL job types
- Base templates: `simple_request.json`, `extra_containers.json`

#### Quoter (`ABConnect.Quoter`)
`Quoter` class handles ABC API quote operations with two modes:
- Quick Quote (qq): Fast quote generation
- Quote Request (qr): Full quote with booking capability
- Integrates with Builder for request construction
- Supports auto-booking functionality

#### Loader (`ABConnect.Loader`)
`FileLoader` class provides robust file loading with:
- Format support: CSV, JSON, XLSX
- Automatic encoding detection via chardet
- Character handling for unsupported characters
- Interactive mode for user prompts

#### API (`ABConnect.api`)
Full-featured API client
1. **Python**: Direct endpoint methods (`api.sms_template.get_notificationtokens()`)
2. **CLI**: Endpoint commands (`ab smstemplate get_notificationtokens`)

#### CATALOG-API
Separate base_url and endpoints, same auth. Work toward seamless.

**Usage Guidelines:**
- Use friendly CLI/Python methods when available (no parameters needed)
- We have ACPortal_swagger_latest.json which gives schemas which may be behind or missing.
- We use examples to create json fixtures to get a real response.
- We use models which should always reconcide the fixture to the schema. 
  - Models should be commented when swagger is wrong.
  - Models should strictly name all optional columns.
  - Models using base inheritance should be invisible to the user, that is, inspecting a fixture should be enough to know how to access a pydantic object.
- We use tests to ensure that both a new call to the endpoint and validating a fixture against a model are both successful.

### API Client Structure
- **Endpoint Classes**: Users, Companies, Contacts, Docs, Forms, Items, Jobs, Tasks
- **Base Classes**: `BaseEndpoint` provides common functionality
- **Authentication**: Token storage supports both file-based (standalone) and session-based (Django) modes
- **Pydantic Models**: Type-safe request/response validation
- **Routes**: Always store expected request and response objects as well as kwargs for url and get params.

### Key Design Patterns
- **Template-based requests**: JSON templates in `base/` define request structures dynamically modified at runtime
- **Endpoint abstraction**: Each API resource has dedicated endpoint class inheriting from `BaseEndpoint`
- **Flexible authentication**: Token storage abstraction supports both standalone and Django-integrated usage
- **Environment switching**: Staging vs production controlled via `env` parameter or `ABC_ENVIRONMENT` variable
- **Auto-discovery**: Tests should warn if any swagger endpoints are not implemented.

### Configuration Files
- `base/ACPortal_swagger_latest.json`: OpenAPI specification for endpoint discovery
- `base/simple_request.json`: Default API request template
- `base/extra_containers.json`: Additional container configs for 3PL requests

## Domain Knowledge

### Data Format Standards

**URL Format**
-- make request url is expected to have "double api" like https://portal.abconnect.co/api/api/documents
-- except https://catalog-api.abconnect.co/api/Catalog has single.

**Job IDs:**
- Format: UUID (string)
- Test job ID: `"550e8400-e29b-41d4-a716-446655440000"`
- Example usage: `job_id="550e8400-e29b-41d4-a716-446655440000"`

**Job Display IDs:**
- Format: Integer (not string)
- Test job display ID: `2000000`
- Example usage: `job_display_id=2000000`, `JobDisplayId=2000000`

**Item IDs:**
- Format: UUID (string) for most operations
- Test item ID: `"550e8400-e29b-41d4-a716-446655440001"`
- Example usage: `itemid="550e8400-e29b-41d4-a716-446655440001"`, `item_id="550e8400-e29b-41d4-a716-446655440001"`

**Document Types:**
- Item Photo: `document_type=6`

**Sharing Levels:**
- Bitwise
- all agents: `shared=28`

### Test Data Standards

When writing tests and examples, always use these consistent values:
- Job ID: `"550e8400-e29b-41d4-a716-446655440000"` (UUID)
- Job Display ID: `2000000` (integer)
- Item ID: `"550e8400-e29b-41d4-a716-446655440001"` (UUID)
- RFQ ID: `987` (when needed)

This ensures realistic test scenarios since most jobs don't have 100+ items.

## Requirements

- Python 3.11+ required
- Key dependencies: pydantic>=2.0, pandas, requests, python-dotenv, beautifulsoup4, openpyxl, Pillow
- Development dependencies: pytest, build, twine
- Documentation dependencies: sphinx, sphinx-rtd-theme, myst-parser