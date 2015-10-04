from __future__ import absolute_import
import time

class Clock:
	def __init__(self):
		self.t = 0

	def tick(self, fps=0):
		now = time.time()
		self.d = (now - self.t) if self.t > 0 else 0
		self.t = now

		return self.get_time()

	def get_time(self):
		return self.d * 1000
