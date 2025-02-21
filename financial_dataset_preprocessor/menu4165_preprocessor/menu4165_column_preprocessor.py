import pandas as pd
from pandas import DataFrame
from ..column_preprocessor_basis import create_df_col_for_double_columns, clean_col1, fill_col1_values, combine_column_names_1, handle_empty_col2

def get_df_preprocessed_column_menu4165(menu4165: DataFrame) -> DataFrame:
    return (
        menu4165
        .pipe(create_df_col_for_double_columns)
        .pipe(clean_col1)
        .pipe(handle_empty_col2)
        .pipe(fill_col1_values)
        .pipe(combine_column_names_1)
    )

def get_preprocessed_column_names_menu4165(menu4165: DataFrame) -> list[str]:
    df = get_df_preprocessed_column_menu4165(menu4165)
    return list(df.iloc[:,-1])
