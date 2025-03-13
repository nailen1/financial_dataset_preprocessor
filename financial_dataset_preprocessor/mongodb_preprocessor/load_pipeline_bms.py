from mongodb_controller import client
from .general_utils import aggregate_pipeline_in_collection, map_results_to_df_raw

DB = client['database-rpa']
COLLECTION = DB['dataset-menu8186']

PIPELINE_FOR_BMS = [
     {
        "$match": {
            "펀드코드": "100004"
        }
    },
    {
        "$project": {
            "_id": 0,
            "일자": 1,
            "KOSPI지수": 1,
            "KOSPI200지수": 1,
            "KOSDAQ지수": 1
        }
    },
    {
        "$sort": {
            "일자": 1
        }
    }
]

def get_results_of_pipeline_for_bms():
    return aggregate_pipeline_in_collection(collection=COLLECTION, pipeline=PIPELINE_FOR_BMS)

def load_raw_bms():
    return map_results_to_df_raw(get_results_of_pipeline_for_bms())

def rename_cols_for_bms(df):
    df.columns = [col.replace('지수', '') for col in df.columns]
    return df

def exclude_k200_col(df):
    df = df.drop(columns=['KOSPI200'])
    return df

def load_bms_from_mongodb(option_exlude_k200=True):
    raw = load_raw_bms()
    return (
        raw
        .copy()
        .pipe(lambda df: df.set_index('일자'))
        .pipe(rename_cols_for_bms)
        .pipe(exclude_k200_col if option_exlude_k200 else lambda df: df)
    )
