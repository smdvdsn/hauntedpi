import director
from constants import *

RUN_TIME = 6.7

def play():
	director.play_sound("scenes/audio/Monster.ogg")
	#[director.set_on(PROP_1_RELAY, t, 0.5) for t in range(0,9)]
	#[director.set_on(PROP_2_RELAY, t/1000, 0.2) for t in range(1000,5000,1000)]
	director.set_on(PROP_2_RELAY, 0, RUN_TIME)
	#director.schedule(10, play, ())


# init triggers etc
print('Load the grabber')
# Trigger the grabber on button 2 and disable button for RUNTIME+2 seconds after push
director.add_trigger(PUSH_BUTTON_2, play, (), bouncetime=RUN_TIME+2)