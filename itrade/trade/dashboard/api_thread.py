import websocket
import requests
import threading
import json

symbols = []
API_KEY = ""
SECRET_KEY = ""
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADER = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}


def get_account():
    global ACCOUNT_URL
    r = requests.get(ACCOUNT_URL, headers=HEADER)
    return json.loads(r.content)


def on_open(ws):
    global API_KEY, SECRET_KEY
    print("opened")
    auth_data = {"action": "auth", "key": API_KEY, "secret": SECRET_KEY}
    ws.send(json.dumps(auth_data))
    listen_message = {"action": "subscribe",
                      "trades": symbols, "bars": ["AM"]}
    ws.send(json.dumps(listen_message))


def on_message(ws, message):
    global baught
    message = message[1:-1]
    print("received a message")
    m = json.loads(message)
    m_price = float(m["p"])
    print(m_price)


def on_close(ws):
    print("closed connection")


class ApiThread(threading.Thread):

    def run(self):
        print(API_KEY)
        socket = "wss://stream.data.alpaca.markets/v2/iex"
        ws = websocket.WebSocketApp(socket, on_open=on_open,
                                    on_message=on_message, on_close=on_close)
        ws.run_forever()
