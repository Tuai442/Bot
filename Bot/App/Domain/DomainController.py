import pprint
import typing
from datetime import datetime, timedelta

import pandas
from binance import Client
import pandas as pd

#TODO: dit moet in config komen.
from Domain.Models.singletonDecorader import singleton
from Domain.plotlyAdapter import PlotlyAdapter
from Domain.svgGenerator import SVGgenerator
from Startegie.Agents.Agent import Agent
from Startegie.Agents.SimulationAgent import SimulationAgent

from Bot.App.Startegie.Strategy.fibonacci import Fibonacci

API_KEY = 'ZJPghmU5njjfV5x7Fogzgf44BKuxPsHuBElzJAWkiJlaDEaH69YsgQsfd8xZAz4T'
API_SECRET = 'uSkzoCcBM4qdSY362TPpb3Sf5okB3ydPrAw8JHHT9twBSpOQyIz9fQESzxaCksmR'
CANDLE_HEADERS = ["Date", "Open","High","Low","Close","Adj Close","Volume"]

@singleton
class DomainController:
    # socket_handler: WebSocketHandler, request_handler: RequestHandler
    def __init__(self):
        self._socket_handler = None
        self._request_handler = None

        self.i = 0
        self._plotly_adapter = PlotlyAdapter()
        self._svg_generator = SVGgenerator()
        self._init_data = pd.DataFrame(columns=CANDLE_HEADERS)
        self._client = Client(API_KEY, API_SECRET)
        self._agent = Agent(self._client, "", "")
        self._simulation_agent = None
        self._level_already_exists = False
        # self._simulation_agent = SimulationAgent(self._client)

    def list2df(self, data: list) -> pd.DataFrame:
        df = pd.DataFrame(columns=CANDLE_HEADERS)
        print("data ", data)
        for index in range(len(data)):
            date = pandas.to_datetime(data[index][0])
            df = df.append({"Date": date, "Open": data[index][1], "High": data[index][2], "Low": data[index][3],
                            "Close": data[index][4], "Adj Close": data[index][5], "Volume": data[index][6]}, ignore_index=True)

        df["Date"] = pd.to_datetime(df["Date"], format='%Y/%m/%d %H:%M:%S')
        df = df.set_index("Date")
        return df

    def candleList2dict(self, candle_list: list) -> typing.Dict:
        candle_dict = dict()
        try:
            candle_dict["Date"] = candle_list[0]
            candle_dict["Open"] = candle_list[1]
            candle_dict["High"] = candle_list[2]
            candle_dict["Low"] = candle_list[3]
            candle_dict["Close"] = candle_list[4]
            candle_dict["Adj Close"] = candle_list[5]
            candle_dict["Volume"] = candle_list[6]
            return candle_dict

        except Exception as e:
            raise Exception(f"Kan candle_list niet omzetten naar dict - {e}")
    # def start_agent(self, symbol: str, interval: str, init_data: list=None) -> bool:
    #     """
    #      Sommige strategieën hebben een bepaalde hoeveelheid start data nodig
    #      daarom wordt er een return voorzien of de agent gestart is om nog meer data
    #      nodig heeft om te kunnen beginnen.
    #     """
    #     # TODO: er kunnen verschillende soorten strategie gestart worden zorg er voor dat dit hier kan gebeuren.
    #     if init_data:
    #         # self._init_data = pd.DataFrame(self.candleList2dict(init_data))
    #         d = self.candleList2dict(init_data)
    #         self._init_data = self._init_data.append(d, ignore_index=True)
    #
    #         if Agent.MIN_DF_LEN < len(self._init_data):
    #             self._init_data = self._init_data.set_index("Date")
    #             self._agent.initiate_fibonacci_strategy(symbol, interval, self._init_data)
    #             return True
    #     else:
    #         pass
    #         # self._agent.initiate_fibonacci_strategy("BTCUSDT", "1m", start_data)
    #
    #     return False

    # Voor andere soort test voorlopig niet meer van toepassing

    # def initialize_simulator(self):
    #     df = pd.read_csv("View/data/BTC-USD.csv", index_col="Date", parse_dates=True)
    #     self.simulator = Fetch(df)
    def get_historical_candles(self, symbol: str, interval: str, start_date: str = None, end_date: str = None):
        if start_date is None and end_date is None:
            end_date = datetime.now()
            start_date = end_date - timedelta(hours=5)
        candlesticks = self._client.get_historical_klines(symbol, interval, str(start_date), str(end_date))

        processed_candlesticks = []

        for data in candlesticks:
            candlestick = {
                "time": data[0] / 1000,
                "open": data[1],
                "high": data[2],
                "low": data[3],
                "close": data[4]
            }

            processed_candlesticks.append(candlestick)

        return processed_candlesticks

    def reset_simulator(self):
        self._simulation_agent = None
    # Simulator
    def create_simulation_agent(self, data):
        params = dict()
        if data["agent"]:
            if data["agent"]["pattern"] == "fibonacci":
                pattern = Fibonacci()


        symbol = data["symbol"]
        interval = data["interval"]
        wallet = float(data["wallet"])
        bounce_margin = int(data["bounce-margin"])
        trend_interval = int(data["trend-interval"])
        total_data = self.list2df(data["data"])
        self._simulation_agent = SimulationAgent(symbol, interval, total_data, {
            "wallet": wallet,
            "fee": 0.0,
            "bounce-margin": 4,
            "trend-interval": 3
        })

        if data["type"] == "fibonacci":
            dates = total_data.index.to_list()
            init_date = pandas.to_datetime(data["init-data"])
            date_index = [date for date in dates if date == init_date]
            init_DATA = total_data.loc[: date_index[0]]
            self._simulation_agent.initiate_fibonacci_strategy(init_DATA, bounce_margin, trend_interval)

        elif data["type"] == "rsi":
            pass

    def process_candle_data(self, candle: list):
        if self._simulation_agent.strategy:
            # temp = self.candleList2dict(candle[0])
            # candle_df = pd.DataFrame(temp, index=["Date"])
            # candle_df = candle_df.set_index("Date")
            candle_df = self.list2df(candle)
            self._simulation_agent.next(candle_df)

        else:
            raise Exception("Er moet eerst een strategie gemaakt worden.")

    def get_graph(self) -> dict:
        graph_info = dict()
        if self._simulation_agent.strategy:
            total = self._simulation_agent.get_graph()
            self.i +=1
            pprint.pprint(total)
            for key in total.keys():
                # Levels omzetten naar plotly-data
                if key == "levels":
                    self._plotly_adapter.reset_rect_shape()
                    first = True
                    previous_level = None
                    for level in total[key].keys():
                        value = total[key][level]
                        if first:
                            y_0 = value["y"][0]
                            y_1 = value["y"][1]
                            previous_level = value["y"][1] # volgende iteratie van toepassing
                        else:
                            y_0 = previous_level
                            y_1 = value["y"][0]
                            previous_level = value["y"][1]
                        first = False

                        p1 = (value["x"][0], y_0)
                        p2 = (value["x"][1], y_1)
                        self._plotly_adapter.add_rect_shape(p1, p2, value["background-color"])
                        self._level_already_exists = True

                # Bounces van levels omzetten naar plotly-data
                if key == "levels":
                    # Verwijdere oude data en vervangen door nieuwe data
                    self._plotly_adapter.delete_key("annotations")
                    for level in total[key].keys():
                        for bounce in total[key][level]["bounces"]:
                            self._plotly_adapter.add_annotations(bounce, "bounce")

            result = self._plotly_adapter.plot
            result["wallet"] = self._simulation_agent.simulation_wallet
            # pprint.pprint(result)
            return result
        return graph_info




