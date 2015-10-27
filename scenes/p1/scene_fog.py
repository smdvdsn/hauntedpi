import director, random
from constants import *

RUN_TIME = 10

def play():
	director.set_on(FOG_RELAY, 0, 10)

def loop():
	play()
	director.schedule(60, loop, ())

# init triggers etc
print('Load the fogger')
# Trigger the grabber on button 2 and disable button for RUNTIME+2 seconds after push
director.add_trigger(FOG_TRIGGER, play, (), bouncetime=RUN_TIME+2)

# Start fog loop after 20sec delay
director.schedule(20, loop, ())
