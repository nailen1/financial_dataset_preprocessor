from ..menu2205_consts import ASSET_CATEGORIES
from ..menu2205 import get_preprocessed_menu2205, get_preprocessed_menu2205_snapshot
from ..menu2205_exceptions import MAPPING_NAMES_TO_CORPNAMES_FOR_EXCEPTIONS, MAPPING_CORPNAMES_TO_CORPNAMES_FOR_EXCEPTIONS
from financial_dataset_preprocessor.universal_applications import get_grouped_dfs_of_df

def get_df_asset_menu2205_snapshot(date_ref=None):
    menu2205 = get_preprocessed_menu2205_snapshot(date_ref=date_ref)
    dfs = dict(tuple(menu2205.groupby('자산')))
    return dfs

def get_df_asset_menu2205(fund_code, date_ref=None):
    menu2205 = get_preprocessed_menu2205(fund_code=fund_code, date_ref=date_ref)
    dfs = dict(tuple(menu2205.groupby('자산')))
    return dfs

def get_df_stock_snapshot(date_ref=None):
    df = get_df_asset_menu2205_snapshot(date_ref=date_ref)[ASSET_CATEGORIES[0]]
    df = df.reset_index(drop=True)
    return df

def get_df_stock(fund_code, date_ref=None):
    df = get_df_asset_menu2205(fund_code=fund_code, date_ref=date_ref)[ASSET_CATEGORIES[0]]
    df = df.reset_index(drop=True)
    return df

def get_df_bond_snapshot(date_ref=None):
    df = get_df_asset_menu2205_snapshot(date_ref=date_ref)[ASSET_CATEGORIES[1]]
    df = df.reset_index(drop=True)
    return df

def get_df_bond(fund_code, date_ref=None):
    df = get_df_asset_menu2205(fund_code=fund_code, date_ref=date_ref)[ASSET_CATEGORIES[1]]
    df = df.reset_index(drop=True)
    return df

def get_mapping_tickers_to_names():
    stocks = get_df_stock_snapshot().iloc[:-1]
    stocks['ticker'] = stocks['종목'].apply(lambda x: x[3:-3])
    cols_to_keep = ['ticker', '종목명']
    stocks = stocks[cols_to_keep].rename(columns={'종목명': 'name'})
    mapping_tickers_to_names = stocks.set_index('ticker').to_dict()['name']
    return mapping_tickers_to_names

def get_mapping_names_to_corpnames():
    stocks = get_df_stock_snapshot().iloc[:-1]
    cols_to_keep = ['종목명', '종목정보: 발행기관',]
    stocks = stocks[cols_to_keep].rename(columns={'종목명': 'name', '종목정보: 발행기관': 'corpname'})
    mapping_names_to_corpnames = stocks.set_index('name').to_dict()['corpname']
    return mapping_names_to_corpnames

def get_df_ticker_name_corpname_for_stocks(date_ref=None, exceptions=True):
    df = get_df_stock_snapshot(date_ref=date_ref).iloc[:-1]
    df['ticker'] = df['종목'].apply(lambda x: x[3:-3])
    cols_to_keep = ['ticker', '종목명', '종목정보: 발행기관']
    df = df[cols_to_keep].rename(columns={'종목명': 'name', '종목정보: 발행기관': 'corpname'})
    if exceptions:
        df = apply_name_exceptions_to_df_ticker_name_corpname(df)
    return df

def get_df_ticker_name_corpname_for_bonds(date_ref=None, exceptions=True):
    df = get_df_bond_snapshot(date_ref=date_ref).iloc[:-1]
    df['ticker'] = df['종목'].apply(lambda x: x[3:-3])
    cols_to_keep = ['ticker', '종목명', '종목정보: 발행기관']
    df = df[cols_to_keep].rename(columns={'종목명': 'name', '종목정보: 발행기관': 'corpname'})
    if exceptions:
        df = apply_name_exceptions_to_df_ticker_name_corpname(df)
        df = apply_corpname_exceptions_to_df_ticker_name_corpname(df)
    return df

def apply_name_exceptions_to_df_ticker_name_corpname(df):
    for name, corpname in MAPPING_NAMES_TO_CORPNAMES_FOR_EXCEPTIONS.items():
        df.loc[df['name']==name, 'hotfix'] = corpname
    return df

def apply_corpname_exceptions_to_df_ticker_name_corpname(df):
    for corpname, hotfix_corpname in MAPPING_CORPNAMES_TO_CORPNAMES_FOR_EXCEPTIONS.items():
        df.loc[df['corpname']==corpname, 'hotfix'] = hotfix_corpname
    return df

def show_all_categories_of_assets():
    print('All categories of assets:')
    print(ASSET_CATEGORIES)
    return ASSET_CATEGORIES

def get_grouped_dfs_of_menu2205(col, date_ref=None):
    df = get_preprocessed_menu2205_snapshot(date_ref=date_ref)
    dfs = get_grouped_dfs_of_df(df=df, col=col)
    return dfs

def get_grouped_dfs_of_menu2205_by_fund(fund_code, col, date_ref=None):
    df = get_preprocessed_menu2205(fund_code=fund_code, date_ref=date_ref)
    dfs = get_grouped_dfs_of_df(df=df, col=col)
    return dfs


# ['국내주식', '국내채권', 'REPO 매수', 'REPO', '국내현금', '국내선물', '국내수익증권',
#        '국내수익증권(ETF)', '외화주식', '외화현금성', '외화스왑', '기타', '기타(총계정원장)', '총계정원장',
#        '차입금']

def search_assets_by_keyword(keyword, date_ref=None):
    df = get_preprocessed_menu2205_snapshot(date_ref=date_ref)
    df = df[df['종목명'].str.contains(keyword)]
    return df

def search_assets_by_keyword_in_fund(keyword, fund_code, date_ref=None):
    df = get_preprocessed_menu2205(fund_code=fund_code, date_ref=date_ref)
    df = df[df['종목명'].str.contains(keyword)]
    return df

def search_assets_including_keywords(keywords, date_ref=None):
    df = get_preprocessed_menu2205_snapshot(date_ref=date_ref)
    reg_keywords = '|'.join(keywords)
    df = df[df['종목명'].str.contains(reg_keywords)]
    return df

def search_assets_including_keywords_in_fund(keywords, fund_code, date_ref=None):
    df = get_preprocessed_menu2205(fund_code=fund_code, date_ref=date_ref)
    reg_keywords = '|'.join(keywords)
    df = df[df['종목명'].str.contains(reg_keywords)]
    return df