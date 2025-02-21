from financial_dataset_preprocessor.menu2205_preprocessor.menu2205_consts import COLUMN_NAMES_MENU2205_PREPROCESSED
from .applications import get_grouped_dfs_of_menu2205, get_grouped_dfs_of_menu2205_by_fund
from financial_dataset_preprocessor.menu8186_preprocessor.menu8186_applications import get_all_fund_codes
from tqdm import tqdm

COLUMNS_FOR_GENERAL_LEDGER = COLUMN_NAMES_MENU2205_PREPROCESSED

def get_general_ledger(date_ref=None):
    """총계정원장 데이터를 가져오는 함수"""
    dfs = get_grouped_dfs_of_menu2205(col='자산', date_ref=date_ref)
    general_ledger = dfs['총계정원장'][COLUMNS_FOR_GENERAL_LEDGER]
    return general_ledger

def get_general_ledger_by_fund(fund_code, date_ref=None):
    """특정 펀드의 총계정원장 데이터를 가져오는 함수"""
    dfs = get_grouped_dfs_of_menu2205_by_fund(fund_code=fund_code, col='자산', date_ref=date_ref)
    general_ledger = dfs['총계정원장'][COLUMNS_FOR_GENERAL_LEDGER]
    return general_ledger

def search_funds_having_general_ledger(date_ref=None, option_exist_data=True):
    """총계정원장 데이터를 보유한 펀드를 검색하는 함수"""
    fund_codes = get_all_fund_codes()
    dct_dfs = {}
    for fund_code in tqdm(fund_codes):
        try:
            dct_dfs[fund_code] = get_general_ledger_by_fund(fund_code=fund_code, date_ref=date_ref)
        except:
            dct_dfs[fund_code] = None
    dct_general_ledger = {fund_code: df for fund_code, df in dct_dfs.items() if df is not None} if option_exist_data else dct_dfs
    return dct_general_ledger
