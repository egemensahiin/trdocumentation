#!/bin/bash

read -p "Dosya ismini giriniz: " DOSYA

if [ -d $DOSYA ]
then
	echo "$DOSYA bir klasördür."
	ls -l $DOSYA
elif [ -f $DOSYA ]
then
	echo "$DOSYA normal bir dosyadır."
	ls -l $DOSYA
elif [ -e $DOSYA ]
then
	echo "$DOSYA farklı bir tip dosyadır."
	ls -l $DOSYA
fi
