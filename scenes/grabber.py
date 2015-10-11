import director, random
from constants import *

SOUND_CHANNEL = "left"
RUN_TIME = 12

def play(loops):
	director.play_sound("scenes/audio/Monster.ogg", channel=SOUND_CHANNEL)
	director.set_on(GRABBER_RELAY, 0, 2)
	director.set_on(GRABBER_RELAY, 2.5, 3)
	if loops > 0:
		loops = loops - 1
		director.schedule(6, play, (loops,))


# Setup a sound to play at random intervals
def background_sound():
	sounds = ("scenes/audio/owl.ogg", "scenes/audio/Crickets.ogg",)
	director.play_sound(random.choice(sounds), channel=SOUND_CHANNEL)

	director.schedule(random.randrange(5, 20), background_sound, ())


# init triggers etc
print('Load the grabber')
# Trigger the grabber on button 2 and disable button for RUNTIME+2 seconds after push
director.add_trigger(GRABBER_TRIGGER, play, (2,), bouncetime=RUN_TIME+2)


# Ambient track to loop in background
director.play_sound("scenes/audio/rainforest_ambience.ogg", delay=0, loops=-1, channel=SOUND_CHANNEL)


# kick off the random background sounds
director.schedule(5, background_sound, ())