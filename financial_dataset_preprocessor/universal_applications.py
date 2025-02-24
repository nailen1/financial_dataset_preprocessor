from canonical_transformer import map_df_to_data, map_df_to_some_data

def get_all_mappings_of_df(df):
    df_ref = df
    somethings = df_ref.columns.tolist()
    dct = {}
    for something in somethings[1:]:
        df = df_ref.loc[:, something].reset_index()
        data = map_df_to_data(df)
        mapping = {datum['index']: datum[something] for datum in data}
        dct[something] = mapping
    return dct
    
def get_grouped_dfs_of_df(df, col):
    return dict(tuple(df.groupby(col)))

def get_mapping_of_column_pairs(df, key_col, value_col):
    data = map_df_to_some_data(df=df, cols=[key_col, value_col])
    mapping = {datum[key_col]: datum[value_col] for datum in data}
    return mapping