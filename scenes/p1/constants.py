from director import add_input, add_output, PUD_UP

# Add variables here for all of the inputs and outputs you want to use
# Call them something that makes sense for the setup

print "create inputs"
GRABBER_TRIGGER = add_input(12)
TOXIC_TRIGGER = add_input(21)
TOXIC_LIMIT_TRIGGER = add_input(16)

print "create outputs"
GRABBER_RELAY = add_output(26)
TOXIC_HAMMER_RELAY = add_output(19)
TOXIC_LIFT_RELAY = add_output(13)
#PROP_2_RELAY = add_output(6)
