from director import add_input, add_output, PUD_UP

# Add variables here for all of the inputs and outputs you want to use
# Call them something that makes sense for the setup

print "create inputs"
PIR_TRIGGER = add_input(21)
CHAIR_TRIGGER = add_input(16)
RESET_TRIGGER = add_input(12)

print "create outputs"
WELCOME_SIGN_RELAY = add_output(26)
CHAIR_SPOT_RELAY = add_output(19)
SIREN_RELAY = add_output(11)
GREEN_LIGHT_RELAY = add_output(13)
RED_LIGHT_RELAY = add_output(6)
CHAIR_VIBRATE_RELAY = add_output(5)