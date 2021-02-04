#!/bin/bash

file_count() {
	local COUNT=$(ls | wc -l)
	if [ $? -eq 0 ]
	then
		echo "Mevcut dizinde $COUNT dosya var."
	else
		echo "Bir problem çıktı..."
		return 1
	fi
}

file_count
