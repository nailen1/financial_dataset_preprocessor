# from .menu2160_preprocessor.menu2160_consts import , COLUMN_NAME_RAW_FOR_PRICE_ADJUSTED, INITIAL_PRICE_DEFAULT
# from .preprocess_consts import COLUMN_NAME_PREPROCESSED_FOR_BBG_PRICE, COLUMN_NAME_RAW_FOR_BBG_CLOSE, INDEX_NAME_PREPROCESSED_FOR_DATE
# from .general_preprocess_utils import format_commaed_number
# from .dataset_concatenator import join_dataframes
# from string_date_controller import get_date_n_days_ago

# def preprocess_columns_in_timeseries(df, col_name_raw, col_name_preprocessed, index_name_preprocessed):
#     cols_to_keep = [col_name_raw]
#     df = (df[cols_to_keep]
#           .dropna()
#           .rename(columns={col_name_raw: col_name_preprocessed})
#           .rename_axis(index=index_name_preprocessed))
#     df[col_name_preprocessed] = df[col_name_preprocessed].apply(format_commaed_number)
#     return df

# def preprocess_zeroth_row_price_in_timeseries_menu2160(df, price_zeroth_row=INITIAL_PRICE_DEFAULT):
#     date_first = df.index.dropna()[0]
#     date_zeroth = get_date_n_days_ago(date_first, 1)
#     df.loc[date_zeroth, df.columns[0]] = price_zeroth_row
#     df = df.sort_index(ascending=True)
#     return df

# def preprocess_colum_name_in_timeseries(df, col_name_price, col_name_preprocessed):
#     df = (df.copy()
#           .rename(columns={col_name_price: col_name_preprocessed}))
#     return df

# def preprocess_timeseries_for_raw_menu2160(df):
#     df = (df.copy()
#           .pipe(lambda x: preprocess_columns_in_timeseries(x, COLUMN_NAME_RAW_FOR_PRICE_ADJUSTED, COLUMN_NAME_PREPROCESSED_FOR_PRICE_ADJUSTED, INDEX_NAME_PREPROCESSED_FOR_DATE))
#           .pipe(lambda x: preprocess_zeroth_row_price_in_timeseries_menu2160(x, price_zeroth_row=INITIAL_PRICE_DEFAULT)))
#     return df

# def preprocess_timeseries_bbg_index(df):
#     df = (df.copy()
#           .pipe(lambda x: preprocess_columns_in_timeseries(x, COLUMN_NAME_RAW_FOR_BBG_CLOSE, COLUMN_NAME_PREPROCESSED_FOR_BBG_PRICE, INDEX_NAME_PREPROCESSED_FOR_DATE)))
#     return df

# def preprocess_timeseries_of_prices(dfs):
#     return (join_dataframes(dfs)
#             .pipe(lambda x: x.ffill()))