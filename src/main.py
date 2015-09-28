#!/usr/bin/env python

import os, glob, imp, threading
import director, constants

print("Load Scenes")
cwd = os.path.dirname(os.path.realpath(__file__))
scenes = glob.glob(os.path.join(cwd, "scene/*.py"))

for file_path in scenes:
    print("loading scene %s" % file_path)
    mod_name,file_ext = os.path.splitext(os.path.split(file_path)[-1])
    scene_mod = imp.load_source(mod_name, file_path)

print("Press CTRL+C to exit")
try:
    while 1:
    	channel = raw_input("Channel:")
        try:
            director.trigger(int(channel))
        except ValueError:
            pass

        print("Director timers %d / %d" % (len(director._timers), len(threading.enumerate())))

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print "DONE."

finally:
    director.cleanup()

