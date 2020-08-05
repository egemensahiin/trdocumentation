#!/bin/bash

# kullanicinin UID ve kullanici adini gosterecek
# kullanicinin vagrant kullanici olup olmadigini gosterecek

# UID'yi yazdir
echo "Kullanici id'niz: ${UID}"

# sadece uid 1000 degil ise yazdir
TEST_EDILECEK_UID='1000' # kodlamada onemli bir konsept, tekrar tekrar kullanilacak degerlerin degiskenlere atanmasidir. gereksiz ve daha uzunmus gibi dursa da scripti baska bir kullaniciyi
			 # test edecek sekilde degistirmek istedigimizde mesela sadece bu degiskeni degistirmemiz yeterli olacaktir, tek tek id'leri degistirmemize gerek kalmaz.
if [[ "${UID}" -ne "${TEST_EDILECEK_UID}" ]] # -ne, aritmetik testlerde esit degildir anlamindadir.
then
  echo "UID'niz $TEST_EDILECEK_UID degildir."
  exit 1 # basarili bir sekilde sonlanan bir programin exit durumu 0'dir. basarisiz bir programin ise exit durumu "0 olmayan" bir degerdir ki genelde 1 kullanilmasina karsin diger herhangi bir
fi       # sayi da gecerlidir. scriptlerde 0 dogrudur diger sayilarsa yanlistir. burada exit durumunu 1 yapiyoruz yani UID 1000 degilse programin kalan kismini calistirmiyoruz. manual sayfa-
	 # larinda programlarin ve komutlarin cikis durumlarini ve ne anlama geldiklerini gormek mumkundur. scriptlerde kullanilacak komutlarin exit durumlarina bakilarak bunlar scriptlerde
	 # test edilebilir.

# kullanici adini yazdir
KULLANICI_ADI=$(id -un)

# komutun basarili olup olmadigini test et
if [[ "${?}" -ne 0 ]] # soru isareti, en son calistirilan komutun exit durumunu tutan ozel bir degikendir. burada en son calistirilan komut "id -un" komutudur. komutun basarili olup olmadigini
then		      # exit durumu 0 ise basarili degil ise basarisizdir.
  echo 'id komutu basarili sekilde calismadi!'
  exit 1
fi
echo "Kullanici adiniz ${KULLANICI_ADI}." # eger if blogu calismazsa yani id komutunun exit durumu eq 0 ise kullanici adini yazdiriyoruz.

# string icin kosullari test edebiliriz.
TEST_KULLANICI_ADI='vagrant'
if [[ "${KULLANICI_ADI}" = "${TEST_KULLANICI_ADI}" ]] # stringlerin test edilmesinde operator olarak semboller kullanilir. sayilarda ise kisaltmalar kullanilir.
then
  echo "Kullanici adiniz ${TEST_KULLANICI_ADI} ile aynidir."
fi

# stringlerde esit olmamanin testi
if [[ "${KULLANICI_ADI}" != "${TEST_KULLANICI_ADI}" ]]
then
  echo "Kullanici adiniz ${TEST_KULLANICI_ADI} degildir."
  exit 1
fi

exit 0 # belirtilmezse genellikle en son komutun exit durumu olarak cikar.
