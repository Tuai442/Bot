import time
from datetime import datetime
import pandas as pd

import mplfinance as mpf
import matplotlib.pyplot as plt
from IPython.core.display import clear_output
from matplotlib import animation
from Bot.App.Startegie.Agents.Agent import Agent
from Bot.App.Startegie.Testen.fetchSimulator import Fetch
from animator import Simulator



if __name__ == '__main__':
    # ../data/BTC-USD_lang.csv
    df = pd.read_csv("../data/BTC-USD.csv", index_col="Date", parse_dates=True)
    fetch = Fetch(df)
    print(fetch.get_dates())
    # "2021-01-19"
    date = datetime(year=2021, month=1, day=19)
    init_data = fetch.init_data_start(date)
    print(init_data)
    agent = Agent(None, "BTC", "1d")
    agent.initiate_fibonacci_strategy(init_data, 1000)


    Simulator = Simulator(agent, fetch, date)
    Simulator.start(speed=0.5)
    

        


