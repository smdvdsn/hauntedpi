from constants import *
import director


def play():
	#[director.set_on(PROP_1_RELAY, t, 0.5) for t in range(0,9)]
	[director.set_on(PROP_2_RELAY, t/1000, 0.2) for t in range(1000,5000,1000)]
	director.set_on(PROP_2_RELAY, 5.2, 5)
	#director.schedule(10, play, ())


# init triggers etc
print('just a grabber')
director.set_off(PROP_2_RELAY)
director.add_trigger(PUSH_BUTTON_2, play, ())