import director, random
from constants import *

SOUND_CHANNEL = "right"
RUN_TIME = 10

def play():
	# TOXIC_HAMMER_RELAY
	# TOXIC_LIFT_RELAY
	director.play_sound("scenes/p1/audio/toxic_trigger.ogg", delay=1, channel=SOUND_CHANNEL)
	director.set_on(TOXIC_LIFT_RELAY)

def limit_switch():
	director.set_off(TOXIC_LIFT_RELAY, 0)

# Setup a hammer to play at random intervals
def hammer_time():
	director.set_on(TOXIC_HAMMER_RELAY, 0, random.randrange(2000, 5000)/1000)
	director.schedule(random.randrange(20, 120), hammer_time, ())

print('Load the toxic man')
director.add_trigger(TOXIC_TRIGGER, play, (), bouncetime=RUN_TIME+2)
director.add_trigger(TOXIC_LIMIT_TRIGGER, limit_switch, (), bouncetime=1)

# Ambient track to loop in background
director.play_sound("scenes/p1/audio/toxic_idle.ogg", delay=0, loops=-1, channel=SOUND_CHANNEL)

# Kick off random hammer
director.schedule(5, hammer_time, ())