from pandas import DataFrame
from financial_dataset_loader import load_menu8186_snapshot

from financial_dataset_preprocessor.column_preprocessor_basis.office_system_column_basis import set_col_as_index
from .menu8186_column_preprocessor import get_preprocessed_column_names_menu8186
from .menu8186_value_preprocessor import preprocess_cols_num_menu8186, preprocess_cols_fund_code_menu8186
from ..row_preprocessor import drop_non_indexed_rows
from ..column_preprocessor_basis import remove_index_name

def preprocess_raw_menu8186(menu8186: DataFrame) -> DataFrame:
    return (
        menu8186
        .copy()
        .pipe(preprocess_cols_fund_code_menu8186)
        .pipe(lambda df: df.set_axis(get_preprocessed_column_names_menu8186(df), axis=1))
        .pipe(preprocess_cols_num_menu8186)
        .pipe(drop_non_indexed_rows)
        .pipe(lambda df:set_col_as_index(df, '펀드코드'))
        .pipe(remove_index_name)
    )


def get_preprocessed_menu8186_snapshot(date_ref=None):
    return preprocess_raw_menu8186(load_menu8186_snapshot(date_ref=date_ref))

# def get_preprocessed_menu8186(fund_code):
#     return preprocess_raw_menu8186(load_menu8186(fund_code))

map_raw_to_preprocessed_menu8186 = preprocess_raw_menu8186
map_fund_code_to_preprocessed_menu8186_snapshot = get_preprocessed_menu8186_snapshot
