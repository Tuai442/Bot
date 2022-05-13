



import pandas as pd
import yfinance as yf
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

df = pd.read_csv("../data/BTC-USD.csv", index_col="Date", parse_dates=True)


#test =  mpf.make_addplot(a, type='scatter', markersize=200, marker='^')
fig, axlist = mpf.plot(df[:100], type='candle', style= 'yahoo', returnfig=True)#addplot=test

date_index = df.index.get_loc('2021-01-29')
axlist[0].annotate('X', (date_index, 30000), fontsize=20, xytext=(date_index, 30000),
                   color='r',
                   arrowprops=dict(
                       arrowstyle='->',
                       facecolor='r',
                       edgecolor='r'))

mpf.show()
