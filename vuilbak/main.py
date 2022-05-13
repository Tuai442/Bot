from abc import ABC, abstractmethod
from datetime import datetime

import pandas as pd
import requests
from matplotlib import pyplot as plt

from vuilbak.fetchSimulator import Fetch
from vuilbak.strategy import Fibonacci

import mplfinance as mpf
pd.set_option('display.max_columns', 500)


# link for Bitcoin Data


if __name__ == '__main__':
    df = pd.read_csv("data/BTC_TEST_1.csv", index_col=0, parse_dates=True)
    fetch = Fetch(df)

    # 2021-12-01
    date = datetime(year=2021, month=12, day=2)
    fetch.start()

    f = Fibonacci("test")
    while fetch.check_available_data():
        data = fetch.next()
        if data.empty == False:
            f.process(data)

    f.save_report("report.xlsx")


    mpf.plot(df, type="candle", style="yahoo")

# 2021-12-17