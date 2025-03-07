from ..general_preprocess_utils import parse_commaed_number, force_int

def preprocess_column_values_to_numbers(df, cols):
    for col in cols:
        try:
            df[col] = df[col].map(parse_commaed_number)
        except KeyError as e:
            print(f"Column not found: {col}")
        except Exception as e:
            print(f"Error processing column {col}: {e}")
    return df

def preprocess_column_value_to_integers(df, cols):
    for col in cols:
        try:
            df[col] = df[col].map(force_int)
        except KeyError as e:
            print(f"Column not found: {col}")
        except Exception as e:
            print(f"Error processing column {col}: {e}")
    return df