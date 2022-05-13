#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd

from Bot.App.Startegie.Strategy.strategy import Strategy


class RSI(Strategy):
	def __init__(self, symbol: str, interval: str, df: pd.DataFrame):
		super().__init__(symbol, interval)
		self._start_df = df

	def calculate(self, ema=True):
		close_delta = self._start_df['Close'].diff()

		# Maak twee series: één voor laage closes een andere voor hoge.
		up = close_delta.clip(lower=0)
		down = -1 * close_delta.clip(upper=0)

		rsi = None
		if ema == True:
			# Use exponential moving average
			ma_up = up.ewm(com = self.period - 1, adjust=True, min_periods = self.period).mean()
			ma_down = down.ewm(com = self.period - 1, adjust=True, min_periods = self.period).mean()
		else:
			# Use simple moving average
			ma_up = up.rolling(window = self.period, adjust=False).mean()
			ma_down = down.rolling(window = self.period, adjust=False).mean()

			rsi = ma_up / ma_down
			rsi = 100 - (100/(1 + rsi))
			rsi = rsi.values[-1] # van series naar np.float
		return rsi

	def next(self, df: pd.DataFrame):
		super().next(df)
