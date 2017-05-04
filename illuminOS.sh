#!/bin/bash

# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.

# Initialize our own variables:
port="/dev/ttyUSB0"

function usage {
    echo ""
    echo "---------------------------------------------------------------------"
    echo "To install to board     : $0 [-p /dev/ttyUSB0] -i" 1>&2;
    echo "To uninstall from board : $0 [-p /dev/ttyUSB0] -u" 1>&2;
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

    for f in $(ls | grep -v illuminOS.sh)
    do
            printf "Uploading $f ......"
            sudo ampy --port /dev/ttyUSB0 put $f
            echo "[OK]"
    done

    echo ""
    echo "INSTALLATION COMPLETE!"
}

function uninstall {
    echo ""
    echo "-----------------------"
    echo "Uninstalling illuminOS"
    echo "-----------------------"
    echo ""

    for f in $(ls | grep -v illuminOS.sh)
    do
            printf "Deleting $f ......"
            if [ -d "$f" ]; then
                sudo ampy --port /dev/ttyUSB0 rmdir $f
            else
                sudo ampy --port /dev/ttyUSB0 rm $f
            fi
            echo "[OK]"
    done

    echo ""
    echo "UNINSTALLATION COMPLETE!"
}

while getopts "h?p:iu" opt; do
    case "$opt" in
    h|\?)
        usage
        exit 0
        ;;
    p)  port=$OPTARG
        echo "Using port: $port"
        ;;
    i)  check_ampy
        install
        exit 0
        ;;
    u)  check_ampy
        uninstall
        exit 0
        ;;
    esac
done

shift $((OPTIND-1))

[ "$1" = "--" ] && shift

# End of file