from abc import ABC, abstractmethod

import pandas as pd
from backtrader import talib

from vuilbak.patterns import Reconizer


class Strategy(ABC):
    def __init__(self):
        self._reconizer = Reconizer()
        self._total_df = pd.DataFrame(columns=["Date","Open","High","Low","Close","Adj Close","Volume"])
        self._total_df = self._total_df.set_index("Date")
        self._total_patterns = None
        

    @abstractmethod
    def process(self, df: pd.DataFrame):
        pass

    def get_total_df(self):
        return self._total_df

    def _save_df(self, df):
        self._total_df = pd.concat([self._total_df, df])

    def _save_pattern(self, df):
        self._total_patterns = pd.concat([self._total_patterns, df], ignore_index=True)

    def save_report(self, path):
        self._total_df  = self._total_df.reset_index()
        self._total_df = self._total_df.join(self._total_patterns)
        self._total_df  = self._total_df.set_index("Date")

        self._total_df.index = self._total_df.index.map(str)
        self._total_df.to_excel(path)


class Fibonacci(Strategy):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def process(self, df: pd.DataFrame):
        self._save_df(df)
        result = self._reconizer.find_patterns(df)
        self._save_pattern(result)

