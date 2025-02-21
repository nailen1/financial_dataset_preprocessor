from pandas import DataFrame
from financial_dataset_loader import load_menu_snapshot

from financial_dataset_preprocessor.column_preprocessor_basis.office_system_column_basis import set_col_as_index

def preprocess_raw_menu3421(menu3421: DataFrame) -> DataFrame:
    return (
        menu3421
        .pipe(set_col_as_index, col='펀드')
    )

def get_preprocessed_menu3421(date_ref=None):
    return preprocess_raw_menu3421(load_menu_snapshot('3421', date_ref=date_ref))

map_raw_to_preprocessed_menu3421 = preprocess_raw_menu3421
map_fund_code_to_preprocessed_menu3421 = get_preprocessed_menu3421
