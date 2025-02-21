from pandas import DataFrame
from financial_dataset_loader import load_menu2205_snapshot, load_menu2205
from .menu2205_column_preprocessor import get_preprocessed_column_names_menu2205
from .menu2205_value_preprocessor import preprocess_cols_num_menu2205, preprocess_cols_int_menu2205
from ..column_preprocessor_basis import remove_index_name, drop_first_row

def preprocess_raw_menu2205(menu2205: DataFrame) -> DataFrame:
    return (
        menu2205
        .copy()
        .pipe(lambda df: df.set_axis(get_preprocessed_column_names_menu2205(df), axis=1))
        .pipe(remove_index_name)
        .pipe(drop_first_row)
        .pipe(preprocess_cols_num_menu2205)
        .pipe(preprocess_cols_int_menu2205)
    )

def get_preprocessed_menu2205_snapshot(date_ref=None):
    return preprocess_raw_menu2205(load_menu2205_snapshot(date_ref=date_ref))

def get_preprocessed_menu2205(fund_code, date_ref=None):
    return preprocess_raw_menu2205(load_menu2205(fund_code, date_ref=date_ref))

map_raw_to_preprocessed_menu2205 = preprocess_raw_menu2205
map_fund_code_to_preprocessed_menu2205_snapshot = get_preprocessed_menu2205_snapshot
map_fund_code_to_preprocessed_menu2205 = get_preprocessed_menu2205
