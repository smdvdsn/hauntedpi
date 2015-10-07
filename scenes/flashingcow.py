import director
from constants import *

RUN_TIME = 4.97

def play():
	director.play_sound("scenes/audio/COW.ogg")
	[director.set_on(PROP_1_RELAY, t, 0.5) for t in range(0,3)]
	director.set_on(PROP_1_RELAY, 3, 4.97)
	#director.schedule(10, play, ())


director.add_trigger(PUSH_BUTTON_1, play, (), bouncetime=RUN_TIME)