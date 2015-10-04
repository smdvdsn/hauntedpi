from director import add_input, add_output, PUD_UP

# Add variables here for all of the inputs and outputs you want to use
# Call them something that makes sense for the setup

print "create inputs"
PUSH_BUTTON_1 = add_input(3)
PUSH_BUTTON_2 = add_input(7)

print "create outputs"
PROP_1_RELAY = add_output(16)
PROP_2_RELAY = add_output(20)
