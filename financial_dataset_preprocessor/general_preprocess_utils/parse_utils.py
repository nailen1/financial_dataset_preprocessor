
import pandas as pd
import numpy as np
from typing import Union, Optional

# 2025-05-26 refactored
def is_missing_value(value) -> bool:
    return pd.isna(value)

def is_numeric_type(value) -> bool:
    return isinstance(value, (int, float))

def is_string_type(value) -> bool:
    return isinstance(value, str)

def clean_string_number(text: str) -> str:
    return text.strip().replace(',', '')

def is_empty_string(text: str) -> bool:
    return not text

def try_convert_to_float(value) -> Optional[float]:
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def convert_string_to_float(text: str) -> Optional[float]:
    cleaned = clean_string_number(text)
    return None if is_empty_string(cleaned) else try_convert_to_float(cleaned)

def parse_commaed_number(value) -> Optional[float]:
    if is_missing_value(value):
        return None
    if is_numeric_type(value):
        return float(value)
    if is_string_type(value):
        return convert_string_to_float(value)
    return try_convert_to_float(value)

def is_integer_float(number: Optional[float]) -> bool:
    return isinstance(number, float) and number.is_integer()

def convert_float_to_int(number: float) -> int:
    return int(number)

def force_int(number) -> Union[int, float, None]:
    parsed = parse_commaed_number(number)
    return convert_float_to_int(parsed) if is_integer_float(parsed) else parsed


def transform_fund_code_float_to_string(fund_code):    
    if pd.isna(fund_code):
        return None    
    if isinstance(fund_code, float):
        fund_code = str(int(fund_code)).replace('.0', '').zfill(6)
    elif isinstance(fund_code, int):
        fund_code = str(fund_code).zfill(6)
    elif isinstance(fund_code, str):
        fund_code = fund_code.replace('.0', '').zfill(6)
    elif isinstance(fund_code, np.number):
        fund_code = str(int(fund_code)).replace('.0', '').zfill(6)
    return fund_code

def ensure_n_digits_code(code, n):
    if pd.isna(code):
        return None
    if isinstance(code, float):
        code = str(int(code)).replace('.0', '').zfill(n)
    elif isinstance(code, int):
        code = str(code).zfill(n)
    elif isinstance(code, str):
        code = code.replace('.0', '').zfill(n)
    elif isinstance(code, np.number):
        code = str(int(code)).replace('.0', '').zfill(n)
    return code
