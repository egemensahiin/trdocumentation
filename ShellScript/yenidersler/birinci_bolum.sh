#!/bin/bash

# Exc 4
if [ -f "/etc/shadow" ]
then
	echo "Shadow password devrede."
	if [ -w "/etc/shadow" ]
	then
		echo "/etc/shadow icin izinleriniz var."
	else
		echo "/etc/shadow icin izinleriniz yok."
	fi
fi

echo

# Exc 5
LISTE="man bear pig dog cat sheep cattle"
for i in $LISTE
do
	echo $i
done
