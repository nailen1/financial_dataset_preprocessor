from typing import Dict, List
from pandas import DataFrame
from ..menu2205 import get_preprocessed_menu2205_snapshot, get_preprocessed_menu2205
from financial_dataset_preprocessor.general_preprocess_utils import map_ticker_to_ticker_bbg

COLUMN_NAMES_FOR_MATCHING_CORPNAME =['자산', '종목명', '종목정보: 발행기관']

MAPPING_NAMES_TO_CORPNAMES_FOR_EXCEPTIONS = {
    '그래피2우선주(전환상환)': '그래피',
    '차바이오텍3우선주': '차바이오텍',
    '두나무(주)': '두나무',
    '윈텍글로비스보통주': '윈텍글로비스',
    '에버베스트헬리오스파워PEF(241211)': '일렉트로엠',
    '메를로랩 보통주': '메를로랩',
    '규원테크 1우선주 240708 (002)': '규원테크',
    '글라세움 4우선주 221014 (002)': '글라세움',
    '이피캠텍 주식회사 보통주': '이피캠텍',
    '비브로스 보통주': '비브로스',
}

MAPPING_ISSUERS_TO_CORPNAMES_FOR_EXCEPTIONS = {
    '브리즈에어일차 주식회사': '브리즈에어일차',
    '(주)농심캐피탈': '농심캐피탈',
    'STX 그린 로지스': 'STX그린로지스',
    '케이비카드': 'KB금융',
}


def filter_by_conditions(df: DataFrame) -> DataFrame:
   return df[
       (~df['종목정보: 발행기관'].isna()) &
       (df['자산'].str.contains('국내주식|국내채권'))
   ]

def set_bbg_ticker_as_index(df: DataFrame) -> DataFrame:
   df.index = df.apply(
       lambda row: map_ticker_to_ticker_bbg(row['종목'][3:-3]) 
       if row['자산']=='국내주식' else None, 
       axis=1
   )
   return df

def apply_hotfix_mapping(df: DataFrame) -> DataFrame:
   df = df.assign(hotfix=None)
   
   for name, value in MAPPING_NAMES_TO_CORPNAMES_FOR_EXCEPTIONS.items():
       df.loc[df['종목명']==name, 'hotfix'] = value
   for issuer, value in MAPPING_ISSUERS_TO_CORPNAMES_FOR_EXCEPTIONS.items():
       df.loc[df['종목정보: 발행기관']==issuer, 'hotfix'] = value
       
   return df

def get_df_holdings_corpname(date_ref=None) -> DataFrame:
   return (
       get_preprocessed_menu2205_snapshot(date_ref)
       .pipe(filter_by_conditions)
       .pipe(set_bbg_ticker_as_index)
       .loc[:, COLUMN_NAMES_FOR_MATCHING_CORPNAME]
       .pipe(apply_hotfix_mapping)
   )

def get_df_fund_holdings_corpname(fund_code,date_ref=None) -> DataFrame:
   return (
       get_preprocessed_menu2205(fund_code, date_ref)
       .pipe(filter_by_conditions)
       .pipe(set_bbg_ticker_as_index)
       .loc[:, COLUMN_NAMES_FOR_MATCHING_CORPNAME]
       .pipe(apply_hotfix_mapping)
   )