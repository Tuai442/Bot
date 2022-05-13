from abc import ABC, abstractmethod

import pandas as pd

from Startegie.Models.trend import Trend
from Startegie.Models.level import Level


class IGraph(ABC):
    @abstractmethod
    def get_candles(self) -> pd.DataFrame:
        pass
    @abstractmethod
    def get_trend(self) -> Trend:
        pass
    @abstractmethod
    def get_support_lines(self) -> Level:
        pass