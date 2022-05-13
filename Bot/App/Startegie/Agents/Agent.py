#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pprint
from abc import ABC, abstractmethod

import pandas as pd
from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_LIMIT, TIME_IN_FORCE_GTC

#from Startegie.Strategy.CustomStrategy import CustomStrategy

import binance

from typing import List, Type

from Startegie.Strategy.fibonacci import Fibonacci
from Startegie.Strategy.strategy import Strategy
from Startegie.Agents.IAgent import IAgent


class Agent(IAgent):
    # Fibonacci:
    MIN_DF_LEN = 5
    def __init__(self, client, symbol: str, interval: str):
        self._client: binance.Client = client
        #self._logger = CustomLog(__name__, testing_mode=False)

        self._order_list: List = None
        self._strategy: Strategy = None

        self._symbol = symbol
        self._interval = interval

        self._current_close = None
        self._current_date = None

        self._currency_wallet: float = None
        self._usd_wallet: float = None
        self.i = 0

    def next(self, df: pd.DataFrame):
        """ Doorgeef luik + data wordt hier ook gecontroleerd. """
        # Een df MOET een lengte van 1 hebben niet meer niet minder.
        if self._strategy is not None:
            if len(df) == 1:
                # waarde update
                self._current_close = df["Close"][-1]
                self._current_date = df.index[-1]



                self._strategy.next(df)
            else:
                raise Exception("Er mag maar een df doorgegeven worden dat een lengte van één moet hebben.")
        else:
            raise Exception("Er moet eerst een strategie gemaakt worden.")

    def update(self):
        pass
    
    def buy_order(self, quantity):
        self.check_proper_initialization()
        self._client.create_test_order(symbol=self._symbol,
                                       side=SIDE_BUY,
                                       type=ORDER_TYPE_LIMIT,
                                       timeInForce=TIME_IN_FORCE_GTC,
                                       quantity=quantity,
                                       price=self._current_close)

    def sell_order(self, quantity):
        self.check_proper_initialization()
        self._client.create_test_order(symbol=self._symbol,
                                       side=SIDE_SELL,
                                       type=ORDER_TYPE_LIMIT,
                                       timeInForce=TIME_IN_FORCE_GTC,
                                       quantity=quantity,
                                       price=self._current_close)

    def calculate_profit(self) -> complex:
        pass


    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strat):
        self._strategy = strat





