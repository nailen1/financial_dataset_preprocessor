from .menu2160_consts import COLUMN_NAMES_PREPROCESSED_TOBE_NUMBER_MENU2160, COLUMN_NAME_RAW_FOR_FUND_CODE_MENU2160
from ..general_preprocess_utils import format_commaed_number, format_fund_code

def preprocess_cols_num_menu2160(df):
    for col in COLUMN_NAMES_PREPROCESSED_TOBE_NUMBER_MENU2160:
        df[col] = df[col].apply(format_commaed_number)
    return df

def preprocess_cols_fund_code_menu2160(df):
    df[COLUMN_NAME_RAW_FOR_FUND_CODE_MENU2160] = df[COLUMN_NAME_RAW_FOR_FUND_CODE_MENU2160].apply(format_fund_code)
    return df