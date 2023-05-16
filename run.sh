#!/bin/bash

export DISPLAY=:0

apt-get install xvfb -y
Xvfb :0 -screen 0 1024x768x24 &

python3 src/main.py