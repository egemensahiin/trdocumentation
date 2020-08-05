#!/bin/bash
#
# Script, verilen serverların acik olup olmadigini kontrol ediyor:
#
SERVERLAR=/vagrant/servers

if [[ ! -e "${SERVERLAR}" ]]
then
  echo "${SERVERLAR} bulunamadi." >&2
  exit 1
fi

for SERVER in $(cat ${SERVERLAR})
do
  echo "${SERVER} ping'leniyor..."
  ping -c 1 ${SERVER} > /dev/null
  if [[ "$?" -ne 0 ]]
  then
    echo "${SERVER}'a ulasilamiyor."
  else
    echo "${SERVER} acik."
  fi
done
  
