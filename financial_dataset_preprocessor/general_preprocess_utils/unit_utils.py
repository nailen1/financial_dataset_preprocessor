
def convert_to_unit(number, currency='KRW', level=None):
    if pd.isna(number) or number == "NaN":
        return number

    number = abs(float(str(number).replace(',', '')))
    
    if currency.upper() == 'KRW':
        units = [
            (1e12, '조'),
            (1e8, '억'),
            (1e4, '만'),
            (1, '')
        ]
    elif currency.upper() == 'USD': 
        units = [
            (1e12, 'T'),
            (1e9, 'B'),
            (1e6, 'M'),
            (1e3, 'K'),
            (1, '')
        ]

    if level is None:
        level = len(units)

    result = []
    for i, (unit_value, unit_name) in enumerate(units[:level]):
        unit_count = int(number // unit_value)
        if unit_count > 0:
            result.append(f"{unit_count}{unit_name}")
        number %= unit_value

    if not result:
        return '0'

    return ' '.join(result)
