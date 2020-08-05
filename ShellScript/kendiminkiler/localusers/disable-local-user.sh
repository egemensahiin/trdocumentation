# Fonksiyonlar
kullanilis() {
  echo "Verilen kullanicilari askiya alir."
  echo "Kullanilis: ${0} [-dra] KULLANICI [KULLANICI] ..." >&2
  echo "    -d: Kullaniciyi tamamen kaldirir." >&2
  echo "    -r: Kullanicinin klasorunu kaldirir." >&2
  echo "    -a: Kullanicinin verilerini arsivler." >&2
  exit 1
}

hata() {
  if [[ "$?" -ne 0 ]]
  then
    echo "${1}" >&2
    exit 1
  fi
}

# atamalar
ARSIV_DIR='/arsiv'

# Root kontrolu
if [[ "$UID" -ne 0 ]]
then
  echo "Yalnizca sudo ile veya root kullanici olarak kullanilabilir." >&2
  exit 1
fi

# Seceneklerin tanimlanmasi
while getopts dra OPTION
do
  case ${OPTION} in
    d) KULLANICI_SIL='true' ;;
    r) SILME_SECENEGI='-r' ;;
    a) ARSIVLE='true' ;;
    ?) kullanilis ;;
  esac
done

# Komut satiri argumanlarindan opsiyonlari kaldiralim
shift $(( OPTIND - 1 ))
if [[ "$#" -lt 1 ]]
then
  kullanilis
fi

# simdi zurnanin zart dedigi yer
# While dongusuyle tum argumanlari tek tek isleyelim. aynisi for ile de yapilabilir. bu durumda for KULLANICI in "${@}" şeklinde olur.
while [[ "$#" -gt 0 ]]
do
  KULLANICI="${1}"
  echo "${KULLANICI} isleniyor..."
  
  # Kullanicinin normal bir kullanici oldugundan emin olmak icin UID kontrolu. (999'dan buyuk olmalidir.)
  KULLANICI_ID="$(id -u $KULLANICI)"
  if [[ "${KULLANICI_ID}" -lt 1000 ]]
  then
    echo "${KULLANICI_ID} id numarali kullanici $KULLANICI silinemiyor." >&2
    exit 1
  fi
  
  # Simdi once arsiv kontrolu. klasor var mi yok mu?
  if [[ "${ARSIVLE}" = 'true' ]]
  then
    if [[ ! -d "${ARSIV_DIR}" ]] #---> -d eger bu bir klasor ise demek. ! -d ise eger bu bir klasor degilse demek
    then
      echo "${ARSIV_DIR} olusturuluyor..."
      mkdir -p ${ARSIV_DIR} #---> -p opsiyonu, eger ARSIV_DIR degiskenini degistirirsek ve /klasor/klasor2 seklinde olursa diye
      hata "Arsiv klasoru ${ARSIV_DIR} olusturulamadi."
    fi
    # Arsiv klasoru varsa veya olusturulduysa:
    HOME_DIR="/home/${KULLANICI}"
    # Kullanicinin home'u olup olmadigina bakalim
    if [[ ! -d "${HOME_DIR}" ]]
    then
      echo "${KULLANICI} kullanicisinin bir home klasoru yoktur."
      exit 1
    else # Eger home klasoru varsa:
      # arsivleyelim.
      ARSIV_DOSYA="${ARSIV_DIR}/${KULLANICI}.tar.gz"
      echo "${HOME_DIR}, ${ARSIV_DOSYA} olarak arsivleniyor..."
      tar -zcf ${ARSIV_DOSYA} ${HOME_DIR} &>/dev/null
      hata "${HOME_DIR} klasoru arsivlenemedi!"
      echo "${HOME_DIR} arsivlendi."
    fi
  fi #--> ARSIV BITTI
  
  # Kullanici silme opsiyonunun kontrolu kontrolleri
  if [[ "${KULLANICI_SIL}" = 'true' ]]
  then
    userdel ${SILME_SECENEGI} ${KULLANICI}
    hata "${KULLANICI} silinemedi." >&2
    echo "${KULLANICI} basariyla silindi."
  else
    # chage ile home dir silmiyoruz!
    chage -E 0 ${KULLANICI}
    hata "${KULLANICI} askiya alinamadi."
    echo "${KULLANICI} askiya alindi."
  fi
  shift
done

exit 0
