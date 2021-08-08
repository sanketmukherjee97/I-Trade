import json
import requests
import threading
from trade.stock.models import Stock


class PriceThread(threading.Thread):

    def __init__(self, API_KEY, SECRET_KEY, SYMBOL):

        threading.Thread.__init__(self)
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.SYMBOL = SYMBOL

        self.MAIN = "https://paper-api.alpaca.markets/v2/account"
        BASE_URL = "https://data.alpaca.markets/v2"

        self.TRADE_URL = "{}/stocks/{}/trades/latest".format(BASE_URL, SYMBOL)
        self.HEADER = {'APCA-API-KEY-ID': API_KEY,
                       'APCA-API-SECRET-KEY': SECRET_KEY}

    def get_account(self):
        r = requests.get(self.MAIN, headers=self.HEADER)

        return json.loads(r.content)

    def get_trade(self):
        t = requests.get(self.TRADE_URL, headers=self.HEADER).json()
        return t

    def run(self):
        self.get_account()
        while True:
            response = self.get_trade()
            symbol = response['symbol']
            st = Stock.objects.get(stock=str(symbol).lower())
            tr = response['trade']
            price = tr['p']
            st.price = str(price)
            st.save()
            # print("Symbol: " + str(symbol), "Price: " + str(price))
