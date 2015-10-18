#!/bin/bash
echo Sync changes...
rsync -avz -e ssh ./ pi@mypi.local:haunt/
echo Sync Success `date`
