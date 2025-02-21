from .menu4165_consts import COLUMN_NAMES_PREPROCESSED_TOBE_NUMBER_MENU4165, COLUMN_NAME_RAW_FOR_FUND_CODE_MENU4165
from ..general_preprocess_utils import format_commaed_number, format_fund_code

def preprocess_cols_num_menu4165(df):
    for col in COLUMN_NAMES_PREPROCESSED_TOBE_NUMBER_MENU4165:
        df[col] = df[col].apply(format_commaed_number)
    return df

def preprocess_cols_fund_code_menu4165(df):
    df[COLUMN_NAME_RAW_FOR_FUND_CODE_MENU4165] = df[COLUMN_NAME_RAW_FOR_FUND_CODE_MENU4165].apply(format_fund_code)
    return df
