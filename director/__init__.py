import os, sched, heapq, threading, logging

logger = logging.getLogger(__name__)

# get the GPIO Library
try:
    import RPi.GPIO as GPIO
except ImportError:
    logger.warn("!!! Using MOCK GPIO !!!")
    import mock.GPIO as GPIO

# Mixer from pygame for sound
try:
    from pygame import mixer, time
except ImportError:
    logger.warn("!!! Using MOCK GPIO !!!")
    from mock.pygame import mixer, time

PUD_DOWN = GPIO.PUD_DOWN
PUD_UP = GPIO.PUD_UP

RISING = GPIO.RISING
FALLING = GPIO.FALLING

_clock = time.Clock()
_elapsed = 0

_events = []

_q_lock = threading.RLock()

def init():
    print "Init IO"
    GPIO.setmode(GPIO.BCM)

    print "Init sound"
    mixer.init()

init()






def tick():
    global _elapsed

    # look for events to trigger
    while _events:
        event = None

        with _q_lock:
            if _events[0][0] < _elapsed:
                event = heapq.heappop(_events)
                logger.debug("Triggering event %s %s", event[0], event[1].__name__)
                event[1](*event[2], **event[3])

        if event == None:
            break

    # tick clock 10 fps
    _elapsed += _clock.tick(60)

def _create_timer(delay, callback, args=[], kwargs={}):
    event = [(delay*1000)+_elapsed, callback, args, kwargs]
    with _q_lock:
        heapq.heappush(_events, event)
    logger.debug("Queue event for %ss - %s %s", delay, event[0], event[1].__name__)

def add_input(channel, pull_up_down=PUD_UP):
    """
    Configure a GPIO for input. This function returns the channel so can
    also be used to define constants for each channel

    e.g to define a constant for a push button on GPIO 5
    BUTTON_5 = director.add_input(5)
    """
    logger.info("Configure input %d", channel)
    # Default to PUD_UP so switch connect to ground
    GPIO.setup(channel, GPIO.IN, pull_up_down=pull_up_down)
    return channel

def add_output(channel, initial=False):
    """
    Configure a GPIO for output. This function returns the channel so can
    also be used to define constants for each channel

    e.g to define a constant for a relay switch on GPIO 5
    RELAY_5 = director.add_output(5)

    You can also optionally pass the inital value
    so the same call with default output HIGH would be
    RELAY_5 = director.add_output(5, True)
    """
    logger.info("Configure output %d", channel)
    GPIO.setup(channel, GPIO.OUT, initial=initial)
    return channel

def set_output(channel, value=True, delay=0, duration=None):
    """
    Sets an output HIGH/LOW. Takes optional delay and duration.
    Passing a duration will reverse the output after duration seconds

    e.g to set GPIO 23 HIGH for 10 seconds in 20 seconds time
    director.set_output(23, 1, 20, 10)
    """
    if delay > 0:
        _create_timer(delay, GPIO.output, (channel, value))
    else:
        GPIO.output(channel, value)

    if ( duration != None ):
        _create_timer(duration+delay, GPIO.output, (channel, not value))

def set_on(channel, delay=0, duration=None):
    """
    Sets an output HIGH. Takes optional delay and duration.
    Passing a duration will turn the output LOW after duration seconds

    e.g to set GPIO 23 HIGH for 10 seconds in 20 seconds time
    director.set_on(23, 20, 10)
    """
    set_output(channel, True, delay, duration)

def set_off(channel, delay=0, duration=None):
    """
    Sets an output LOW. Takes optional delay and duration.
    Passing a duration will turn the output HIGH after duration seconds

    e.g to set GPIO 23 LOW for 10 seconds in 20 seconds time
    director.set_off(23, 20, 10)
    """
    set_output(channel, False, delay, duration)

def add_trigger(channel, callback, args, bouncetime=200, edge=RISING):
    """
    Call a function when an input GPIO is triggered

    e.g to call the function play when GPIO 5 is triggered
    director.add_trigger(5, play, ()))
    """
    def trigger(channel):
        callback(*args)
    GPIO.remove_event_detect(channel)
    GPIO.add_event_detect(channel, edge, callback=trigger, bouncetime=bouncetime)

def schedule(delay, callback, args):
    """
    Schedules a function to be called after the defined delay in seconds

    e.g to call the play function after 10 seconds
    director.schedule(10, play, ())
    """
    _create_timer(delay, callback, args)


def play_sound(sound, delay=0, loops=0, maxtime=0, fade_ms=0):
    """
    Play the sound at the given file location.
    """
    #sound = os.path.join(_cwd, sound)
    if ( delay > 0 ):
        _create_timer(delay, play_sound, (sound,loops,maxtime,fade_ms,))
    else:
        logger.info("Playing sound %s loops %s", sound, loops)
        mixer.Sound(sound).play(loops=loops,maxtime=maxtime,fade_ms=fade_ms)

def cleanup():
    logger.info("Flush queue")
    with _q_lock:
        _events = []
    print "Cleanup IO"
    GPIO.cleanup() # cleanup all GPIO
    mixer.quit()

def reset():
    cleanup()
    init()
