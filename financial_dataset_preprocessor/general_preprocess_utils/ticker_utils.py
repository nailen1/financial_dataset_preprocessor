
def get_ticker_bbg_of_ticker(ticker):
    return f"{ticker} KS Equity".replace(' KS KS', ' KS')

def get_ticker_from_ticker_bbg(ticker_bbg):
    return ticker_bbg.replace(' Equity', '')

map_ticker_to_ticker_bbg = get_ticker_bbg_of_ticker
map_ticker_bbg_to_ticker = get_ticker_from_ticker_bbg