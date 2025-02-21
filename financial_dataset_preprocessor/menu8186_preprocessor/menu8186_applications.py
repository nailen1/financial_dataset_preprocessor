from .menu8186 import get_preprocessed_menu8186_snapshot
from .menu8186_consts import COLUMN_NAMES_MENU8186_PREPROCESSED
from canonical_transformer import map_df_to_some_data, map_df_to_data

def get_data_of_columns_menu8186(cols, date_ref=None, option_sort=None, ascending=True):    
    menu8186_snapshot = get_preprocessed_menu8186_snapshot(date_ref=date_ref).reset_index()
    if option_sort:
        menu8186_snapshot = menu8186_snapshot.sort_values(by=cols[-1], ascending=ascending)
    data = map_df_to_some_data(menu8186_snapshot, cols)
    return data

def get_data_for_mapping_menu8186(col_for_range, col_for_domain='index', date_ref=None):   
    cols_domain_range = [col_for_domain, col_for_range]
    data = get_data_of_columns_menu8186(cols=cols_domain_range, date_ref=date_ref)
    return data

def get_mapping_menu8186(col_for_range, col_for_domain='index', date_ref=None):
    data = get_data_for_mapping_menu8186(col_for_range=col_for_range, col_for_domain=col_for_domain, date_ref=date_ref)
    mapping = {datum[col_for_domain]: datum[col_for_range] for datum in data}
    return mapping

def show_all_somethings_for_data_menu8186():
    data = COLUMN_NAMES_MENU8186_PREPROCESSED
    print('Show all somethings for get_all_something_of_fund_by_date(something=...)')
    print(data)
    return data

def get_mapping_fund_to_something_by_date(something, col_for_domain='index', date_ref=None):
    return get_mapping_menu8186(col_for_range=something, col_for_domain=col_for_domain, date_ref=date_ref)

def get_all_mappings_to_fund_by_date(date_ref=None):
    df_ref = get_preprocessed_menu8186_snapshot(date_ref)
    somethings = df_ref.columns.tolist()
    dct = {}
    for something in somethings[1:]:
        df = df_ref.loc[:, something].reset_index()
        data = map_df_to_data(df)
        mapping = {datum['index']: datum[something] for datum in data}
        dct[something] = mapping
    return dct

def get_all_fund_codes(date_ref=None):
    menu8186_snapshot = get_preprocessed_menu8186_snapshot(date_ref=date_ref)
    fund_codes = list(menu8186_snapshot.index.unique())
    return fund_codes

def get_all_fund_names(date_ref=None):
    return get_mapping_menu8186(col_for_range='펀드명', date_ref=date_ref)

def get_all_fund_prices(date_ref=None):
    return get_mapping_menu8186(col_for_range='수정기준가', date_ref=date_ref)

def get_all_fund_nav(date_ref=None):
    return get_mapping_menu8186(col_for_range='순자산', date_ref=date_ref)

def search_something_of_fund_by_date(something, fund_code, date_ref=None):
    return get_mapping_menu8186(col_for_range=something, date_ref=date_ref)[fund_code]

def search_nav_of_fund_by_date(fund_code, date_ref=None):
    return search_something_of_fund_by_date(something='순자산', fund_code=fund_code, date_ref=date_ref)

def search_price_of_fund_by_date(fund_code, date_ref=None):
    return search_something_of_fund_by_date(something='수정기준가', fund_code=fund_code, date_ref=date_ref)