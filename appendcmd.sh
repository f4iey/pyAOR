#!/bin/zsh
#
# Interactive CLI to quickly add multiple instances of AOR DV commands
#

while [[ 1 ]];
do
	echo "Name: "
	read n
	echo -e "\nParameter (leave blank if none): "
	read p
	echo -e "\nDescription (mandatory): "
	read d
	N=$(sed -e 's/\(.*\)/\L\1/' <<< "$n")
	echo "\t\t$N = Command(\"$n\", \"\", \"$d\")\n" >> ./Commands.py
done
