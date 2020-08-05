#!/bin/bash

# bu scriptte netstat komutunu awk komutu ile pipelayarak, acik port numaralarini goruyoruz.
netstat -nutl ${1} | grep -Ev '^Active|^Proto' | awk '{print $4}' | awk -F ':' '{print $NF}'
