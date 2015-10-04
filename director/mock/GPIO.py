import inspect

BCM = 0

IN = 0
OUT = 1

PUD_DOWN = 0
PUD_UP = 1

RISING = 0
FALLING = 1

detect = {}

def printFunc(vars, func):
	print (func.__name__, [vars[arg] for arg in inspect.getargspec(func).args])

def setmode(mode):
	printFunc(locals(), setmode)

def setup(channel, in_out, initial=1, pull_up_down=PUD_DOWN):
	printFunc(locals(), setup)

def input(channel):
	printFunc(locals(), input)

def output(channel, state):
	printFunc(locals(), output)

	callback = detect.get(channel, None)
	if ( callback != None ):
		callback(channel)

def add_event_detect(channel, state, callback, bouncetime=0):
	printFunc(locals(), add_event_detect)
	detect[channel] = callback

def remove_event_detect(channel):
	detect.pop(channel, None)

def cleanup():
	printFunc(locals(), cleanup)
