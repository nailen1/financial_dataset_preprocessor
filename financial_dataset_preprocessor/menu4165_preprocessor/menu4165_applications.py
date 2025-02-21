from .menu4165 import get_preprocessed_menu4165_snapshot
from financial_dataset_preprocessor.universal_applications import get_grouped_dfs_of_df

def get_attributions_and_exposures_in_menu4165(fund_code, date_ref=None):
    menu4165 = get_preprocessed_menu4165_snapshot(fund_code=fund_code, date_ref=date_ref)
    dfs = get_grouped_dfs_of_df(df=menu4165, col='자산구분')
    df = dfs['주식']
    cols_to_keep = ['종목', '종목명', '기여도(%): 합계', '순자산편입비']
    df = df[cols_to_keep]
    return df