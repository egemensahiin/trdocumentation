#!/bin/bash

# bu scriptle kullanici olusturacagiz. kullanici adi ve sifreyi promptan girecegiz.
# promptan kullanici tarafindan veri girilmesi icin builtin komutlardan biri olan read kullanilir. diger metodlari daha sonra isleyecegiz. read, standart inputu satirini okur. istersek bunu bir
# degiskene kaydedebiliriz. -p secenegi ile yazma islemini bir prompttan sonra da yapabiliriz ki bence daha kullanisli. normal syntax read DEGISKEN seklindedir. prompt secenegitle beraber
# read -p 'prompt' DEGISKEN seklindedir.

# kullanici eklemek icinde useradd komutu calistirilir. useradd komutu ile birlikte bir kullanici adi girilmelidir (man sayfasinda LOGIN ile belirtilir.)
# kullanici adlariyla ilgili onemli uc nokta var: buyuk-kucuk harf duyarliligi, ozel karakter kabul edilmemesi ve 8 harf siniri. kullanici adi 8 harften uzun oldugunda bazi eski komutlarin
# ciktilarinda kullanici adinin yalniz ilk yedi karakteri ve bir + isareti yazilmaktadir.

# useradd komutu eklenen kullaniciya sifre atamaz. kullanicilara sifre atamak icin passwd komutu kullanilir. passwd komutu normalde prompt araciligiyla komut satirindan veri alir fakat
# --stdin secenegi kullanilarak passwd komutunun standart input kabul etmesi saglanabilmektedir. bir standart input olusturmak icin pipeline kullanacagiz. PAROLA degiskenini echo komutuyla
# cagiracagiz ki bu komut sonucu stdin olarak soz konusu parola cikacak. bunu da passwd komutuna --stdin secenegiyle birlikte pipeladigimizda parolayi input olarak alacak.

# kullanici adini sor
read -p 'Kullanici adini giriniz: ' KULLANICI_ADI
# gercek adini sor
read -p 'Kullanicinin gercek adini giriniz: ' GERCEK # useradd man sayfasinda -c opsiyonunda aciklanmaktadir ve bu opsiyonla eklenir. COMMENT, kullanicinin gercek adini icerir.

# sifreyi sor
read -p 'Parola giriniz: ' PAROLA

# kullaniciyi olustur
useradd -c "${GERCEK}" -m ${KULLANICI_ADI}
	# COMMENT eklemek icin -c opsiyonunu, home klasoru olusturulmasına zorlamak icinse -m opsiyonunu verdik. COMMENT'i atarken "" kullanmamizin sebebi, bosluk kullanilmasi durumunda butu
	# butun bir string olarak degerlendirilmesini saglamak.

# sifreyi ayarla
echo "$PAROLA" | passwd --stdin ${KULLANICI_ADI}

# ilk giriste sifreyi degismeye zorla
passwd -e ${KULLANICI_ADI} # -e (expire) opsiyonu kullaniciyi ilk giriste parola degistirmeye zorlar. kullanici ilk parolayi belirlerken parola gorulmektedir fakat bu sekilde parolayi
			   # degistirterek parolanin daha gizli olmasini sagliyoruz.
