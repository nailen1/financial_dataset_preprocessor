from aws_s3_controller import scan_files_in_bucket_by_regex, load_csv_in_bucket
from canonical_transformer.functionals import pipe
from canonical_transformer.morphisms import map_df_to_data

def load_menu5105(date_ref=None):
    regex = 'code000005' if date_ref is None else f'code000005-.*to{date_ref.replace("-", "")}'
    file_names = sorted(scan_files_in_bucket_by_regex(bucket='dataset-system', bucket_prefix='dataset-menu5105', regex=regex, option='name'))
    raw = load_csv_in_bucket(bucket='dataset-system', bucket_prefix='dataset-menu5105', regex=file_names[-1])
    return raw

def get_data_menu5105(date_ref=None):
    return pipe(
        load_menu5105,
        map_df_to_data
    )(date_ref)

def preprocess_menu5105(raw):
    COLS_TO_KEEP = ['구간초일', 'Rf']
    df = raw[COLS_TO_KEEP].rename(columns={'구간초일': 'date', 'Rf': 'return_free'}).set_index('date')
    return df

def get_df_free_return(date_ref=None):
    return pipe(
        load_menu5105,
        preprocess_menu5105
    )(date_ref)

def get_data_free_return(date_ref=None):
    return pipe(
        get_df_free_return,
        map_df_to_data
    )(date_ref)