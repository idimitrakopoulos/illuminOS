#!/bin/bash

# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.

# Initialize our own variables:
device="/dev/ttyUSB0"
profile="default"

function usage {
    echo ""
    echo "---------------------------------------------------------------------"
    echo "To install to board     : $0 -i [-p <profile>] [-d /dev/ttyUSB0] " 1>&2;
    echo "To uninstall from board : $0 -u [-d /dev/ttyUSB0]" 1>&2;
    echo "---------------------------------------------------------------------"
    echo ""
    exit 1;
}

function check_ampy {
    if hash ampy 2>/dev/null; then
        echo "Adafruit ampy is already installed..."
        sudo ls 1>/dev/null # making sure we have sudo access
    else
        sudo pip3 install adafruit-ampy
    fi
}


function install {
    echo ""
    echo "-----------------------"
    echo "Installing illuminOS"
    echo "-----------------------"
    echo ""

    for f in $(ls -t | grep -v illuminOS.sh)
    do

            if [ "$f" = "timestamp" ]
            then
                echo "Timestamp file found. Breaking ...."
                break
            fi
            printf "Uploading $f ......"
            sudo ampy --port /dev/ttyUSB0 put $f
            echo "[OK]"
    done

    touch timestamp

    echo ""
    echo "INSTALLATION COMPLETE!"
}


function apply_profile {
    if [ -d "profile/$profile" ]
    then
        echo "Overwriting files required for profile '$profile'"
        sudo ampy --port /dev/ttyUSB0 put profile/$profile/main.py main.py
        sudo ampy --port /dev/ttyUSB0 put profile/$profile/conf/profile.properties conf/profile.properties
    else
        echo "Error! Profile '$profile' doesn't exist"
    fi
}

function uninstall {
    echo ""
    echo "-----------------------"
    echo "Uninstalling illuminOS"
    echo "-----------------------"
    echo ""

    # Remove timestamp file if exist
    rm -f timestamp

    for f in $(ls | grep -v illuminOS.sh)
    do
            printf "Deleting $f ......"
            if [ -d "$f" ]; then
                sudo ampy --port /dev/ttyUSB0 rmdir $f 2>/dev/null
            else
                sudo ampy --port /dev/ttyUSB0 rm $f 2>/dev/null
            fi
            echo "[OK]"
    done

    echo ""
    echo "UNINSTALLATION COMPLETE!"
}

while getopts "h?d:p:uic" opt; do
    case "$opt" in
    h|\?)
        usage
        exit 0
        ;;
    d)  device=$OPTARG
        echo "Using device: $device"
        ;;
    p)  profile=$OPTARG
        echo "Using profile: $profile"
        apply_profile
        exit 0
        ;;
    u)  check_ampy
        uninstall
        exit 0
        ;;
    i)  check_ampy
        install
        ;;
    c)  sudo picocom --baud 115200 $device
        exit 0
        ;;
    esac
done

shift $((OPTIND-1))

[ "$1" = "--" ] && shift

# End of file