import threading
import time
from .Data import *
import pandas as pd
from flask_socketio import SocketIO, emit


class WebSocketHandler():
    def __init__(self):
        self.data_list = list()
        self.col = ["Date","Open","High","Low","Close","Adj" "Close","Volume"]

    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()

    def run(self):
        # simuleer websocket
        symbol = "btcusdt"
        interval = "1d"
        data = Candle(symbol, interval)
        while True:
            with open("BTC-USD.csv", "r") as file:
                for line in file.readlines():
                    dataframe = pd.DataFrame([line.split(",")], columns=self.col)
                    dataframe = dataframe.set_index("Date")
                    data.add_candle(dataframe)
                    self.data_list.append(data)
                    time.sleep(4)


    def get_all_candle_data(self) -> list:
        return self.data_list







