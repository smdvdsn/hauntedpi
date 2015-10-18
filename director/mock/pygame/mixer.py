
def init():
	print("Mixer init")

def quit():
	print("Mixer quit")

class Channel:
	def set_volume(self, *volume):
		print("Set volume")

class Sound:
	def __init__(self, sound):
		print("New sound: %s" % sound)

	def play(self,loops=0, maxtime=0, fade_ms=0):
		print("Play sound")
		return Channel()

