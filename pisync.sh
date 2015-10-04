#!/bin/bash
echo Change detected...
rsync -avz -e ssh src/ pi@mypi.local:haunt/src
echo Sync Success `date`
