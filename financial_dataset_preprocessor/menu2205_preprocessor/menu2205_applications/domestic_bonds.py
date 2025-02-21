from .applications import get_grouped_dfs_of_menu2205, get_grouped_dfs_of_menu2205_by_fund
from financial_dataset_preprocessor.menu8186_preprocessor.menu8186_applications import get_all_fund_codes
from tqdm import tqdm
from financial_dataset_preprocessor.menu2205_preprocessor.menu2205_consts import COLUMN_NAMES_MENU2205_PREPROCESSED

COLUMNS_FOR_DOMESTIC_BONDS = bond_specific_indices = [
    '자산',
    '종목명',
    '종목',
    '원화 보유정보: 수량',
    '원화 보유정보: 매매가능수량',
    '원화 보유정보: 장부가액',
    '원화 보유정보: 평가액',
    '원화 보유정보: 취득액',
    '원화 보유정보: 평가손익',
    '원화 보유정보: 손익률',
    '원화 보유정보: 미수이자',
    '원화 보유정보: 선급비용',
    '원화 보유정보: 상환손익',
    '평가정보: 종가',
    '평가정보: 시가수익률',
    '평가정보: 3사평균',
    '평가정보: 4사평균',
    '평가정보: KBP가격',
    '평가정보: NICE가격', 
    '평가정보: KIS가격',
    '평가정보: FNP가격',
    '평가정보: 3사평균YTM',
    '평가정보: 4사평균YTM',
    '평가정보: KBP YTM',
    '평가정보: NICE YTM',
    '평가정보: KIS YTM',
    '평가정보: FNP YTM',
    '종목정보: 표면금리',
    '종목정보: 할인율',
    '종목정보: 매입수익률',
    '종목정보: 회계적수익률',
    '종목정보: 발행일',
    '종목정보: 만기일',
    '종목정보: 편입일',
    '종목정보: 듀레이션',
    '종목정보: 컨벡시티',
    '종목정보: KBP듀레이션',
    '종목정보: KBP컨벡시티',
    '종목정보: KIS듀레이션',
    '종목정보: KIS컨벡시티',
    '종목정보: NICE듀레이션',
    '종목정보: NICE컨벡시티',
    '종목정보: FNP듀레이션',
    '종목정보: FNP컨벡시티',
    '종목정보: 신용등급',
    '종목정보: 잔존일수',
    '종목정보: 발행기관',
    '종목정보: 이자지급방법',
    '종목정보: 자산분류'
]

MAPPING_RENAME = {
    '원화 보유정보: 수량': '원화 보유정보: 액면금액',
    '원화 보유정보: 매매가능수량': '원화 보유정보: 매매가능액면금액',
}

def get_domestic_bonds(date_ref=None):
    dfs = get_grouped_dfs_of_menu2205(col='자산', date_ref=date_ref)
    domestic_bonds = dfs['국내채권'][COLUMNS_FOR_DOMESTIC_BONDS]
    domestic_bonds = domestic_bonds.rename(columns=MAPPING_RENAME)
    return domestic_bonds

def get_domestic_bonds_by_fund(fund_code, date_ref=None):
    dfs = get_grouped_dfs_of_menu2205_by_fund(fund_code=fund_code, col='자산', date_ref=date_ref)
    domestic_bonds = dfs['국내채권'][COLUMNS_FOR_DOMESTIC_BONDS]
    domestic_bonds = domestic_bonds.rename(columns=MAPPING_RENAME)
    return domestic_bonds

def search_funds_having_domestic_bonds(date_ref=None, option_exist_data=True):
    fund_codes = get_all_fund_codes()
    dct_dfs = {}
    for fund_code in tqdm(fund_codes):
        try:
            dct_dfs[fund_code] = get_domestic_bonds_by_fund(fund_code=fund_code, date_ref=date_ref)
        except:
            dct_dfs[fund_code] = None
    dct_bonds = {fund_code: df for fund_code, df in dct_dfs.items() if df is not None} if option_exist_data else dct_dfs
    return dct_bonds
