#!/bin/bash

# Root kontrolu:
if [[ "${UID}" -ne 0 ]]
then
	echo "Kullanici olusturulamadi! Bu islemi yalnizca root gerceklestirebilir."
	exit 1
fi

# Syntax kontrolu:
if [[ "${#}" -lt 1 ]]
then
	echo "Bir seyler eksik!"
	echo "Kullanilis: ${0} KULLANICI_ADI [GERCEK_ADI]"
	echo "Lokal sistemde GERCEK_ADI kisisi icin KULLANICI_ADI adinda bir hesap olusturur."
	exit 1
fi

# Her sey dogru ise argumanlari atayalim:
KULLANICI_ADI="${1}"
shift
GERCEK_ADI="${*}"

# Sonra parolayi olusturup PAROLA degiskenine kaydedelim. Degiskenleri basta atamak daha okunur olmasini saglar:
OZEL_KARAKTER="$(echo '!^+%?$#[]{}()=?_-|<>' | fold -w1 | shuf | head -c1)"
PAROLA="$(date +%s%N | sha256sum | head -c11)${OZEL_KARAKTER}"

# Simdi de kullaniciyi olusturalim:
useradd -c "${GERCEK_ADI}" -m ${KULLANICI_ADI}
if [[ "${?}" -ne 0 ]]
then
	echo "Bir terslik var! Kullanici olusturulamadi."
	exit 1
fi

# Eger kullanici olustuysa parolayi bu kullaniciya tanimlayalim:
echo "$PAROLA" | passwd --stdin ${KULLANICI_ADI}
if [[ "${?}" -ne 0 ]]
then
	echo "Bir seyler ters gitti! Kullaniciya parola atanamadi."
	exit 1
fi

passwd -e ${KULLANICI_ADI}

# Olusturulan kullanicinin bilgilerini verelim:
echo
echo "Kullanici basariyla olusturuldu!"
echo "--------------------------------"
echo "Kullanici adi: ${KULLANICI_ADI}"
echo "Kullanici sahibi: ${GERCEK_ADI}"
echo "Host adi: ${HOSTNAME}"
echo "Parola: ${PAROLA}"
exit 0
