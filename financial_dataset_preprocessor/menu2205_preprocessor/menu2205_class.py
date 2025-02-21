from .menu2205 import preprocess_raw_menu2205
from .menu2205_consts import ASSET_CATEGORIES
from financial_dataset_loader import load_menu2205
from canonical_transformer import map_df_to_some_data

class Menu2205:
    def __init__(self, fund_code, date_ref=None, option_data_source='s3'):
        self.menu_code = '2205'
        self.fund_code = fund_code
        self.date_ref = date_ref
        self.raw = self.get_raw(option_data_source=option_data_source)
        self.df = self.get_df()
        self.asset = self.get_asset()
        self.stock = self.get_stock()
        self.bond = self.get_bond()
        self.num_shares = self.get_number_of_shares()
    
    def get_raw(self, option_data_source='s3'):
        self.raw = load_menu2205(self.fund_code, date_ref=self.date_ref, option_data_source=option_data_source)
        return self.raw
    
    def get_df(self):
        self.df = preprocess_raw_menu2205(menu2205=self.raw)
        return self.df

    def get_asset(self):
        df = self.df
        self.asset = {category: df[df['자산']==category] for category in ASSET_CATEGORIES}
        return self.asset

    def get_stock(self):
        self.stock = self.asset[ASSET_CATEGORIES[0]]
        return self.stock

    def get_bond(self):
        self.bond = self.asset[ASSET_CATEGORIES[1]]
        return self.bond

    def get_number_of_shares(self):
        df = self.df
        df = df[df['종목명']!='소계']
        cols = ['종목명', '원화 보유정보: 수량']
        self.num_shares = map_df_to_some_data(df=df, cols=cols)
        return self.num_shares