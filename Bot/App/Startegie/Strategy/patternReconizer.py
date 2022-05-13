import pandas as pd

from Bot.App.Startegie.Strategy.fibonacci import Fibonacci


class PatternReconizer:
    def __init__(self, params: dict):
        self._params = params

    def reconize_patterns(self, df: pd.DataFrame) -> list:
        patterns = list()
        fib_pattern = self.check_fib_pattern(df, if_pattern_found_create=True)
        if fib_pattern:
            patterns.append(fib_pattern)

        return patterns


    def check_fib_pattern(self, df: pd.DataFrame, if_pattern_found_create=False):
        MIN_LEN_FIB = 10
        dates = list(df.index)

        highest_close = df["High"].max()
        latest_highest_close_date = df.loc[df["High"] == highest_close].tail(1).index
        latest_highest_close_date_index = dates.index(latest_highest_close_date)

        lowest_close = df["Low"].min()
        latest_lowest_close_date = df.loc[df["Low"] == lowest_close].tail(1).index
        latest_lowest_close_date_index = dates.index(latest_lowest_close_date)

        min_index = min(latest_lowest_close_date_index, latest_highest_close_date_index)
        max_index = max(latest_lowest_close_date, latest_highest_close_date_index)
        if len(df.iloc[min_index: max_index]) > MIN_LEN_FIB:
            if if_pattern_found_create:
                return Fibonacci(df, self._params)
            else:
                return True

        return False
