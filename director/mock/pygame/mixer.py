
def init():
	print("Mixer init")

def quit():
	print("Mixer quit")


class Sound:
	def __init__(self, sound):
		print("New sound: %s" % sound)

	def play(self,loops=0, maxtime=0, fade_ms=0):
		print("Play sound")

