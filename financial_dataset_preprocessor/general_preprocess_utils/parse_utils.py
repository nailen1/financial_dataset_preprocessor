
import pandas as pd
import numpy as np


def parse_commaed_number(value) -> float | None:
   if pd.isna(value):
       return None
       
   if isinstance(value, (int, float)):
       return float(value)
       
   if isinstance(value, str):
       # Remove whitespace and commas
       cleaned = value.strip().replace(',', '')
       
       # Handle empty string
       if not cleaned:
           return None
           
       try:
           return float(cleaned)
       except ValueError:
           return None
           
   # For any other type (e.g. numpy numbers)
   try:
       return float(value)
   except (ValueError, TypeError):
       return None

def force_int(number):
    if isinstance(number, float) and number.is_integer():
        return int(number)
    return number

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

def ensure_n_digits_code(corpcode, n):
    if pd.isna(corpcode):
        return None
    if isinstance(corpcode, float):
        corpcode = str(int(corpcode)).replace('.0', '').zfill(n)
    elif isinstance(corpcode, int):
        corpcode = str(corpcode).zfill(n)
    elif isinstance(corpcode, str):
        corpcode = corpcode.replace('.0', '').zfill(n)
    elif isinstance(corpcode, np.number):
        corpcode = str(int(corpcode)).replace('.0', '').zfill(n)
    return corpcode
