### Usage

#### Running
To run hauntedpi

`$ python main.py`

#### Constants
Update the constants.py file with the details of your inputs and outputs

#### Scenes
For each scene you wish to configure create a file in the scenes dir.
See the files in that directory for examples but you should just
make calls to the director methods to play sound and switch you outputs.



## Director Commands

#### director.add_input(channel)

Configure a GPIO for input. This function returns the channel so can
also be used to define constants for each channel

e.g to define a constant for a push button on GPIO 5
BUTTON_5 = director.add_input(5)



#### director.add_output(channel, initial=False)

Configure a GPIO for output. This function returns the channel so can
also be used to define constants for each channel

e.g to define a constant for a relay switch on GPIO 5
RELAY_5 = director.add_output(5)

You can also optionally pass the inital value
so the same call with default output HIGH would be
RELAY_5 = director.add_output(5, True)


#### director.add_trigger(channel, callback, args, bouncetime=200, edge=RISING)

Call a function when an input GPIO is triggered

e.g to call the function play when GPIO 5 is triggered
director.add_trigger(5, play, ()))


#### director.schedule(function, arguments, delay)

Schedules a function to be called after the defined delay in seconds

e.g to call the play function after 10 seconds
director.schedule(play, (), 10)


#### director.set_on(channel, delay=0, duration=None)

Sets an output HIGH. Takes optional delay and duration.
Passing a duration will turn the output LOW after duration seconds

e.g to set GPIO 23 HIGH for 10 seconds in 20 seconds time
director.set_on(23, 20, 10)


#### director.set_off(channel, delay=0, duration=None)

Sets an output LOW. Takes optional delay and duration.
Passing a duration will turn the output HIGH after duration seconds

e.g to set GPIO 23 LOW for 10 seconds in 20 seconds time
director.set_off(23, 20, 10)


#### director.play_sound(sound, delay=0)

Play the sound at the given file location.



## Raspberry Pi Tips

#### Update rasbian
`$ sudo apt-get update`
`$ sudo apt-get upgrade`

#### Install pygame
`$ sudo apt-get install python-pygame`

#### Set mixer to auto output
If there is no sound from your pi when playing a sound file.
You can run the following command to set the audio output
Last number can also be 1 to force headphones.

`$ sudo amixer cset numid=3 0`



#### Hiss on audio output
https://github.com/raspberrypi/firmware/issues/380
Add the following line to the file /boot/config.txt

disable_audio_dither=1


