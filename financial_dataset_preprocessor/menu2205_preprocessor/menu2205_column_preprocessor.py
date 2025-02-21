import pandas as pd
from pandas import DataFrame
from ..column_preprocessor_basis import create_df_col_for_double_columns, handle_unnamed_columns, combine_column_names_2, COLUMN_NAME_FOR_HEADER_01

def get_df_preprocessed_column_menu2205(menu2205: DataFrame) -> DataFrame:
    return (
        menu2205
        .pipe(create_df_col_for_double_columns)
        .pipe(lambda df: handle_unnamed_columns(df=df, column=COLUMN_NAME_FOR_HEADER_01))
        .pipe(combine_column_names_2)
    )

def get_preprocessed_column_names_menu2205(menu2205: DataFrame) -> list[str]:
    df = get_df_preprocessed_column_menu2205(menu2205)
    return list(df.iloc[:,-1])
