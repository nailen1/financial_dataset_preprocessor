from .menu3233 import get_preprocessed_menu3233
from canonical_transformer import map_df_to_data

fund_code = '100005'

def get_data_menu3233_by_fund_code(fund_code, date_ref=None):
    df = get_preprocessed_menu3233(fund_code=fund_code, date_ref=date_ref)
    data = map_df_to_data(df[df['펀드코드']==fund_code])
    dct = {'fund_code': fund_code, 'data': data}
    return dct