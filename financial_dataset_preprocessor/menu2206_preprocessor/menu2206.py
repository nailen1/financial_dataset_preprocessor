from pandas import DataFrame
from financial_dataset_loader import load_menu2206
from .menu2206_column_preprocessor import get_preprocessed_column_names_menu2206
from .menu2206_value_preprocessor import preprocess_cols_num_menu2206, preprocess_cols_int_menu2206
from ..column_preprocessor_basis import remove_index_name, drop_first_row

def set_index_name_for_menu2206(df):
    df.index.name = '일자'
    return df

def preprocess_raw_menu2206(menu2206: DataFrame) -> DataFrame:
    return (
        menu2206
        .copy()
        .pipe(lambda df: df.set_axis(get_preprocessed_column_names_menu2206(df), axis=1))
        .pipe(set_index_name_for_menu2206)
        .pipe(drop_first_row)
        .pipe(preprocess_cols_num_menu2206)
        .pipe(preprocess_cols_int_menu2206)
    )

def get_preprocessed_menu2206(date_ref=None):
    return preprocess_raw_menu2206(load_menu2206(date_ref=date_ref))

map_raw_to_preprocessed_menu2206 = preprocess_raw_menu2206
map_date_ref_to_preprocessed_menu2206 = get_preprocessed_menu2206