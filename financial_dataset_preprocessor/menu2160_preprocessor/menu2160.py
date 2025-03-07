from pandas import DataFrame
from financial_dataset_loader import load_menu2160, load_menu2160_snapshot
from .menu2160_column_preprocessor import get_preprocessed_column_names_menu2160
from .menu2160_value_preprocessor import preprocess_cols_num_menu2160, preprocess_cols_fund_code_menu2160
from ..row_preprocessor import drop_non_indexed_rows

def preprocess_raw_menu2160(menu2160: DataFrame) -> DataFrame:
    return (
        menu2160
        .copy()
        .pipe(preprocess_cols_fund_code_menu2160)
        .pipe(lambda df: df.set_axis(get_preprocessed_column_names_menu2160(df), axis=1))
        .pipe(preprocess_cols_num_menu2160)
        .pipe(drop_non_indexed_rows)
    )

def get_preprocessed_menu2160(fund_code):
    return preprocess_raw_menu2160(load_menu2160(fund_code))

def get_preprocessed_menu2160_snapshot(date_ref=None):
    return preprocess_raw_menu2160(load_menu2160_snapshot(date_ref=date_ref))

map_raw_to_preprocessed_menu2160 = preprocess_raw_menu2160
map_fund_code_to_preprocessed_menu2160 = get_preprocessed_menu2160
map_fund_code_to_preprocessed_menu2160_snapshot = get_preprocessed_menu2160_snapshot
