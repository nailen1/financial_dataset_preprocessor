from .applications import get_grouped_dfs_of_menu2205, get_grouped_dfs_of_menu2205_by_fund
from ..menu2205_consts import COLUMN_NAMES_MENU2205_PREPROCESSED
from financial_dataset_preprocessor.menu8186_preprocessor.menu8186_applications import get_all_fund_codes
from tqdm import tqdm

COLUMNS_FOR_DOMESTIC_STOCKS = COLUMN_NAMES_MENU2205_PREPROCESSED

def get_domestic_stocks(date_ref=None):
    dfs = get_grouped_dfs_of_menu2205(col='자산', date_ref=date_ref)
    domestic_stocks = dfs['국내주식'][COLUMNS_FOR_DOMESTIC_STOCKS]
    return domestic_stocks

def get_domestic_stocks_by_fund(fund_code, date_ref=None):
    dfs = get_grouped_dfs_of_menu2205_by_fund(fund_code=fund_code, col='자산', date_ref=date_ref)
    domestic_stocks = dfs['국내주식'][COLUMNS_FOR_DOMESTIC_STOCKS]
    return domestic_stocks

def search_funds_having_domestic_stocks(date_ref=None, option_exist_data=True):
    fund_codes = get_all_fund_codes()
    dct_dfs = {}
    for fund_code in tqdm(fund_codes):
        try:
            dct_dfs[fund_code] = get_domestic_stocks_by_fund(fund_code=fund_code, date_ref=date_ref)
        except:
            dct_dfs[fund_code] = None
    dct_domestic_stocks = {fund_code: df for fund_code, df in dct_dfs.items() if df is not None} if option_exist_data else dct_dfs
    return dct_domestic_stocks