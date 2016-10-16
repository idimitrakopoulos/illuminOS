#!/bin/bash

echo '''
 _ _ _                 _       _____ _____
(_) | |               (_)     |  _  /  ___|
 _| | |_   _ _ __ ___  _ _ __ | | | \ `--.
| | | | | | | `_ ` _ \| | `_ \| | | |`--. \
| | | | |_| | | | | | | | | | \ \_/ /\__/ /
|_|_|_|\__,_|_| |_| |_|_|_| |_|\___/\____/ v0.2

'''

MPF_FILE="illuminos.mpf"
DEFAULT_TTY="ttyUSB0"

SKIP_DIRS=("skip1 skip2")

if [ $# -eq 0 ]; then
	echo "Usage: ./${0##*/} <tty>"
	echo ""
	echo "[NOTES]"
	echo "No <tty> provided; $DEFAULT_TTY will be used!"
	TTY=$DEFAULT_TTY
else
	TTY=$1
fi

printfill()
{
	printf -v es '%*s' $2 ''
	echo "${es// /  }$1"
}

recurse()
{
	local INX=$2
	for i in "$1"/*;do
		if [ -d "$i" ];then
			IS_OK=true
			for skdir in $SKIP_DIRS; do
				if [ "$(basename $i)" == $skdir ]; then
					IS_OK=false
					break
				fi
			done

			if [ $IS_OK == true ]; then
			    printfill "$(basename $i)/" $INX
				echo "mput ${i}" >> $MPF_FILE
			    INX=$((INX+1))
			    recurse "$i" $INX
			    INX=$2
			fi
		elif [ -f "$i" ]; then
			if [ $(basename ./${0##*/}) != $(basename $i) ]; then
			    printfill "$(basename $i)" $INX
				echo "mput ${i}" >> $MPF_FILE
			fi
		fi
	done
}

echo ""

echo "[FILES STRUCTURE]"
rm $MPF_FILE && recurse . 0

echo ""

echo "[LOGS]"
echo "open $TTY
$(cat $MPF_FILE)" > $MPF_FILE

echo ": $MPF_FILE created"
cat $MPF_FILE

git pull
echo ": git pull finished"

sudo mpfshell -s $MPF_FILE
echo ": upload completed"

rm $MPF_FILE
echo ": mpf file deleted"

echo ""
echo "Have fun!"
echo ""

