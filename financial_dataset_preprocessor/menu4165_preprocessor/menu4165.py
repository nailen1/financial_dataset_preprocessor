from pandas import DataFrame
from financial_dataset_loader import load_menu4165, load_menu4165_snapshot
from .menu4165_column_preprocessor import get_preprocessed_column_names_menu4165
from .menu4165_value_preprocessor import preprocess_cols_num_menu4165, preprocess_cols_fund_code_menu4165
from ..row_preprocessor import drop_non_indexed_rows

def preprocess_raw_menu4165(menu4165: DataFrame) -> DataFrame:
    return (
        menu4165
        .copy()
        .pipe(preprocess_cols_fund_code_menu4165)
        .pipe(lambda df: df.set_axis(get_preprocessed_column_names_menu4165(df), axis=1))
        .assign(순자산편입비=lambda df: df['순자산편입비'].str.replace('%',''))
        .pipe(preprocess_cols_num_menu4165)
        .pipe(drop_non_indexed_rows)
        .pipe(lambda df: df.set_index('펀드'))
    )

def get_preprocessed_menu4165(fund_code, date_ref=None):
    return preprocess_raw_menu4165(load_menu4165(fund_code=fund_code, date_ref=date_ref))

def get_preprocessed_menu4165_snapshot(fund_code, date_ref=None):
    return preprocess_raw_menu4165(load_menu4165_snapshot(fund_code=fund_code, date_ref=date_ref))

map_raw_to_preprocessed_menu4165 = preprocess_raw_menu4165
map_fund_code_to_preprocessed_menu4165 = get_preprocessed_menu4165
map_fund_code_to_preprocessed_menu4165_snapshot = get_preprocessed_menu4165_snapshot
