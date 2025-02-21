from .menu3412 import get_preprocessed_menu3412
from pandas import DataFrame

def get_preprocessed_menu3412_nonan(date_ref=None) -> DataFrame:
    df = get_preprocessed_menu3412(date_ref=date_ref)
    df_nonan = df.dropna(axis=1, how='all')
    return df_nonan
