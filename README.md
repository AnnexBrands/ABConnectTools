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

Run tests with:

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- **Documentation**: [https://abconnecttools.readthedocs.io/](https://abconnecttools.readthedocs.io/)
- **Repository**: [https://github.com/AnnexBrands/ABConnectTools](https://github.com/AnnexBrands/ABConnectTools)
- **Issue Tracker**: [https://github.com/AnnexBrands/ABConnectTools/issues](https://github.com/AnnexBrands/ABConnectTools/issues)
- **PyPI**: [https://pypi.org/project/ABConnect/](https://pypi.org/project/ABConnect/)