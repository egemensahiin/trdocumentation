#!/bin/bash

# bu script kullanici kimligi ve kullanici adini yazdiracak
# ardindan kullanicinin root olup olmadigini yazdiracak.

# pseudocode teknigi: önce scriptin neler yapmasini istiyoruz onlari belitip daha sonra bunlarin altina kodlarin yazilmas

# UID'yi yazdiralim
echo "Kullanici id'niz: ${UID}"
	# UID degiskeni bash'te onceden tanimli bir degiskendir. bu tip onceden tanimli (preset) degiskenlerin manual sayfalari mevcuttur.
	# bash icin manual sayfasinda (man bash) bu preset degiskenleri bulmak mumkundur. UID, mevcut kullanicinin id'sini verirken benzeri bir degisken olan EUID etkin kullanicinin id'sini
	# verir. bunlara shell degiskenleri denir ve sadece okunabilen degiskenlerdir, yazilabilir yani degistirilebilir degildir. komut satirina UID="1001" gibi bir sey yazarsak cikti olarak
	# hata aliriz.

# kullanici adi yazdiralim
	# komut satirinda kullanici adini yazdirmanin iki farkli yolu vardir bunlardan ilki id komutudur ki bu komut tek basina cikti olarak kullanici id'si (uid), grup id'si (gid) ve
	# gruplari, ayrica bunlarin isimlerini parantez icinde cikti olarak verir. -u secenegi "user" -n secenegi ise "name" icin kullanilir ve sonucta id -un (veya -nu veya -u -n veya -n -u)
	# cikti olarak mevcut kullanicinin adini cikti olarak verir.
	# diger bir secenek "whoami" komutudur ki dogrudan man sayfasindaki tanimiyla "id -un" komutuyla ayni seydir.
	# onca bir degiskene kullanici adini kaydediyoruz. scriptingde bir terminal komutunun ciktisini bir degiskene atarken $(komut) syntaxi kullanilir.
KULLANICI_ADI=$(id -un)
echo "Kullanici adiniz ${KULLANICI_ADI}"
# veya
KULLANICI_ADI=$(whoami)
echo "Kullanici adiniz ${KULLANICI_ADI}"
	# $(komut) syntaxinin bir alternatifi olarak `komut`(bu isaret ALT GR+,) syntaxi da kullanilabilmektedir fakat sahsi olarak fikrim $(komut)'un okunurlugunun daha iyi oldugu
KULANICI_ADI=`id -un`
echo "Kullanici adiniz ${KULLANICI_ADI}"

# root olup olup olmadigini yazdiralim
	# burada bir if ifadesi kullanilacak. if syntaxi scriptingde asagidaki gibidir (if [[ifade]]; then; tab komut; else; tab komut; fi). esitlik icin -eq kullanilir. root icin kullanici
	# id'si 0 oldugu icin eger UID = 0 ise yani kullanici root ise echo "Root kullanicisiniz!", degilse echo "Root kullanici degilsiniz!" ciktisi alacagiz. aslinda uid kullanmak zorunda
	# degiliz daha once tanimladigimiz KULLANICI_ADI degiskeni uzerinden de kontrol edebiliriz ama UID tum linux sistemlerde root kullanici icin 0'dir yani bu sekliyle script tum linux
	# sistemlerde ayni sekilde calisacaktir.
if [[ "${UID}" -eq 0 ]] # bosluklar onemli, bunlar olmadigi zaman hata alinir. ayrica if ifadesinde cagirilan degiskenin syntaxina da dikkat; degiskenleri cagirirken hep "" kullaniyoruz
then		    # eger braket kullanmiyorsak "" kullanmaya gerek yok yani if [[ $UID ]], if [[ "$UID" ]] ve if [[ "${UID}" ]] ayni seydir. [[ yerine [ da kullanilabilir ama [[ daha yeni
	echo "Root kullanicisiniz!" # bir syntaxtir. 
else # aslinda tab veya bosluklar gerekli degil, sayisi da onemli degil ama okunurluk acisindan bence olmazsa olmaz.
	echo "Root kullanici degilsiniz!"
fi
