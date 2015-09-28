from constants import *
import director


def play():
	director.play_sound("audio/COW.ogg")
	director.set_on(PROP_1_RELAY, 0, 2)
	director.set_on(PROP_1_RELAY, 3, 2)
	director.set_on(PROP_1_RELAY, 6, 2)
	director.schedule(play, (), 10)


director.add_trigger(PUSH_BUTTON_1, play, ())