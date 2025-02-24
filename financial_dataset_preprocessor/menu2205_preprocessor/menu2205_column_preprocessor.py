import pandas as pd
from pandas import DataFrame
from ..column_preprocessor_basis import create_df_col_for_double_columns, handle_unnamed_columns, combine_column_names_2, COLUMN_NAME_FOR_HEADER_01


def replace_old_column_with_new_column(df: DataFrame) -> DataFrame:
    # 2024-12-31 이전 칼럼명의 hotfix
    if 'col2' not in df.columns:
        raise ValueError("Column 'col2' not found in DataFrame")
        
    return df.assign(
        col2=df['col2'].str.replace('미수/미지급이자', '미수이자', regex=False)
    )

def get_df_preprocessed_column_menu2205(menu2205: DataFrame) -> DataFrame:
    return (
        menu2205
        .pipe(create_df_col_for_double_columns)
        .pipe(lambda df: handle_unnamed_columns(df=df, column=COLUMN_NAME_FOR_HEADER_01))
        .pipe(replace_old_column_with_new_column)
        .pipe(combine_column_names_2)
    )


def get_preprocessed_column_names_menu2205(menu2205: DataFrame) -> list[str]:
    df = get_df_preprocessed_column_menu2205(menu2205)
    return list(df.iloc[:,-1])
