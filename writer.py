import pyautogui as pag
from typing import List


class Writer:

	def __init__(self, default_interval):
		self.default_interval = default_interval


	def write_line(self, line: str, interval_start: float, interval_end: float):
		if interval_start == None:
			interval_start = self.default_interval
		if interval_end == None:
			interval_end = self.default_interval

		for symbol in line:
			interval = uniform(interval_start, interval_end) if interval_start < interval_end else interval_start
			pag.write(symbol, interval)


	def write_lines(self, lines: List[str], interval_start: float, interval_end: float):
		if interval_start == None:
			interval_start = self.default_interval
		if interval_end == None:
			interval_end = self.default_interval

		for line in lines:
			self.write_line(line, interval_start, interval_end)
			pag.write('\n')
			pag.press('home')
			interval = 0
