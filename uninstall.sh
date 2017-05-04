#!/bin/bash
function check_ampy {
    if hash ampy 2>/dev/null; then
        echo "Adafruit ampy is installed..."
        sudo ls
    else
        sudo pip3 install adafruit-ampy
    fi
}

check_ampy

for f in $(ls)
do
        printf "Deleting $f ......"


        if [ -d "$f" ]; then

            sudo ampy --port /dev/ttyUSB0 rmdir $f

        else

            sudo ampy --port /dev/ttyUSB0 rm $f

        fi


        echo "[OK]"
done
