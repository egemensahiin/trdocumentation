#!/bin/bash

# Root kontrolu
if [[ "${UID}" -ne 0 ]]
then
  echo "Kullanici olusturulamadi! Bu programi yalnizca yonetici olarak calistirabilirsiniz." >&2
  exit 1
fi

# Syntax kontrolu
if [[ "${#}" -lt 1 ]]
then
  echo "Kullanici olusturulamadi! Arguman eksik." >&2
  echo "Kullanilis: ${0} KULLANICI_ADI [HESAP_SAHIBI]..." >&2
  exit 1
fi

# Kullanici adi, comment ve parola atanmasi
KULLANICI_ADI="${1}"
shift
HESAP_SAHIBI="${*}"
PAROLA="$(date +%s%N | sha256sum | head -c15)"

# Hesap olusturulmasi
useradd -c "${HESAP_ADI}" -m "${KULLANICI_ADI}" &> /dev/null

# Kullanici kontrolu
if [[ "${?}" -ne 0 ]]
then
  echo "Kullanici olusturulamadi! Bir hata olustu." >&2
  exit 1
fi

# Parola olusturulmasi
echo "${PAROLA}" | passwd --stdin "${KULLANICI_ADI}" &> /dev/null

# Parolanin kontrolu
if [[ "${?}" -ne 0 ]]
then
  PAROLA="KULLANICIYA PAROLA ATANAMADI!"
fi

# Ilk giriste parola yenilemeye zorla
passwd -e "${KULLANICI_ADI}" &> /dev/null

# Olusturulan kullanicinin bildirilmesi
echo "---------------------"
echo "Kullanici adi: ${KULLANICI_ADI}"
echo "Host adi: ${HOSTNAME}"
echo "Parola: ${PAROLA}"
exit 0
