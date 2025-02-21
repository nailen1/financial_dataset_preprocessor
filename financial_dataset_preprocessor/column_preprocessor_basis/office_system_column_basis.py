# basis functions

import pandas as pd
from pandas import DataFrame
from typing import Dict, List
from .office_system_column_consts import (
    COLUMN_NAME_FOR_HEADER_01,
    COLUMN_NAME_FOR_HEADER_02,
    COLUMN_NAME_FOR_RETURN,
    COLUMN_NAME_TOBE_ELIMINATED,
    CHARACTER_TOBE_REPLACED,
    CHARACTER_TOBE_SPLITTED,
)


def get_data_of_double_columns_in_raw_csv_dataset(df: DataFrame) -> Dict[str, List[str]]:
    return {
        COLUMN_NAME_FOR_HEADER_01: list(df.columns),
        COLUMN_NAME_FOR_HEADER_02: list(df.iloc[0])
    }


def get_data_of_single_column_in_raw_csv_dataset(df): 
    return {
        COLUMN_NAME_FOR_HEADER_01: list(df.columns),
        COLUMN_NAME_FOR_HEADER_02: None
    }

def create_df_col_for_double_columns(df: DataFrame) -> DataFrame:
    return pd.DataFrame(data=get_data_of_double_columns_in_raw_csv_dataset(df))

def create_df_col_for_single_columns(df: DataFrame) -> DataFrame:
    return pd.DataFrame(data=get_data_of_single_column_in_raw_csv_dataset(df))

def clean_column(df: DataFrame, column: str) -> DataFrame:
    return df.assign(
        column=df[column].apply(lambda x: x.replace(CHARACTER_TOBE_REPLACED,'').split(CHARACTER_TOBE_SPLITTED)[0])
                           .apply(lambda x: None if COLUMN_NAME_TOBE_ELIMINATED in x else x)
    )

def clean_col1(df: DataFrame) -> DataFrame:
    return df.assign(
        col1=df[COLUMN_NAME_FOR_HEADER_01].apply(lambda x: x.replace(CHARACTER_TOBE_REPLACED,'').split(CHARACTER_TOBE_SPLITTED)[0])
                           .apply(lambda x: None if COLUMN_NAME_TOBE_ELIMINATED in x else x)
    )

def clean_col2(df: DataFrame) -> DataFrame:
    return df.assign(
        col2=df[COLUMN_NAME_FOR_HEADER_02].apply(lambda x: x.replace(CHARACTER_TOBE_REPLACED,'').split(CHARACTER_TOBE_SPLITTED)[0])
                           .apply(lambda x: None if COLUMN_NAME_TOBE_ELIMINATED in x else x)
    )

def process_return_column_from_col1_to_col2(df: DataFrame) -> DataFrame:
    return df.assign(
        col2=df.apply(lambda x: x[COLUMN_NAME_FOR_HEADER_01] if x[COLUMN_NAME_FOR_HEADER_01]==COLUMN_NAME_FOR_RETURN else x[COLUMN_NAME_FOR_HEADER_02], axis=1)
           .apply(lambda x: '' if pd.isna(x) else x)
    )

def fill_col1_values(df: DataFrame) -> DataFrame:
    return df.assign(
        col1=df[COLUMN_NAME_FOR_HEADER_01].apply(lambda x: None if x==COLUMN_NAME_FOR_RETURN else x).ffill()
    )

def handle_unnamed_columns(df: DataFrame, column: str) -> DataFrame:
    return df.assign(**{
        column: df[column].apply(lambda x: None if 'Unnamed:' in str(x) else x).ffill()
    })

def handle_empty_column(df: DataFrame, column: str) -> DataFrame:
    return df.assign(**{
        column: df[column].apply(lambda x: None if pd.isna(x) else x)
    })

def handle_empty_col1(df: DataFrame) -> DataFrame:
    return handle_empty_column(df=df, column=COLUMN_NAME_FOR_HEADER_01)

def handle_empty_col2(df: DataFrame) -> DataFrame:
    return handle_empty_column(df=df, column=COLUMN_NAME_FOR_HEADER_02)

def combine_column_names(df: DataFrame, col_prefix: str, col_suffix: str) -> DataFrame:
    return df.assign(
        col=df.apply(
            lambda x: f"{x[col_prefix]}: {x[col_suffix]}" if x[col_prefix] != None else x[col_suffix],
            axis=1
        )
    )

def combine_column_names_1(df):
    return df.assign(
        col=df.apply(lambda x: f"{x[COLUMN_NAME_FOR_HEADER_01]}: {x[COLUMN_NAME_FOR_HEADER_02]}" if x[COLUMN_NAME_FOR_HEADER_02] else x[COLUMN_NAME_FOR_HEADER_01], axis=1)
    ) 

def combine_column_names_2(df):
    return df.assign(
        col=df.apply(lambda x: f"{x[COLUMN_NAME_FOR_HEADER_01]}: {x[COLUMN_NAME_FOR_HEADER_02]}" if x[COLUMN_NAME_FOR_HEADER_01] else x[COLUMN_NAME_FOR_HEADER_02], axis=1)
    ) 

def attach_col1_to_col2(df):
    col_prefix = COLUMN_NAME_FOR_HEADER_01
    col_suffix = COLUMN_NAME_FOR_HEADER_02
    return combine_column_names(df=df, col_prefix=col_prefix, col_suffix=col_suffix)

def attach_col2_to_col1(df):
    col_prefix = COLUMN_NAME_FOR_HEADER_02
    col_suffix = COLUMN_NAME_FOR_HEADER_01
    return combine_column_names(df=df, col_prefix=col_prefix, col_suffix=col_suffix)

def remove_index_name(df: DataFrame) -> DataFrame:
   return df.rename_axis(None)

def drop_first_row(df: DataFrame) -> DataFrame:
   return df.iloc[1:]

def set_col_as_index(df: DataFrame, col: str) -> DataFrame:
    return df.set_index(col)