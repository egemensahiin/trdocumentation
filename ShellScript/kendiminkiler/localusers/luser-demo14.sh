#!/bin/bash

LOGFILE="${1}"

if [[ ! -e "${LOGFILE}" ]]
then
  echo "${LOGFILE} dosyasi bulunamadi!" >&2
  exit 1
fi

cut -d '"' -f 2 "${LOGFILE}" | cut -d " " -f 2 | sort | uniq -c | sort -n | tail -3
