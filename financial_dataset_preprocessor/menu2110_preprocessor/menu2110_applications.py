from .menu2110 import get_preprocessed_menu2110
from financial_dataset_preprocessor.universal_applications import get_grouped_dfs_of_df
from canonical_transformer import map_df_to_some_data
import pandas as pd


def get_data_of_columns_menu2110(cols):    
    menu2110_snapshot = get_preprocessed_menu2110().reset_index().rename(columns={'index': '펀드코드'})
    data = map_df_to_some_data(menu2110_snapshot, cols)
    return data

def get_data_for_mapping_menu2110(col_for_range, col_for_domain='펀드코드'):   
    cols_domain_range = [col_for_domain, col_for_range]
    data = get_data_of_columns_menu2110(cols_domain_range)
    return data

def get_mapping_menu2110(col_for_range, col_for_domain='펀드코드'):
    data = get_data_for_mapping_menu2110(col_for_range=col_for_range, col_for_domain=col_for_domain)
    mapping = {datum[col_for_domain]: datum[col_for_range] for datum in data}
    return mapping

def get_mapping_fund_class():
    return get_mapping_menu2110(col_for_range='클래스구분', col_for_domain='펀드코드')

def get_data_of_fund_type_and_class():
    data = get_data_of_columns_menu2110(cols=['펀드코드', '펀드명', '펀드분류', '클래스구분', '클래스'])
    return data

def get_df_fund_class_sorted(date_ref=None):
    df = get_preprocessed_menu2110(date_ref=date_ref)
    df['클래스구분'] = df['클래스구분'].fillna('-')
    cols_to_keep = ['펀드명', '클래스구분']
    df = df[cols_to_keep]

    custom_order = ['운용펀드', '-', '일반', '클래스펀드']
    df['클래스구분'] = pd.Categorical(df['클래스구분'], 
                            categories=custom_order, 
                            ordered=True)

    df_sorted = df.sort_values('클래스구분')
    return df_sorted

def get_df_by_class(class_name, date_ref=None):
    df = get_preprocessed_menu2110(date_ref=date_ref)
    grouped_dfs = get_grouped_dfs_of_df(df=df, col='클래스구분')
    df = grouped_dfs[class_name]
    return df

def get_fund_codes_by_class_name(class_name, date_ref=None):
    df = get_df_by_class(class_name, date_ref=date_ref)
    return list(df.index)

def get_fund_codes_mothers(date_ref=None):
    fund_codes_managing = get_fund_codes_by_class_name(class_name='운용펀드', date_ref=date_ref)
    fund_codes_nonclassified = get_fund_codes_by_class_name(class_name='-', date_ref=date_ref)
    fund_codes = fund_codes_managing + fund_codes_nonclassified
    return fund_codes

def get_fund_codes_general(date_ref=None):
    fund_codes = get_fund_codes_by_class_name(class_name='일반', date_ref=date_ref)
    return fund_codes

def get_fund_codes_class(date_ref=None):
    fund_codes = get_fund_codes_by_class_name(class_name='클래스펀드', date_ref=date_ref)
    return fund_codes

def get_fund_codes_main(date_ref=None):
    df = get_df_fund_class_sorted(date_ref=date_ref)
    df = df[df['클래스구분']!='클래스펀드']
    fund_codes = list(df.index)
    return fund_codes

def get_preprocessed_funds_main(date_ref=None):
    menu2110 = get_preprocessed_menu2110(date_ref=date_ref)
    df = menu2110[menu2110['클래스구분']!='클래스펀드']
    return df

def get_dfs_by_fund_type(date_ref=None):
    df = get_preprocessed_menu2110(date_ref=date_ref)
    return dict(tuple(df.groupby('펀드분류')))

FUND_TYPES = ['변액', '주식형', '주식혼합', '채권혼합', '혼합자산']

def get_preprocessed_funds_by_fund_type(fund_type, date_ref=None):
    df = get_dfs_by_fund_type(date_ref=date_ref)[fund_type]
    return df

def get_preprocessed_funds_variable_type(date_ref=None):
    df = get_dfs_by_fund_type(date_ref=date_ref)['변액']
    return df

def get_preprocessed_funds_equity_type(date_ref=None):
    df = get_dfs_by_fund_type(date_ref=date_ref)['주식형']
    return df

def get_preprocessed_funds_equity_mixed_type(date_ref=None):
    df = get_dfs_by_fund_type(date_ref=date_ref)['주식혼합']
    return df

def get_preprocessed_funds_bond_mixed_type(date_ref=None):
    df = get_dfs_by_fund_type(date_ref=date_ref)['채권혼합']
    return df

def get_preprocessed_funds_multi_asset_type(date_ref=None):
    df = get_dfs_by_fund_type(date_ref=date_ref)['혼합자산']
    return df

def filter_df_by_fund_codes_main(df, date_ref=None):
    fund_codes_main = get_fund_codes_main(date_ref=date_ref)
    df = df[df.index.isin(fund_codes_main)]
    return df