from pandas import DataFrame
from financial_dataset_loader import load_menu_snapshot
from .menu2110_consts import COLUMN_NAMES_MENU2110_PREPROCESSED
from ..column_preprocessor_basis import remove_index_name, drop_first_row, set_col_as_index

def fill_class_with_nan(df):
    df['클래스구분'] = df['클래스구분'].fillna('-')
    df['클래스'] = df['클래스'].fillna('-')
    return df

def preprocess_raw_menu2110(menu2110: DataFrame) -> DataFrame:
    return (
        menu2110
        .copy()
        .pipe(lambda df: df.set_axis(COLUMN_NAMES_MENU2110_PREPROCESSED, axis=1))
        .pipe(drop_first_row)
        .pipe(fill_class_with_nan)
        .pipe(lambda df: df.rename_axis('펀드명').reset_index())
        .pipe(lambda df: set_col_as_index(df, '펀드'))
        .pipe(remove_index_name)
    )

def get_preprocessed_menu2110(date_ref=None):
    return preprocess_raw_menu2110(load_menu_snapshot('2110', date_ref=date_ref))

map_raw_to_preprocessed_menu2110 = preprocess_raw_menu2110
map_fund_code_to_preprocessed_menu2110 = get_preprocessed_menu2110
