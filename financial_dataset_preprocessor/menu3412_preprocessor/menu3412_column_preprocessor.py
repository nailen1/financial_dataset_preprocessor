import pandas as pd
from pandas import DataFrame

def determine_col_name(row):
    if row['base'] == '기준':
        return f"{row['bm_label']}: {row['base']}"
    if row['ratio'] == '비율':
        return f"{row['bm_label']}: {row['ratio']}"
    if row['fx'] == '환율적용':
        return f"{row['bm_label']}: {row['fx']}"
    if row['bm_label'] == None:
        return row['col1']


def get_df_preprocessed_column_menu3412(menu3412: DataFrame) -> DataFrame:
    df = pd.DataFrame({'col1': list(menu3412.columns)})
    df['bm_index'] = df['col1'].apply(lambda x: f"{x.replace('BM기준구분', '')}" if 'BM기준구분' in x else None)
    df['bm_label'] = df['col1'].apply(lambda x: f"{x.split('기준구분')[0]}" if 'BM기준구분' in x else None)
    df['base'] = df['col1'].apply(lambda x: f"기준" if 'BM기준구분' in x else None)
    df['ratio'] = df['col1'].apply(lambda x: f"비율" if 'BM비율' in x else None)
    df['fx'] = df['col1'].apply(lambda x: f"환율적용" if '환율적용' in x else None)
    df['bm_label'] = df.apply(lambda x: f"{x['bm_label']}{x['bm_index']}" if x['bm_index']!=None else None, axis=1).ffill()
    df['col'] = df.apply(lambda x: determine_col_name(x), axis=1)
    return df

def get_preprocessed_column_names_menu3412(menu3412: DataFrame) -> list[str]:
    df = get_df_preprocessed_column_menu3412(menu3412)
    return list(df.iloc[:,-1])
