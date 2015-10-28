import director, random
from constants import *

SOUND_CHANNEL = "left"
RUN_TIME = 22

def play():
	director.play_sound("scenes/p1/audio/grave_yard_moans.ogg", channel=SOUND_CHANNEL)
	director.set_on(GRABBER_RELAY, 0, 6)
	director.set_on(GRABBER_RELAY, 7.5, 9)
	director.set_on(GRABBER_RELAY, 17.5, 5)


# Setup a sound to play at random intervals
def background_sound():
	sounds = ("scenes/p1/audio/grave_yard_owl.ogg", "scenes/p1/audio/grave_yard_crickets.ogg", "scenes/p1/audio/grave_yard_crow.ogg",)
	director.play_sound(random.choice(sounds), volume=0.5, channel=SOUND_CHANNEL)

	director.schedule(random.randrange(7, 20), background_sound, ())


# init triggers etc
print('Load the grabber')
# Trigger the grabber on button 2 and disable button for RUNTIME+2 seconds after push
director.add_trigger(GRABBER_TRIGGER, play, (), bouncetime=RUN_TIME+2)


# Ambient track to loop in background
director.play_sound("scenes/p1/audio/grave_yard_idle.ogg", delay=0, loops=-1, channel=SOUND_CHANNEL)


# kick off the random background sounds
director.schedule(5, background_sound, ())