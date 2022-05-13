#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import datetime
from typing import List

import pandas as pd


class Trend():
	def __init__(self, trend: str, date_1: datetime, date_2: datetime):
		self._trend = trend
		self._first_date = date_1
		self._last_date = date_1

		if self._trend == "DOWN":
			self._color = "red"
		elif self._trend == "UP":
			self._color = "greend"
		else:
			raise Exception("trend is niet in correcte formaat kies uit DOWN of UP.")


	def to_dict(self):
		return {
			"x": [],
			"y": [],
			"color": self._color,
		}


	@property
	def trend(self):
		return self._trend