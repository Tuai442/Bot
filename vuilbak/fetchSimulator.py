import pprint
from datetime import datetime

import pandas as pd


class Fetch:
    def __init__(self, df: pd.DataFrame, realistic=False):
        self.realistic = realistic # Zorgt voor double data en foute data

        self._current_index = 1

        if df.index.name == "Date":
            self.complete_df = df
            self._fetched_df = pd.DataFrame()
        else:
            raise IndexError("Date moet als index ingesteld zijn")

    def start(self, start_date: datetime=None, start_index: int=None):
        self.check_correct_start(start_date, start_index)

        if start_date:
            data = self.get_candle_by_date(start_date)
            i = self.get_index_from_date(start_date)
            self._fetched_df = self.complete_df[: start_date]
        elif start_index:
            data = self.get_candle_by_index(start_index)
            self._fetched_df = self.complete_df[:start_index]

        else:
            data = self.get_candle_by_index(0)
            self._fetched_df = self.complete_df[:0]


        return data

    def init_data_start(self, start_date: datetime=None, start_index: int=None) -> pd.DataFrame:
        if start_date:
            data = self.get_candle_up_to_date(start_date)
            self._fetched_df = data
        return data

    def next(self, itteration=1):
        if self.check_available_data():
            data = self.complete_df.iloc[self._current_index: self._current_index + itteration]
            self._current_index = self._current_index + itteration
            return data
        else:
            print("Er is geen data meer beschikbaar")
            return None

    def get_total_fetched_data(self):
        data = self.complete_df[: self._current_index]
        if len(self.complete_df) == len(data):
            # Alles is terug gegeven
            return None
        return data

    def get_dates(self):
        return list(self.complete_df.index)

    def check_correct_start(self, start_date, start_index):
        if start_date is not None and start_index is not None:
            raise Exception("Er kan maar een van de 2 parameter ingsteld worden")
        if start_date is not None:
            if start_date not in self.get_dates():
                raise Exception("De datum kan niet gevonden worden in de gegeven dataframe, "
                      f"hier zijn de mogelijkheden: {self.get_dates()}")
        if start_index is not None:
            if len(self.complete_df.index) < start_index:
                raise IndexError("Out of range")

    def get_index_from_date(self, date):
        dates_list = list(self.complete_df.index)
        return dates_list.index(date)

    def get_candle_by_date(self, start_date, auto_increment=True):
        # end = pd.Timestamp(start_date)
        end = self.get_index_from_date(start_date)
        if auto_increment:
            self._current_index = end
        return self.complete_df[end: end + 1]

    def get_candle_by_index(self, start_index, auto_increment=True):
        end = start_index
        if auto_increment:
            self._current_index = end
        return self.complete_df[end - 1: end]

    def check_available_data(self):
        if len(self.complete_df) < self._current_index:
            return False
        return True

    @property
    def fetched_df(self):
        return self._fetched_df

    def get_candle_up_to_date(self, start_date, auto_increment=True) -> pd.DataFrame:
        end = self.get_index_from_date(start_date)
        if auto_increment:
            self._current_index = end
        return self.complete_df[: end + 1]