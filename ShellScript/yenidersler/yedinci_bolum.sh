#!/bin/bash

# nullglob ayarlanmadiğinda cp komutu, arguman olarak "*.jpg"
# string'ini alır ama ayarladigimizda, bos olan wildcard'lar
# string degil null yani bos olur ve cp komutu calismaz.
shopt -s nullglob

bulunan=0

for i in *.jpg
do
	cp $i $(date +%Y%m%d)${i}
	bulunan=$((bulunan + 1))
done

if [[ bulunan -eq 0 ]]
then
	echo "Hic jpg dosyasi bulunamadi!"
fi

#shopt -u nullglob
