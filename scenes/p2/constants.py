from director import add_input, add_output, PUD_UP

# Add variables here for all of the inputs and outputs you want to use
# Call them something that makes sense for the setup

print "create inputs"
DOOR_TRIGGER = add_input(22)		# Photo beam at feet level
CHAIR_TRIGGER = add_input(27)		# Limit switch on the chair seat
PROXIMITY_TRIGGER = add_input(17)	# PIR trigger welcome sound
FOG_TRIGGER = add_input(23)			# Trigger a blast of fog

RESET_TRIGGER = add_input(18)		# External button outside room can reset before normal timeout


print "create outputs"
WELCOME_SIGN_RELAY = add_output(26)	# R1 - Flickering light for welcome sign
CHAIR_SPOT_RELAY = add_output(19)	# R2 - Chair light on solid during idle. Flicker with the electric sound when chair is going
SIREN_RELAY = add_output(11)		# R3 - Relay to turn on the rotating light
GREEN_LIGHT_RELAY = add_output(13)	# R4 - Relay for yellow bulb
RED_LIGHT_RELAY = add_output(6)		# R5 - Relay for red bulb
CLAXON_RELAY = add_output(16)		# R6 - Relay for Claxon (needs pulses)
CHAIR_VIBRATE_RELAY = add_output(5)	# R7 - Relay to actually turn the chair on
AIR_BLAST_RELAY = add_output(20)		# R8 - Air solenoid (slight delay after vib starts then 2 sec pulse off 1 sec pulse off)