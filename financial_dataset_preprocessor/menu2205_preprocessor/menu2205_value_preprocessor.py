from .menu2205_consts import COLUMN_NAMES_PREPROCESSED_TOBE_NUMBER_MENU2205, COLUMN_NAMES_PREPROCESSED_TOBE_INTEGER_MENU2205
from ..value_preprocessor_basis import preprocess_column_values_to_numbers, preprocess_column_value_to_integers


def preprocess_cols_num_menu2205(df):
    df = preprocess_column_values_to_numbers(df, cols=COLUMN_NAMES_PREPROCESSED_TOBE_NUMBER_MENU2205)
    return df

def preprocess_cols_int_menu2205(df):
    df = preprocess_column_value_to_integers(df, cols=COLUMN_NAMES_PREPROCESSED_TOBE_INTEGER_MENU2205)
    return df
