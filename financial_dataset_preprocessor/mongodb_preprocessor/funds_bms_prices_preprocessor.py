from .load_pipeline_prices import load_fund_prices_from_mongodb
from .load_pipeline_bms import load_bms_from_mongodb
from ..preprocess_consts import INDEX_NAME_PREPROCESSED_FOR_DATE

def get_timeseries_prices_funds_bms_from_mongodb(option_exlude_k200=False):
    fund_prices = load_fund_prices_from_mongodb()
    bms = load_bms_from_mongodb(option_exlude_k200=option_exlude_k200)
    prices_funds_bms = fund_prices.join(bms, how='left')
    return (
        prices_funds_bms
        .pipe(lambda df: df.fillna(0))
        .pipe(lambda df: df.rename_axis(index=INDEX_NAME_PREPROCESSED_FOR_DATE))
    )