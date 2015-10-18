from __future__ import absolute_import
import time

class Clock:
	def __init__(self):
		self.t = 0

	def tick(self, fps=0):
		now = time.time()
		last = self.t if self.t > 0 else now
		self.d = now - last
		self.t = now

		if fps > 0 and self.d < (1000/fps):
			time.sleep(((1000/fps) - self.d) / 1000)

		return self.get_time()

	def get_time(self):
		return self.d * 1000
