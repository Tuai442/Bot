import pandas as pd


class Fetch:
    def __init__(self, df: pd.DataFrame):
        self._start = 0
        self._end = 1

        self.is_index_date = False

        self.data = df

    def start(self, end=None):
        if end == None:
            print("Kan geen start terug geven met NONE")
            return None

        data = None
        if isinstance(end, int):
            self._end += end
            data = self.data[self._start: self._end]
            self._start = self._end - 1

        elif isinstance(end, str):
            end = pd.Timestamp(end)
            index_list = list(self.data.index)
            self._end = index_list.index(end)
            data = self.data[self._start: self._end]


        return data

    def fetch(self, speed=1):
        if self.is_index_date:
            data = self.data.iloc[self._start: self._end]
            self._start += speed
            self._end += speed

        else:
            data = self.data[self._start: self._end]
            self._start += speed
            self._end += speed

        return data

    def get_total_fetched_data(self):
        data = self.data[: self._end]
        if len(self.data) == len(data):
            # Alles is terug gegeven
            return None
        return data
