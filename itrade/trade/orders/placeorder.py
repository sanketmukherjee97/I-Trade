import threading
import json
from trade.orders import models
import requests
from requests.api import head
from django.contrib.auth import get_user_model
from .models import Orders
from trade.stock.models import Stock

User = get_user_model()


class PlaceOrder(threading.Thread):
    def __init__(self, API_KEY, SECRET_KEY, SYMBOL, id, options):
        threading.Thread.__init__(self)
        self.options = options
        self.id = id
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.SYMBOL = SYMBOL
        self.BASE_URL = "https://paper-api.alpaca.markets"
        self.ACCOUNT_URL = "{}/v2/account".format(self.BASE_URL)
        self.ORDERS_URL = "{}/v2/orders".format(self.BASE_URL)
        self.HEADER = {'APCA-API-KEY-ID': self.API_KEY,
                       'APCA-API-SECRET-KEY': self.SECRET_KEY}

    def get_account(self):
        r = requests.get(self.ACCOUNT_URL, headers=self.HEADER)

        return json.loads(r.content)

    def create_order(self, symbol, qty, side, type, time_in_force):
        data = {
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "type": type,
            "time_in_force": time_in_force
        }
        r = requests.post(self.ORDERS_URL, json=data, headers=self.HEADER)
        return json.loads(r.content)

    # response = create_order("AAPL", 100, "buy", "market", "gtc")
    # response = create_order("TSLA", 20, "sell", "market", "gtc")
    # print(response)

    def run(self):
        symbol = self.SYMBOL
        print(symbol)
        print(self.id)
        user = User.objects.get(id=self.id)
        stk = Stock.objects.get(user_id=self.id, stock=self.SYMBOL)
        order = Orders.objects.get(user_id=self.id, stock=self.SYMBOL)
        if self.options == 'buy':
            print(float(order.b_p))
            print(float(stk.price))
            while True:
                if float(order.b_p) > float(stk.price):
                    response = self.create_order(
                        str(order.stock).upper(), order.bquantity, self.options, "market", order.btime)
                    return "Order Placced"
                # print("order placing in prograce")
        elif self.options == 'sell':
            while True:
                if float(order.s_p) < float(stk.price):
                    response = self.create_order(
                        str(order.stock).upper(), order.squantity, self.options, "market", order.stime)
                    return "Soled"
        elif self.options == 'auto':
            while True:
                if float(order.b_p) > float(stk.price):
                    response = self.create_order(
                        str(order.stock).upper(), order.bquantity, "buy", "market", order.btime)
                    break

            while True:
                if float(order.s_p) < float(stk.price):
                    response = self.create_order(
                        str(order.stock).upper(), order.squantity, "sell", "market", order.stime)
                    break
            return "auto"
