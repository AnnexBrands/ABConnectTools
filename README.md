# ABConnect

[![Documentation Status](https://readthedocs.org/projects/abconnecttools/badge/?version=latest)](https://abconnecttools.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/ABConnect.svg)](https://badge.fury.io/py/ABConnect)
[![Python Support](https://img.shields.io/pypi/pyversions/ABConnect.svg)](https://pypi.org/project/ABConnect/)

ABConnect is a Python package that provides a collection of tools for connecting and processing data for Annex Brands. It includes modules for quoting, building, and loading data from various file formats (CSV, JSON, XLSX), with a focus on handling unsupported characters and encoding issues seamlessly.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Builder](#builder)
  - [Quoter](#quoter)
- [Development](#development)
- [License](#license)

## Features

### New in v0.1.8
- **Generic Endpoint System:** Automatic access to all 223+ API endpoints without manual implementation
- **Fluent Query Builder:** Build complex API queries with method chaining
- **Pydantic Models:** Type-safe response models with automatic validation

### Core Features
- **API Request Builder:** Assemble dynamic API requests using static JSON templates and runtime updates.
- **Quoter Module:** Retrieve and parse quotes from the ABC API in both Quick Quote (qq) and Quote Request (qr) modes.
- **Robust Data Loading:** Supports CSV, JSON, and XLSX files with built-in encoding and character handling.
- **Full API Client:** Comprehensive API client with authentication and endpoint-specific methods.

## Installation

You can install ABConnect using pip:

```bash
pip install ABConnect
```

For more detailed installation instructions and documentation, visit [https://abconnecttools.readthedocs.io/](https://abconnecttools.readthedocs.io/)

## Configuration

### Environment Variables

ABConnect requires the following environment variables for authentication:

```bash
# Create a .env file with your credentials
ABCONNECT_USERNAME=your_username
ABCONNECT_PASSWORD=your_password
ABC_CLIENT_ID=your_client_id
ABC_CLIENT_SECRET=your_client_secret

# Optional: Set environment (defaults to production)
ABC_ENVIRONMENT=staging  # or 'production'
```

### Using Different Environments

ABConnect supports both staging and production environments:

```python
from ABConnect.api import ABConnectAPI

# Use staging environment
api = ABConnectAPI(env='staging')

# Use production environment (default)
api = ABConnectAPI()

# Environment can also be set via ABC_ENVIRONMENT variable
```

### Testing Configuration

For testing, create a `.env.staging` file with staging credentials:

```bash
cp ABConnect/dotenv.sample .env.staging
# Edit .env.staging with your staging credentials
```

Tests will automatically use `.env.staging` when running with pytest.

## Documentation

Full documentation is available at [https://abconnecttools.readthedocs.io/](https://abconnecttools.readthedocs.io/)

## Development

To contribute to ABConnect, clone the repository and install in development mode:

```bash
git clone https://github.com/AnnexBrands/ABConnectTools.git
cd ABConnectTools
pip install -e .[dev]
```

### Testing

Run all tests with:

```bash
pytest
```

#### Testing Model Implementation Against Swagger

ABConnect maintains strict alignment with the API's swagger specification. Several tests verify that all models and endpoints are properly implemented:

**1. Test All Endpoints Have Implementations**
```bash
# Comprehensive test with visual tree output showing which endpoints are implemented
pytest tests/api/swagger/test_all_swagger_endpoints_have_implementations.py -v

# Displays:
# ✅ Working endpoints with path count
# ❌ Missing endpoint files
# ⚠️  Import failures for endpoints that exist but can't be imported
```

**2. Test Constitution Compliance**
```bash
# Tests endpoint-model pairing and swagger-first principles
pytest tests/test_constitution.py -v

# Verifies:
# - All swagger endpoints have implementations
# - Endpoints have corresponding Pydantic models
# - No duplicate or violating files exist
```

**3. Verify Model Imports**
```bash
# Test that all models can be imported without errors
python -c "from ABConnect.api.models import shared, companies, contacts, job, address, jobtimeline; print('All model imports successful')"

# Test specific model validation and inspect fields
python -c "from ABConnect.api.models.jobparcelitems import ParcelItem; print(list(ParcelItem.model_fields.keys()))"
```

**4. Run Specific Test Categories**
```bash
# Test only API endpoints
pytest tests/api/ -v

# Test only models
pytest tests/api/models/ -v

# Test swagger compliance with detailed output
pytest tests/api/swagger/ -v -s
```

**Test Coverage Summary**
- **Endpoint Tests**: Verify all 223+ API endpoints are accessible
- **Model Tests**: Validate Pydantic models match swagger schemas
- **Integration Tests**: Test end-to-end API workflows
- **Constitution Tests**: Ensure code follows architecture principles

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- **Documentation**: [https://abconnecttools.readthedocs.io/](https://abconnecttools.readthedocs.io/)
- **Repository**: [https://github.com/AnnexBrands/ABConnectTools](https://github.com/AnnexBrands/ABConnectTools)
- **Issue Tracker**: [https://github.com/AnnexBrands/ABConnectTools/issues](https://github.com/AnnexBrands/ABConnectTools/issues)
- **PyPI**: [https://pypi.org/project/ABConnect/](https://pypi.org/project/ABConnect/)