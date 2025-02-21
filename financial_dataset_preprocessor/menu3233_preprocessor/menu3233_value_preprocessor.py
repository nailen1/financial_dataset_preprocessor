from .menu3233_consts import COLUMN_NAMES_PREPROCESSED_TOBE_NUMBER_MENU3233
from ..value_preprocessor_basis import preprocess_column_values_to_numbers 


def preprocess_cols_num_menu3233(df):
    df = preprocess_column_values_to_numbers(df, cols=COLUMN_NAMES_PREPROCESSED_TOBE_NUMBER_MENU3233)
    return df
