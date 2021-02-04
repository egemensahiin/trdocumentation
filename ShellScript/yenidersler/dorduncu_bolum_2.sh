#!/bin/bash

file_count() {
	local COUNT=$(ls $@ | wc -l)
	if [ $? -eq 0 ]
	then
		echo "${@}:"
		echo "$COUNT"
	else
		echo "Bir problem çıktı..."
		return 1
	fi
}

file_count $@
