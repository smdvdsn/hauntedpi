
def init():
	print("Mixer init")

def quit():
	print("Mixer quit")


class Sound:
	def __init__(self, sound):
		print("New sound: %s" % sound)

	def play(self):
		print("Play sound")
