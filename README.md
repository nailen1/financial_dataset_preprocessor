# Financial Dataset Preprocessor

A Python package for preprocessing financial datasets from various sources. This package provides tools and utilities for cleaning, transforming, and preparing financial data for analysis.

## Features

- Menu 2205 Preprocessor
  - Corporation Name Finder
  - Domestic Beneficiary Certificates Processing
  - Domestic Bonds Analysis
  - Repo Agreement Processing
  - Borrowings Management
- Additional preprocessors for other financial datasets (coming soon)

## Installation

You can install the package using pip:

```bash
pip install financial_dataset_preprocessor
```

## Requirements

- Python >= 3.11
- Dependencies are listed in requirements.txt

## Usage Examples

### 1. Search for Funds with Bonds

```python
from financial_dataset_preprocessor import (
    search_funds_having_domestic_bonds,
    get_domestic_bonds_by_fund
)

# Get all funds that have domestic bonds
fund_bonds = search_funds_having_domestic_bonds(date_ref='2025-02-21')

# Get bond details for a specific fund
fund_code = '100075'
bond_details = get_domestic_bonds_by_fund(fund_code=fund_code, date_ref='2025-02-21')
```

### 2. Analyze Fund Borrowings

```python
from financial_dataset_preprocessor import (
    search_funds_having_borrowings,
    get_borriwings_by_fund
)

# Find funds with borrowings
funds_with_borrowings = search_funds_having_borrowings(date_ref='2025-02-21')

# Get borrowing details
fund_code = '100075'
borrowing_details = get_borriwings_by_fund(fund_code=fund_code, date_ref='2025-02-21')
```

### 3. Check Repo Agreements

```python
from financial_dataset_preprocessor import (
    search_funds_having_repos,
    get_repos_by_fund
)

# Find funds with repos
funds_with_repos = search_funds_having_repos(date_ref='2025-02-21')

# Get repo details for a specific fund
fund_code = '100075'
repo_details = get_repos_by_fund(fund_code=fund_code, date_ref='2025-02-21')
```

## Development

To set up the development environment:

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under a proprietary license. All rights reserved.

### Terms of Use

- Source code viewing and forking is allowed
- Commercial use is prohibited without explicit permission
- Redistribution or modification of the code is prohibited
- Academic and research use is allowed with proper attribution

## Author

**June Young Park**  
AI Management Development Team Lead & Quant Strategist at LIFE Asset Management

LIFE Asset Management is a hedge fund management firm that integrates value investing and engagement strategies with quantitative approaches and financial technology, headquartered in Seoul, South Korea.

### Contact

- Email: juneyoungpaak@gmail.com
- Location: TWO IFC, Yeouido, Seoul
