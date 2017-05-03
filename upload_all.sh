#!/bin/bash
function check_ampy {
    if hash ampy 2>/dev/null; then
        echo "Adafruit ampy is installed..."
    else
        sudo pip3 install adafruit-ampy
    fi
}

check_ampy

for f in $(ls)
do
        printf "Uploading $f ......"
        sudo ampy --port /dev/ttyUSB0 put $f
        echo "[OK]"

        #if [ -d "$f" ]; then

        #       echo ".... is a dir"
        #fi
done
