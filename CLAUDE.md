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
Full-featured API client with three access layers:
1. **Raw**: Direct endpoint access (`api.raw.get('/api/companies/{id}')`)
2. **Tagged**: Auto-generated from swagger tags (`api.companies.get_details()`)
3. **Friendly**: Manual convenience methods (`api.companies.get_by_code()`)

### API Client Structure
- **Endpoint Classes**: Users, Companies, Contacts, Docs, Forms, Items, Jobs, Tasks
- **Base Classes**: `BaseEndpoint` provides common functionality
- **Authentication**: Token storage supports both file-based (standalone) and session-based (Django) modes
- **Generic Endpoints**: 223+ endpoints auto-discovered from OpenAPI spec
- **Query Builder**: Fluent interface for complex API queries
- **Pydantic Models**: Type-safe request/response validation

### Key Design Patterns
- **Template-based requests**: JSON templates in `base/` define request structures dynamically modified at runtime
- **Endpoint abstraction**: Each API resource has dedicated endpoint class inheriting from `BaseEndpoint`
- **Flexible authentication**: Token storage abstraction supports both standalone and Django-integrated usage
- **Environment switching**: Staging vs production controlled via `env` parameter or `ABC_ENVIRONMENT` variable
- **Auto-discovery**: Generic endpoints automatically generated from swagger.json specification

### Configuration Files
- `base/simple_request.json`: Default API request template
- `base/extra_containers.json`: Additional container configs for 3PL requests
- `base/companies.json`: Static company reference data
- `base/statuses.json`: Static status reference data
- `base/swagger.json`: OpenAPI specification for endpoint discovery

## Requirements

- Python 3.11+ required
- Key dependencies: pydantic>=2.0, pandas, requests, python-dotenv, beautifulsoup4, openpyxl
- Development dependencies: pytest, build, twine
- Documentation dependencies: sphinx, sphinx-rtd-theme, myst-parser