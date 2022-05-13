
from abc import abstractmethod, ABC
import pandas as pd
#from Startegie.Strategy.pattern import Pattern

from Bot.App.Startegie.Strategy.patternReconizer import PatternReconizer


class IStrategy(ABC):
    @abstractmethod
    def next(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def update(self):
        pass


class Strategy(IStrategy):
    def __init__(self, df: pd.DataFrame, params: dict):
        self._params = params

        self._pattern_reconizer = PatternReconizer(params)
        self._patterns = list()

        self._total_df = df

    def next(self, df: pd.DataFrame):
        self._total_df = self._total_df.append(df, ignore_index=False)
        self._pattern_reconizer.reconize_patterns(self._total_df)
        self.calculate(df)


    def calculate(self, df: pd.DataFrame):
        for pattern in self._patterns:
            pattern.update(df)
            pattern.decider()


    @property
    def total_df(self) -> pd.DataFrame:
        return self._total_df

    # def find_trend(self, trend_interval: int) -> Trend:
    #     total_len = len(self._total_df)
    #     if total_len > trend_interval:
    #         close_1 = self._total_df["Close"][total_len - trend_interval]
    #         close_2 = self._total_df["Close"][-1]
    #         last_date = self._total_df.index[-1]
    #         if close_1 > close_2:
    #             # Down trend
    #             return Trend("DOWN", last_date, trend_interval)
    #         else:
    #             # Up trend
    #             return Trend("UP", last_date, trend_interval)

    def report_graph(self) -> dict:
       pass