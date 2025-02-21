from .applications import get_grouped_dfs_of_menu2205, get_grouped_dfs_of_menu2205_by_fund
from financial_dataset_preprocessor.menu8186_preprocessor.menu8186_applications import get_all_fund_codes
from tqdm import tqdm

COLUMNS_FOR_BORROWINGS = [
    '자산',
    '종목명',
    '종목',
    '원화 보유정보: 장부가액',
    '원화 보유정보: 평가액',
    '원화 보유정보: 취득액',
    '원화 보유정보: 미수이자',
    '종목정보: 표면금리',
    '종목정보: 회계적수익률',
    '종목정보: 발행일',
    '종목정보: 만기일',
    '종목정보: 잔존일수',
    '종목정보: 발행기관',
    '종목정보: 만기일'
]

def get_borriwings(date_ref=None):
    dfs = get_grouped_dfs_of_menu2205(col='자산', date_ref=date_ref)
    borrowings = dfs['차입금'][COLUMNS_FOR_BORROWINGS]
    return borrowings

def get_borriwings_by_fund(fund_code, date_ref=None):
    dfs = get_grouped_dfs_of_menu2205_by_fund(fund_code=fund_code, col='자산', date_ref=date_ref)
    borrowings = dfs['차입금'][COLUMNS_FOR_BORROWINGS]
    return borrowings

def search_funds_having_borrowings(date_ref=None, option_exist_data=True):
    fund_codes = get_all_fund_codes()
    dct_dfs = {}
    for fund_code in tqdm(fund_codes):
        try:
            dct_dfs[fund_code] = get_borriwings_by_fund(fund_code=fund_code, date_ref=date_ref)
        except:
            dct_dfs[fund_code] = None
    dct_borrowings = {fund_code: df for fund_code, df in dct_dfs.items() if df is not None} if option_exist_data else dct_dfs
    return dct_borrowings