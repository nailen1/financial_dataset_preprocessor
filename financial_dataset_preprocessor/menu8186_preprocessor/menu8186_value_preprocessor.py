from .menu8186_consts import COLUMN_NAMES_PREPROCESSED_TOBE_NUMBER_MENU8186, COLUMN_NAME_RAW_FOR_FUND_CODE_MENU8186
from ..general_preprocess_utils import format_commaed_number, format_fund_code

def preprocess_cols_num_menu8186(df):
    for col in COLUMN_NAMES_PREPROCESSED_TOBE_NUMBER_MENU8186:
        df[col] = df[col].apply(format_commaed_number)
    return df

def preprocess_cols_fund_code_menu8186(df):
    df[COLUMN_NAME_RAW_FOR_FUND_CODE_MENU8186] = df[COLUMN_NAME_RAW_FOR_FUND_CODE_MENU8186].apply(format_fund_code)
    return df