from constants import *
import director


def play():
	director.play_sound("scene/audio/COW.ogg")
	[director.set_on(PROP_1_RELAY, t, 0.5) for t in range(0,3)]
	director.set_on(PROP_1_RELAY, 5, 5)
	#director.schedule(10, play, ())


director.add_trigger(PUSH_BUTTON_1, play, ())
director.schedule(5, play, ())