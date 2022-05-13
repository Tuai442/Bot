from datetime import datetime

import pandas as pd
from binance import Client

from Bot.App.Domain import Data
from Bot.App.Domain.Models.data_keys import Key


class RequestHandler:
    def __init__(self, client: Client, data: Data):
        self._client = client
        self._data = data
        self.request_has_been_made_dict = self.create_request_list()

    def get_historical_kline_data(self, symbol: str, interval: str, start_date: datetime, end_date: datetime):
        # TODO: controle van tijdzones.
        candle_list = self._client.get_historical_klines(symbol,
                                                         interval,
                                                         str(start_date), str(end_date))

        # Lijst omzetten naar df.
        candle_df = pd.DataFrame(columns=["Date", "Open", "Close", "High", "Low", "Volume"])
        for candle in candle_list:
            str_timestamp = str(candle[0])[:-3]
            date_time = datetime.fromtimestamp(int(str_timestamp))
            format_row = {"Date": date_time, "Open": float(candle[1]), "High": float(candle[2]),
                          "Low": float(candle[3]), "Close": float(candle[4]), "Volume": float(candle[5]),
                          "Interval": candle[6]}
            candle_df = candle_df.append(format_row, ignore_index=True)

        candle_df = candle_df.set_index("Date", inplace=True, drop=True)
        self._data.add_historical_df(symbol, interval, candle_df)

        # TODO: tijdelijke oplossing MOET veranderd worden.
        key = Key.create_key(symbol, interval)
        self.request_has_been_made_dict[key] = True

    def create_request_list(self):
        temp = dict()
        for key in Key:
            temp[key] = False
        return temp

    def is_request_made(self, key: Key):
        return self.request_has_been_made_dict[key]
