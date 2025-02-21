import pandas as pd
from pandas import DataFrame
from ..column_preprocessor_basis import create_df_col_for_single_columns, clean_col1, process_return_column_from_col1_to_col2, fill_col1_values, handle_empty_col2, combine_column_names_1

def get_df_preprocessed_column_menu8186(menu8186: DataFrame) -> DataFrame:
    return (
        menu8186
        .pipe(create_df_col_for_single_columns)
        .pipe(clean_col1)
        .pipe(process_return_column_from_col1_to_col2)
        .pipe(fill_col1_values)
        .pipe(handle_empty_col2)
        .pipe(combine_column_names_1)
    )

def get_preprocessed_column_names_menu8186(menu8186: DataFrame) -> list[str]:
    df = get_df_preprocessed_column_menu8186(menu8186)
    return list(df.iloc[:,-1])