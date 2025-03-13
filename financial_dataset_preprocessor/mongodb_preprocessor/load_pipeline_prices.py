from mongodb_controller import client
from .general_utils import aggregate_pipeline_in_collection, map_results_to_df_raw

DB = client['database-rpa']
COLLECTION = DB['dataset-menu8186']

PIPELINE_FOR_PRICES = [
    {
        "$project": {
            "_id": 0,
            "일자": 1,
            "펀드코드": 1,
            "수정기준가": 1
        }
    },
    {
        "$sort": {
            "일자": 1,
            "펀드코드": 1
        }
    }
]

def get_results_of_pipeline_for_prices():
    return aggregate_pipeline_in_collection(collection=COLLECTION, pipeline=PIPELINE_FOR_PRICES)

def load_raw_prices():
    return map_results_to_df_raw(get_results_of_pipeline_for_prices())

def map_df_raw_to_df_prices(df):
    return df.pivot(index='일자', columns='펀드코드', values='수정기준가')

def map_df_prices_to_df_fund(df, fund_code):
    return df[[fund_code]].dropna()

def load_fund_prices_from_mongodb():
    df = load_raw_prices()
    df_fund_prices = map_df_raw_to_df_prices(df)
    return df_fund_prices

def load_fund_price_from_mongodb(fund_code):
    df = load_raw_prices()
    df_fund_price = map_df_prices_to_df_fund(df, fund_code)
    return df_fund_price

