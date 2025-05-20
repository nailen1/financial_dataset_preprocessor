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

def create_column_name_for_duplicated_delta(df_columns, index):
    prefix_ref, suffix_ref = df_columns.iloc[index-1, -1].split(': ')
    _, suffix = df_columns.iloc[index, -1].split(': ')
    column_name = f'{prefix_ref}: {suffix_ref}{suffix}'
    return column_name

def insert_column_names_for_duplicated_delta(df_columns):
    indices = df_columns[df_columns['col'].str.contains('평가정보: 증감')].index
    for index in indices:
        df_columns.iloc[index, -1] = create_column_name_for_duplicated_delta(df_columns, index)
    return df_columns

def get_df_preprocessed_column_menu2206(menu2206: DataFrame) -> DataFrame:
    return (
        menu2206
        .pipe(create_df_col_for_double_columns)
        .pipe(lambda df: handle_unnamed_columns(df=df, column=COLUMN_NAME_FOR_HEADER_01))
        .pipe(replace_old_column_with_new_column)
        .pipe(combine_column_names_2)
        .pipe(insert_column_names_for_duplicated_delta)
    )

def get_preprocessed_column_names_menu2206(menu2206: DataFrame) -> list[str]:
    df = get_df_preprocessed_column_menu2206(menu2206)
    return list(df.iloc[:,-1])
