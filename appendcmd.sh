#!/bin/zsh
#
# Interactive CLI to quickly add multiple instances of AOR DV commands
#

while [[ 1 ]];
do
	echo "Name: "
	read n
	echo -e "\nDescription (mandatory): "
	read d
	N=$(sed -e 's/\(.*\)/\L\1/' <<< "$n")
	echo "        $N = Command(\"$n\", \"\", \"$d\")" >> ./Commands.py
done
