from datetime import datetime

import pandas as pd

from Bot.App.Startegie.Testen.fetchSimulator import Fetch


API_KEY = 'ZJPghmU5njjfV5x7Fogzgf44BKuxPsHuBElzJAWkiJlaDEaH69YsgQsfd8xZAz4T'
API_SECRET = 'uSkzoCcBM4qdSY362TPpb3Sf5okB3ydPrAw8JHHT9twBSpOQyIz9fQESzxaCksmR'


if __name__ == '__main__':
    # ../data/BTC-USD_lang.csv
    df = pd.read_csv("data/BTC-USD.csv", index_col="Date", parse_dates=True)
    fetch = Fetch(df)
    # "2021-02-04"
    date = datetime(year=2021, month=2, day=4)
    data = fetch.start(date)
    total_data = fetch.get_total_fetched_data()

    # client = Client(API_KEY, API_SECRET)
    # agent = Agent(client)
    # agent.initiate_fibonacci_strategy("BTCUSDT", "1m", total_data)
    # while True:
    #     data = fetch.next()
    #     if data is None:
    #         break
    #
    #     agent.next(data)
    #     print(data)


