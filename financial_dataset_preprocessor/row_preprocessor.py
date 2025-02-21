import pandas as pd
from pandas import DataFrame

def drop_non_indexed_rows(df):
    df = df[pd.notna(df.index)]
    return df
