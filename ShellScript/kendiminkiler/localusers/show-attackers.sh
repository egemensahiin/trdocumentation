#!/bin/bash

# Degiskenler
LOGFILE="${1}"
LIMIT=10

# Yanlis kullanilista uyar.
if [[ "${#}" -eq 0 ]]
then
  echo "Bir seyler eksik!" >&2
  echo "Kullanilis: ${0} LOGFILE" >&2
  exit 1
fi

# Baslik
echo "Sayi,IP,Konum"

# LOGFILE degiskeni olustur ve dosyanın varlıgını kontrol et
if [[ ! -e "$LOGFILE" ]]
then
  echo "$LOGFILE bulunamadi!" >&2
  exit 1
fi

grep Failed ${LOGFILE} | awk '{print $(NF - 3)}' | sort | uniq -c | sort -nr | while read SAYI IP
do
  if [[ "$SAYI" -gt "$LIMIT" ]]
  then
    echo "${SAYI},${IP},$(geoiplookup ${IP} | awk -F ", " '{print $2}')"
  fi
done
exit 0
