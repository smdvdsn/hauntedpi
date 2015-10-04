#!/bin/bash
echo Change detected...
rsync -avz -e ssh ./ pi@mypi.local:haunt/
echo Sync Success `date`
