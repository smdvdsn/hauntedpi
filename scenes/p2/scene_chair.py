import director, random
from constants import *


def reset():
	director.set_on(WELCOME_SIGN_RELAY)
	director.set_on(CHAIR_SPOT_RELAY)
	director.set_off(GREEN_LIGHT_RELAY)
	director.set_off(RED_LIGHT_RELAY)

	director.add_trigger(PIR_TRIGGER, enter, (), bouncetime=2)
	director.add_trigger(CHAIR_TRIGGER, play, (), bouncetime=2)

def enter():
	director.play_sound("scenes/p2/audio/take_a_seat.ogg")
	director.set_off(WELCOME_SIGN_RELAY, 2)
	director.remove_trigger(PIR_TRIGGER)

def play():
	switch_sound = director.load_sound("scenes/p2/audio/switch.ogg")

	# Siren
	director.set_on(SIREN_RELAY, 0, 13)
	director.play_sound("scenes/p2/audio/siren.ogg")

	# Green light and hum sound effect
	director.play_sound(switch_sound, 5)
	director.set_on(GREEN_LIGHT_RELAY, 5.5, 7.5)
	director.play_sound("scenes/p2/audio/switch_hum.ogg", 5, loops=-1, maxtime=4)
	
	# Red light
	director.play_sound(switch_sound, 6)
	director.set_on(RED_LIGHT_RELAY, 6.5, 6.5)
	
	# fire the chair
	director.set_on(CHAIR_VIBRATE_RELAY, 6.8, 5)
	director.play_sound("scenes/p2/audio/electric.ogg", 6, maxtime=6.5)

	# Flicker chair light
	director.set_off(CHAIR_SPOT_RELAY, 6.8)
	director.set_on(CHAIR_SPOT_RELAY, 6.9, 0.2)
	director.set_on(CHAIR_SPOT_RELAY, 7.9, 0.2)
	director.set_on(CHAIR_SPOT_RELAY, 8.3, 0.1)
	director.set_on(CHAIR_SPOT_RELAY, 8.7, 0.1)
	director.set_on(CHAIR_SPOT_RELAY, 8.9, 0.3)
	director.set_on(CHAIR_SPOT_RELAY, 9.5, 0.1)
	director.set_on(CHAIR_SPOT_RELAY, 9.7, 0.1)
	director.set_on(CHAIR_SPOT_RELAY, 10.4, 0.3)
	director.set_on(CHAIR_SPOT_RELAY, 11, 0.1)
	director.set_on(CHAIR_SPOT_RELAY, 11.3, 0.4)
	director.set_on(CHAIR_SPOT_RELAY, 12.2, 0.3)
	director.set_on(CHAIR_SPOT_RELAY, 12.8)

	# End sound
	director.play_sound(switch_sound, 12.5)

	# Reset
	director.schedule(20, reset, ())

	director.remove_trigger(CHAIR_TRIGGER)


# init triggers etc
print('Load the chair')
director.add_trigger(RESET_TRIGGER, reset, (), bouncetime=2)

reset()
