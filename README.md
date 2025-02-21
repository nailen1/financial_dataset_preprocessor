# Financial Dataset Preprocessor

A Python package for preprocessing financial datasets from various sources. This package provides tools and utilities for cleaning, transforming, and preparing financial data for analysis.

## Features

- Menu 2205 Preprocessor
  - Corporation Name Finder
  - Domestic Beneficiary Certificates Processing
- Additional preprocessors for other financial datasets (coming soon)

## Installation

You can install the package using pip:

```bash
pip install financial-dataset-preprocessor
```

## Requirements

- Python >= 3.11
- Dependencies are listed in requirements.txt

## Usage

```python
from financial_dataset_preprocessor.menu2205_preprocessor import corpname_finder

# Example usage
df_holdings = corpname_finder.get_df_fund_holdings_corpname(...)
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

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
