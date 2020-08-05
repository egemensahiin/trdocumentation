#!/bin/bash

# Kullaniciyi kontrol et. Root degilse sonlandir.
if [[ "${UID}" -ne 0 ]]
then
  echo 'Bu islemi yalnica root kullanici ile gerceklestirebilirsiniz!'
  exit 1
fi
# Prompttan kullanici adini, kullanan kisinin adini ve parolayi ata.
read -p 'Adinizi giriniz: ' GERCEK
read -p 'Kullanici adi giriniz: ' KULLANICI_ADI
read -p 'Parola giriniz: ' PAROLA
# Kullaniciyi olustur. Eger bir hata soz konusu ise sonlandir.
# Kullanicinin gercek adi da atanacagi icin -c opsiyonu, home olusturmak icin -m opsiyonu:
useradd -c "${GERCEK}" -m ${KULLANICI_ADI}
if [[ "${?}" -ne 0 ]]
then
  echo "Bir hata olustu! Kullanici olusturulamadi."
  exit 1
fi
# Parolayi kaydet.
echo "${PAROLA}" | passwd --stdin ${KULLANICI_ADI}
if [[ "${?}" -ne 0 ]]
then
  echo "Hata olustu! Sifre atanamasdÄ."
  exit 1
fi
# Kullanici bu parolayi ilk girisinde degistirsin
passwd -e ${KULLANICI_ADI}
echo # bir bosluk olsun diye
# Kullanicinin kim oldugunu, hangi hosta bagli oldugunu, kullanici adini ve parolasini yazdir.
echo "Kullanici : ${GERCEK}"
echo "Host: ${HOSTNAME}" # builtin bir degisken!
echo "Kullanici adi: ${KULLANICI_ADI}"
echo "Parola: ${PAROLA}"
exit 0
