#!/usr/bin/python

import signal, os, glob, imp, sys, threading, logging
import director, constants

logging.basicConfig(level=logging.DEBUG)

def load_scenes():
    """
    Load all py files in scene directory
    """
    
    print("Resetting Director")
    director.reset()
    reload(constants)

    print("Loading Scenes")
    _cwd = os.path.dirname(os.path.realpath(__file__))
    scenes = glob.glob(os.path.join(_cwd, "scenes/*.py"))

    for file_path in scenes:
        print("loading scene %s" % file_path)
        mod_name,file_ext = os.path.splitext(os.path.split(file_path)[-1])
        try:
            del sys.modules["scene_" + mod_name]
        except KeyError:
            pass
        scene_mod = imp.load_source("scene_" + mod_name, file_path)

def process_keyboard():
    try:
        while True:
            channel = sys.stdin.readline()
            try:
                channel = int(channel)
                director.trigger(channel)
            except ValueError:
                if channel == "r\n":
                    load_scenes()
                else:
                    pass
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        print "Process DONE."

# setup a thread to monitor key input
key_thread = threading.Thread(target=process_keyboard)
key_thread.daemon = True
key_thread.start()

# handle SIGTERM
def terminate(signum, frame):
    raise KeyboardInterrupt()
signal.signal(signal.SIGTERM, terminate)

# Load the scenes
load_scenes()

print("Press CTRL+C to exit")
try:
    while 1:
        director.tick()

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print "DONE."

finally:
    director.cleanup()

