from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        # for i in range(1000):
        #     self.send(json.dumps({'message': randint(1, 100)}))
        #     sleep(1)

    def disconnect(self, close_code):
        self.accept()
        self.send({
            "type": "websocket.close"
        })
        self.close()
        print("disconnected", close_code)
