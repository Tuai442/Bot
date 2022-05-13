#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Startegie.Strategy import strategy
from Startegie.Strategy.strategy import Strategy


class CustomStrategy(Strategy):
	def __init__(self, symbol: str, interval: str):
		super().__init__(symbol, interval)

	def calculate(self):
		pass

