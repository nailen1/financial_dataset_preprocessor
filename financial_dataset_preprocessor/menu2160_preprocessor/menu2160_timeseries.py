from .menu2160 import get_preprocessed_menu2160, preprocess_raw_menu2160
from .menu2160_consts import COLUMN_MAPPING_FOR_PRICE, INDEX_NAME_FOR_DATE, INITIAL_PRICE_DEFAULT
from string_date_controller import get_date_n_days_ago


def select_column_for_timeseries_menu2160(df):
    return df[list(COLUMN_MAPPING_FOR_PRICE.keys())].rename(columns=COLUMN_MAPPING_FOR_PRICE)

def inject_initial_adjusted_price_in_zeroth_row(df, price_zeroth_row=INITIAL_PRICE_DEFAULT):
    dates = df.index.dropna()
    date_first = dates[0]
    date_zeroth = get_date_n_days_ago(date_first, 1)
    df.loc[date_zeroth, df.columns[0]] = price_zeroth_row
    df = df.sort_index(ascending=True)
    return df

def preprocess_timeseries_menu2160(menu2160_preprocessed):
    df = (menu2160_preprocessed.copy()
          .pipe(select_column_for_timeseries_menu2160)
          .rename_axis(index=INDEX_NAME_FOR_DATE)
          .pipe(lambda df: inject_initial_adjusted_price_in_zeroth_row(df)))
    return df

def preprocess_timeseries_for_raw_menu2160(menu2160):
    return preprocess_timeseries_menu2160(preprocess_raw_menu2160(menu2160))

def get_timeseries_fund_price(fund_code, option_col_name=True):
    menu2160_preprocessed = get_preprocessed_menu2160(fund_code=fund_code)
    timeseries = preprocess_timeseries_menu2160(menu2160_preprocessed)
    if option_col_name:
        timeseries.columns = [fund_code]
    return timeseries
