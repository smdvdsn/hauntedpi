import os, sched, time

from threading import Timer

# get the GPIO Library
#import RPi.GPIO as GPIO
import mock.GPIO as GPIO

# Mixer from pygame for sound
from mock.pygame import mixer


_channels = {}

print("*** Init IO")
GPIO.setmode(GPIO.BCM)

print("*** Init sound")
mixer.init()

cwd = os.path.dirname(os.path.realpath(__file__))

_timers = []

def _create_timer(delay, callback, args=[], kwargs={}):
    timer = None
    def trigger():
        callback(*args, **kwargs)
        _timers.remove(timer)

    timer = Timer(delay, trigger)
    _timers.append(timer)
    timer.start()

def add_input(channel, pull_up_down=GPIO.PUD_DOWN):
    GPIO.setup(channel, GPIO.IN, pull_up_down)
    return channel

def add_output(channel, initial=0):
    GPIO.setup(channel, GPIO.OUT, initial)
    return channel

def set_output(channel, value=1, delay=0, duration=None):
    Timer(delay, GPIO.output, (channel, value)).start()
    if ( duration != None ):
        _create_timer(duration+delay, set_output, (channel, not value))

def set_on(channel, delay=0, duration=None):
    set_output(channel, True, delay, duration)

def set_off(channel, delay=0, duration=None):
    set_output(channel, False, delay, duration)

def add_trigger(channel, callback, args, pull_up_down=GPIO.PUD_DOWN):
    def trigger(channel):
        callback(*args)
    GPIO.add_event_detect(channel, GPIO.RISING if pull_up_down == GPIO.PUD_DOWN else GPIO.FALLING, callback=trigger)

def schedule(callback, args, delay=0):
    print("Schedule %d" % delay)
    _create_timer(delay, callback, args)


def play_sound(sound, delay=None):
    sound = os.path.join(cwd, sound)
    if ( delay != None ):
        _create_timer(delay, play, (sound))
    else:
        mixer.Sound(sound).play()

def trigger(channel):
    GPIO.trigger(channel)

def cleanup():
    print "Cleaning up."
    [t.cancel() for t in _timers]

    print "Wait for timers"
    time.sleep(5)

    print "Cleanup IO"
    GPIO.cleanup() # cleanup all GPIO
    mixer.quit()


