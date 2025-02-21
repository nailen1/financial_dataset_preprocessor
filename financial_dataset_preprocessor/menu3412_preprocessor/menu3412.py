from pandas import DataFrame
from financial_dataset_loader import load_menu_snapshot
from .menu3412_column_preprocessor import get_preprocessed_column_names_menu3412
from ..row_preprocessor import drop_non_indexed_rows


def keep_last_duplicate_index(df: DataFrame) -> DataFrame:
   return df[~df.index.duplicated(keep='last')]

def preprocess_raw_menu3412(menu3412: DataFrame) -> DataFrame:
    return (
        menu3412
        .copy()
        .pipe(lambda df: df.set_axis(get_preprocessed_column_names_menu3412(df), axis=1))
        .pipe(keep_last_duplicate_index)
    )


def get_preprocessed_menu3412(date_ref=None):
    return preprocess_raw_menu3412(load_menu_snapshot(menu_code='3412', date_ref=date_ref))

map_raw_to_preprocessed_menu3412 = preprocess_raw_menu3412
map_fund_code_to_preprocessed_menu3412 = get_preprocessed_menu3412
