import pandas as pd

def aggregate_pipeline_in_collection(collection, pipeline):
    return collection.aggregate(pipeline)

def map_results_to_data(results):
    return results.to_list()

def map_data_to_df_raw(data):
    return pd.DataFrame(data)

def map_results_to_df_raw(results):
    return map_data_to_df_raw(map_results_to_data(results))