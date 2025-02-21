from .menu3421_consts import COLUMN_NAMES_PREPROCESSED_TOBE_NUMBER_MENU3421, COLUMN_NAMES_PREPROCESSED_TOBE_INTEGER_MENU3421
from ..value_preprocessor_basis import preprocess_column_values_to_numbers, preprocess_column_value_to_integers


def preprocess_cols_num_menu3421(df):
    df = preprocess_column_values_to_numbers(df, cols=COLUMN_NAMES_PREPROCESSED_TOBE_NUMBER_MENU3421)
    return df

def preprocess_cols_int_menu3421(df):
    df = preprocess_column_value_to_integers(df, cols=COLUMN_NAMES_PREPROCESSED_TOBE_INTEGER_MENU3421)
    return df
