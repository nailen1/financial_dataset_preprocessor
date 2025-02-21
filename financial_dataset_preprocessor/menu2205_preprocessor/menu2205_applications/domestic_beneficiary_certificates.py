from .applications import get_grouped_dfs_of_menu2205, get_grouped_dfs_of_menu2205_by_fund
from financial_dataset_preprocessor.menu8186_preprocessor.menu8186_applications import get_all_fund_codes
from tqdm import tqdm
from financial_dataset_preprocessor.menu2205_preprocessor.menu2205_consts import COLUMN_NAMES_MENU2205_PREPROCESSED

COLUMNS_FOR_DOMESTIC_BENEFICIARY_CERTIFICATES = COLUMN_NAMES_MENU2205_PREPROCESSED

def get_domestic_beneficiary_certificates(date_ref=None):
    dfs = get_grouped_dfs_of_menu2205(col='자산', date_ref=date_ref)
    domestic_beneficiary_certificates = dfs['국내수익증권'][COLUMNS_FOR_DOMESTIC_BENEFICIARY_CERTIFICATES]
    return domestic_beneficiary_certificates

def get_domestic_beneficiary_certificates_by_fund(fund_code, date_ref=None):
    dfs = get_grouped_dfs_of_menu2205_by_fund(fund_code=fund_code, col='자산', date_ref=date_ref)
    domestic_beneficiary_certificates = dfs['국내수익증권'][COLUMNS_FOR_DOMESTIC_BENEFICIARY_CERTIFICATES]
    return domestic_beneficiary_certificates

def search_funds_having_domestic_beneficiary_certificates(date_ref=None, option_exist_data=True):
    fund_codes = get_all_fund_codes()
    dct_dfs = {}
    for fund_code in tqdm(fund_codes):
        try:
            dct_dfs[fund_code] = get_domestic_beneficiary_certificates_by_fund(fund_code=fund_code, date_ref=date_ref)
        except:
            dct_dfs[fund_code] = None
    dct_domestic_beneficiary_certificates = {fund_code: df for fund_code, df in dct_dfs.items() if df is not None} if option_exist_data else dct_dfs
    return dct_domestic_beneficiary_certificates
