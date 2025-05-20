from string_date_controller import get_all_dates_between_dates

def get_dates_pair_of_timeseries(timeseries, start_date=None, end_date=None):
    initial_date, final_date = timeseries.index[0], timeseries.index[-1] 
    if start_date:
        initial_date = start_date if initial_date < start_date else initial_date
    if end_date:
        final_date = end_date if final_date > end_date else final_date
    return initial_date, final_date

def get_all_dates_for_timeseries(timeseries, start_date=None, end_date=None):
    initial_date, final_date = get_dates_pair_of_timeseries(timeseries, start_date, end_date)
    all_dates = get_all_dates_between_dates(initial_date, final_date)
    return all_dates

def extend_timeseries_by_all_dates(timeseries, start_date=None, end_date=None):
    df = timeseries.copy()
    print(f'(original) {df.index[0]} ~ {df.index[-1]}, {len(df)} days')
    all_dates = get_all_dates_for_timeseries(df, start_date, end_date)
    df_extended = df.reindex(all_dates).ffill()
    print(f'(extended) {df_extended.index[0]} ~ {df_extended.index[-1]}, {len(df_extended)} days')
    return df_extended
