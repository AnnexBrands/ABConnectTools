# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Virtual Environment

**IMPORTANT**: Always activate the virtual environment before running any Python or pip commands:
```bash
source claude-env/bin/activate
```

All Python and pip commands should be run within the activated virtual environment to ensure correct dependencies and isolation.

## Development Commands

### Testing
```bash
pytest                          # Run all tests (uses .env.staging automatically)
pytest tests/test_api.py        # Run specific test file
python -m pytest tests/        # Alternative test runner
```

### Environment Configuration
Tests automatically use `.env.staging` configuration. To run with production config:
```bash
ABC_ENVIRONMENT=production pytest  # Force production environment
```

Create `.env.staging` from the sample:
```bash
cp ABConnect/dotenv.sample .env.staging
# Edit .env.staging with staging credentials
```

### Building and Publishing
```bash
python -m build                 # Build distribution packages
pip install -e .               # Install in development mode
twine upload dist/*             # Upload to PyPI (after build)
```

### Installation
```bash
pip install -e .[dev]          # Install with development dependencies
```

## Code Architecture

ABConnect is a Python package for Annex Brands data processing and API interactions, structured in four main modules:

### Core Modules
- **Builder (`ABConnect.Builder`)**: `APIRequestBuilder` class dynamically constructs API requests from static JSON templates in `base/` directory. Supports nested path updates and transformations for both Regular and 3PL job types.

- **Quoter (`ABConnect.Quoter`)**: `Quoter` class handles ABC API quote operations with two modes - Quick Quote (qq) and Quote Request (qr). Integrates with Builder for request construction and supports auto-booking functionality.

- **Loader (`ABConnect.Loader`)**: `FileLoader` class provides robust file loading for CSV, JSON, and XLSX formats with automatic encoding detection and character handling.

- **API (`ABConnect.api`)**: Full-featured API client with endpoint-specific classes (Users, Companies, Contacts, Docs, Forms, Items, Jobs, Tasks). Uses token storage system supporting both file-based and session-based authentication for Django compatibility.

### Key Design Patterns
- **Template-based requests**: JSON templates in `base/` directory define request structures that are dynamically modified at runtime
- **Endpoint abstraction**: Each API resource has dedicated endpoint class inheriting from `BaseEndpoint`
- **Flexible authentication**: Token storage abstraction supports both standalone and Django-integrated usage
- **Environment switching**: Staging vs production environments controlled via `env` parameter

### Configuration Files
- `base/simple_request.json`: Default API request template
- `base/extra_containers.json`: Additional container configurations for 3PL requests
- `base/companies.json`, `base/statuses.json`: Static reference data

The package requires Python 3.11+ and is designed for internal Annex Brands workflows with ABC API integration.