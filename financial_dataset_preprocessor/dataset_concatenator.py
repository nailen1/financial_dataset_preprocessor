from functools import reduce

def join_dataframes(dfs, join_type='left'):
    if not dfs:
        raise ValueError("Empty dataframe included.")
    
    df_base = dfs[0].copy()  
    dfs_remaining = dfs[1:]  
    
    return reduce(
        lambda acc, df: acc.join(df, how=join_type),
        dfs_remaining,
        df_base
    )