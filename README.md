# ABConnect

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

- **API Request Builder:** Assemble dynamic API requests using static JSON templates and runtime updates.
- **Quoter Module:** Retrieve and parse quotes from the ABC API in both Quick Quote (qq) and Quote Request (qr) modes.
- **Robust Data Loading:** Supports CSV, JSON, and XLSX files with built-in encoding and character handling.
- **Centralized Constants:** Manage API keys and configuration values via a dedicated module.

## Installation

You can install ABConnect using pip:

```bash
pip install ABConnect