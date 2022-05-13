#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import datetime


class Level:
	# _available_bg_colors = ["lightsalmon", "palegoldenrod", "palegreen", "powderblue", "plum", "lightpink"]
	_available_bg_colors = ["#4251bb", "#a3e99c", "#e27360", "#a42181", "#45a9be", "#769963", "#73e038"]
	_used_bg_colors = list()

	def __init__(self, start_date: datetime, end_date: datetime, close, bounce_margin: int=10, color="black", bg=None, tag=None):
		self._start_date = start_date
		self._end_date = end_date
		self._close = close
		self._tag = tag


		self._bounce_margin = bounce_margin
		self._bounce_list = list()

		self._color = str()
		if bg is None:
			self._background_color = Level.get_available_color()

		self.color = color


	def to_dict(self) -> dict:
		return {
			"x": [self._start_date.strftime('%Y-%m-%d %X'), self._end_date.strftime('%Y-%m-%d %X')],
			"y": [self._close, self._close],
			"name": self._tag,
			"background-color": self._background_color,
			"mode": "line",
			"line": {
				"color": self._color,
				"witdh": None,
			},
			"bounces": [[date.strftime('%Y-%m-%d %X'), close] for date, close in self._bounce_list]

		}
		
	def is_in_bounce_region(self, close: float):
		if self._close - self._bounce_margin < close < self._close + self._bounce_margin:
			return True
		return False

	def add_bounce(self, date, close):
		self._bounce_list.append((date, close))

	@property
	def bounce_list(self):
		return self._bounce_list

	@bounce_list.setter
	def bounce_list(self, value):
		self._bounce_list = value

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, value):
		self._color = value

	@property
	def background_color(self):
		return self._background_color

	@background_color.setter
	def background_color(self, value):
		if value in Level._used_bg_colors:
			raise Exception("Er kunnen geen 2 dezelfde achtergrond kleuren zijn")

		self._background_color = value
		Level._used_bg_colors.append(value)

	@classmethod
	def get_available_color(cls):
		if len(Level._available_bg_colors) > 0:
			color = Level._available_bg_colors[0]
			Level._available_bg_colors.remove(color)
		else:
			color = None
		return color

	@property
	def end_date(self):
		return self._end_date

	@end_date.setter
	def end_date(self, new_date):
		print("new date: ", new_date)
		self._end_date = new_date

	@property
	def tag(self):
		return self._tag

	def __repr__(self) -> str:
		return f"Level: {self._close}"


