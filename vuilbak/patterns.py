from abc import ABC, abstractmethod

import numpy as np
import pandas as pd
import talib
from talib import CDL2CROWS, CDLDOJI


class IPattern(ABC):
    @abstractmethod
    def search(self):
        pass


class Reconizer:
    def __init__(self):
        self._pattern_list = list()
        self._trend_list = list()
        self.candle_names = talib.get_function_groups()['Pattern Recognition']

    def find_patterns(self, df: pd.DataFrame):
        open, high, low, close = df["Open"][0], df["High"][0], df["Low"][0], df["Close"][0]

        open = np.array([open], dtype=float)
        high = np.array([high], dtype=float)
        low = np.array([low], dtype=float)
        close = np.array([close], dtype=float)

        result = pd.DataFrame(columns=self.candle_names)
        for candle in self.candle_names:
            result[candle] = getattr(talib, candle)(open, high, low, close)

        return result
