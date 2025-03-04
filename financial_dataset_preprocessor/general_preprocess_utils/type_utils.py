def transform_column_value_type_as_str(df, column):
    return df.assign(**{column: df[column].astype(str)})