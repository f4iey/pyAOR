#!/bin/zsh
#
# Interactive CLI to quickly add multiple instances of AOR DV commands
#

while 1
do
	echo "Name: "
	read n
	echo -e "\nParameter (leave blank if none): "
	read p
	echo -e "\nResult Codes (leave blank if default): "
	read r
	while [[ -n -z $r ]] do
		echo


done
