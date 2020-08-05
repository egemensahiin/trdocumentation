#!/bin/bash

# komut satirinda yazilanlari pozisyonel parametrelerle cagirip bunlari for dongusunde kullanarak verilen kullanici adlarina rastgele sifreler atayacagiz. bunun icin pozisyonel parametrelerden
# faydalanacagiz. pozisyonel parametreler atanamaz fakat bazi ozel parametrelerle cagrilabilir. bunlari bash man sayfasinda Special Parameters bolumunde bulmak mumkundur.

# ozel parametreler, degiskenlerle ayni syntaxla cagirilir. 0, calistirilan scripti kaydeder. yani bir yerde 0. pozisyon diyebiliriz buna. 0'ı dirname komutuyla cagirirsak scriptin konumunu
# basename komutu ile ise adini yazdirabiliriz. bu iki komut basit calisir, en son backslashten sonrasini basename, oncesini dirname olarak alirlar; ls gibi aslinda olmayan bir dosya yazildi-
# ginda uyari vermez.

# Bash'te calistirilan scripti yazdiralim:
echo "${0} calistiriliyor."
echo "$(dirname ${0}) konumunda $(basename ${0}) scripti calisiyor."

# Ozel parametrelerden biri de #'tir ve komuta girilen argumanlarin sayisini verir. programin 1'den daha az arguman kabul etmesini istemiyoruz. bu yuzden bir if kosulu kuruyoruz:
if [[ "${#}" -lt 1 ]]
then
  echo "Kullanilis: ${0} KULLANICI_ADI [KULLANICI_ADI]..." # yani bir kullanici adi olmak zorunda, kalani opsiyonel ama istendigi kadar olabilir.
  exit 1
fi

# Simdi verilen her parametreye bir sifre atayacak ve bunu yazdiracagiz. bunun icin for dongusu kullanmamiz lazim. syntaxi help sayfasinda gorulebilir. bir dizi argumani veya parametreyi
# teker teker cagirmak icin kullanilir. for dongusunu, scripte verilen parametrelerle beslemek icin baska bir ozel parametreden faydalanilir. @ parametresi cagirildiginda tek tek 1., 2. ..
# tum pozisyonel parametreleri cagirir. bash manualinde benzeri bir parametre olarak * goze carpar fakat farkli olarak * tum pozisyonel parametreleri yan yana tek bir string olarak cagirir.
# onemli bir nokta; a b c d, 4 farkli pozisyonel parametre belirtirken a "b c" d, 3 adet pozisyonel parametre belirtir. for dongusu syntaxi: for ISIM [in KELIMELER]; do KOMUTLAR; done
for KULLANICI_ADI in "${@}"
do
  PAROLA="$(date +%s%N | sha256sum | head -c32)"
  echo "${KULLANICI_ADI}: ${PAROLA}"
done

exit 0
