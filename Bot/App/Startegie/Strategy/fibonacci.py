from abc import abstractmethod
from datetime import datetime
import pandas as pd

from typing import List
from Startegie.Models.level import Level
from Startegie.Strategy.strategy import Strategy
from Startegie.Models.trend import Trend




class Pattern:
    def __init__(self, df: pd.DataFrame, params: dict):
        self._params = params
        self._level_dict = dict()
        self._doij_dict = dict()
        self._trend_dict = dict()
        self._current_trend = self.find_trend(df, self._params["trend-interval"])
        self._df = df

    def find_trend(self, df: pd.DataFrame, trend_interval: int):
        df_len = len(df)
        if df_len > trend_interval:
            first_close = df["Close"][df_len - trend_interval]
            last_close = df["Close"][-1]
            date_1 = df.index[df_len - trend_interval]
            date_2 = df.index[-1]
            if first_close > last_close:
                self._trend_dict[date_2] = self._current_trend
                return Trend("DOWN", date_1, date_2)
            else:
                self._trend_dict[date_2] = self._current_trend
                return Trend("UP", date_1, date_2)
        return None

    def update(self, df: pd.DataFrame):
        self._current_trend = self.find_trend(df, self._params["trend-interval"])

    @abstractmethod
    def decider(self) -> float:
        """
        Druk in percentage uit of we iets moeten kopen of verkopen.
        negatief voor koop.
        positief voor verkoop.
        """
        pass

    def get_report(self) -> dict:
        return {
            "levels": self._level_list,
            "doij": self._doij_list
        }

    def update_levels(self, new_end_date: datetime):
        level = self._level_list[0]
        if new_end_date > level.end_date:
            for level in self._level_list:
                level.end_date = new_end_date


class Fibonacci(Pattern):
    def __init__(self, df, params: dict):
        super().__init__(df, params)
        self.RATIOS = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1]
        self._bounce_margin = params["bounce_margin"]
        self._level_dict = self._get_levels()
        self._fibonacci_trend = self.find_fib_trend(df)

    def _get_levels(self) -> dict:
        highest_close = self._df["High"].max()
        lowest_close = self._df["Low"].min()
        diffrence = highest_close - lowest_close
        levels = dict()
        for ratio in self.RATIOS:
            level = highest_close - (diffrence * ratio)
            level = Level(self._df.index[0], self._df.index[-1], level, tag=ratio, bounce_margin=self._bounce_margin)
            levels[ratio] = level

        return levels

    def update(self, df: pd.DataFrame):
        super().update(df)
        self.update_levels(df.index[-1])
        #self.check_for_bounces()

    def decider(self) -> float:
        if self._fibonacci_trend.trend == "DOWN":
            if self._current_trend.trend == "UP":
                self.check_for_bounces()

        elif self._fibonacci_trend.trend == "UP":
            if list(self._trend_dict.values())[-2].trend == "DOWN":
                pass

    def check_for_bounces(self):
        close = self._df["Close"][0]
        for key in self._level_dict.keys():
            level = self._level_dict[key]
            if level.is_in_bounce_region(close):
                level.add_bounce(self._df.index[0], close)
                return str(key)

        return None

    def find_fib_trend(self, df: pd.DataFrame):
        dates = list(df.index)

        highest_close = df["High"].max()
        latest_highest_close_date = df.loc[df["High"] == highest_close].tail(1).index
        latest_highest_close_date_index = dates.index(latest_highest_close_date)

        lowest_close = df["Low"].min()
        latest_lowest_close_date = df.loc[df["Low"] == lowest_close].tail(1).index
        latest_lowest_close_date_index = dates.index(latest_lowest_close_date)

        if latest_lowest_close_date_index > latest_highest_close_date_index:
            return Trend("DOWN", latest_highest_close_date, latest_lowest_close_date)
        else:
            return Trend("UP", latest_lowest_close_date, latest_highest_close_date)
