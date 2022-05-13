import pprint
from datetime import datetime
from time import sleep

import pandas as pd

from Startegie.Agents.Agent import Agent

from Startegie.Strategy.fibonacci import Fibonacci
from Startegie.Strategy.pennants import Pennants
from Startegie.Strategy.rsi import RSI

from Startegie.Agents.IAgent import IAgent

from Bot.App.Startegie.Strategy.fibonacci import Pattern
from Bot.App.Startegie.Strategy.strategy import Strategy
from Bot.App.Startegie.Testen.fetchSimulator import Fetch

params = {
    "agent": {
        "pattern": None,
        "strategy": None,
        "wallet": float(),
        "fee": float(),
    },
    "boucne-margin": float(),
    "trend-interval": 3
}

class SimulationAgent(IAgent):
    def __init__(self, symbol: str, interval: str, df: pd.DataFrame, params: dict):
        self._total_df = df
        self._fee = params["fee"]
        self._simulation_wallet = params["wallet"]
        self._simulation_currency_wallet = 0.00
        self._fetch = Fetch(df)
        self._orders = dict()
        self._pattern: Pattern
        self._strategy = Strategy(df, params)

    def buy_order(self, quantity, add_info=""):
        self.check_proper_initialization()
        if self._simulation_wallet - (quantity * self._current_close) > 0:
            self._simulation_wallet -= (quantity * self._current_close)
            self._orders[self._current_date] = {
                "quantity": quantity,
                "additional_info": add_info
            }
            self._simulation_currency_wallet += quantity
        else:
            print("Er staat geen geld meer op de simulation wallet")

    def sell_order(self, quantity):
        self.check_proper_initialization()
        if self._simulation_currency_wallet - (quantity * self._current_close) > 0:
            self._simulation_currency_wallet -= (quantity * self._current_close)
            self._simulation_wallet += quantity
        else:
            print("Er staat geen geld meer op de simulation currency wallet")

    def init_fib(self):
        self._pattern = Fibonacci(self.df, self.params)

    def start(self, start_date: datetime):
        if self._pattern:
            self.isStarted = True
            init_data = self._fetch.init_data_start(start_date)
            return self._fetch.check_available_data()
        else:
            raise Exception("Er moet eerst een pattern geselecteerd worden.")

    def next_itteration(self, delay) -> dict:
        if self._isStarted:
            sleep(delay)
            self._fetch.next()
            self._pattern.update()
            return self._pattern.get_report()
        else:
            raise Exception("Moet eerst starten")



    def get_report_pattern(self) -> dict:
        """
        Hier bij moet alles van de GraphAnalyzer samengevoed worden om vervolgen in de View te kunnen bekeiken
        :return: List
        """
        self.check_proper_initialization_pattern()
        report = self._strategy.report_graph()
        print("report")
        pprint.pprint(report)
        return report


    @property
    def simulation_wallet(self):
        return self._simulation_wallet

    @property
    def total_df(self):
        return self._total_df
