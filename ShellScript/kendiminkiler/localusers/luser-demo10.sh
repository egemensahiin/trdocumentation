#!/bin/bash

# fonksiyonlar, programda siklikla kullanilan kodlari tekrarlarken veya ic ice bir cok is yapan bir program yazarken bize kolaylik saglar. fonksiyonlar kullanilarak hazirlanan kodlara
# dry kod denmektedir yani "don't repeat yourself". fonksiyonlar kullanilmadan kodlari tekrarlayarak yazilan kodlara "we enjoy typing" manasinda wet denmektedir.

# fonksiyonlarin syntaxi: function isim { KOMUTLAR ; } veya isim() { KOMUTLAR ; }

# bir log fonksiyonu yazalim. yalnizca fonksiyonun calistirildigini yazdirsin:

# log(){
#   echo 'log fonksiyonunu cagirdiniz!'
# }

# veya

function log {
  echo 'log fonksiyonunu cagirdiniz!'
}

# simdi de fonksiyonu cagiralim:
log

# fonksiyonlar icin ozel bir komut soz konusudur. local komutu yalnizca fonksiyon bloklarinda calistirilabilir ve local ile tanimlanan bir degisken yalnizca o fonksiyonda mevcuttur, fonk-
# siyonun disinda o fonksiyon yoktur.
function log_goruntule {
  local MESAJ="$@" # '@' bir shell degiskeni unutma! bütün pozisyonel parametreleri cagirir.
  echo "${MESAJ}"
}

log_goruntule 'Merhaba!'
log_goruntule 'Script yazayrik daa.'
# MESAJ degiskeni sadece fonksiyon icersinde tanimlidir. fonksiyon disinde cagirildiginda en son atanan deger yani 'Script yazayrik daa.' yi goremeyecegiz, boyle bir degisken tanimlanmadigi
# icin sadece bir bosluk olacak
echo "${MESAJ}"

# fonksiyon icersinde local komutuyla degil de normal syntaxla bir degisken tanimladigimizda normal global bir degisken olur ve bunu fonksiyon disinda da cagirabiliriz.
deneme(){
  GORUNTU="$*"
  echo "${GORUNTU}"
}

deneme 'Deneme fonksiyonu'
deneme 'olmasi gerektigi gibi calisiyor!'

echo "${GORUNTU}"

# fonksiyonlarda kosullu ifadeler de kullanabiliriz:
function log_kosul {
  local MESAJ="$@"
  if [[ "${KONTROL}" = 'true' ]]
  then
    echo "${MESAJ}"
  fi
}

log_kosul 'Burasi yazilmayacak :(' # su an ortada bir KONTROL degiskeni yok o yuzden bu fonksiyondan bir cikti alinmayacak
KONTROL='true'
log_kosul 'Burasi yazilacak!!'

# global degiskenlerdense local degiskenler daha kullanislidir cunku nerede neye karsilik geldikleri daha tahmin edilebilirdir. bunun icin KONTROL_LOCAL degiskenini local olarak tanim-
# layip fonksiyona verilen ilk parametreyi kontrol, kalan kismi ise arguman olarak ayarlayabiliriz:
function log_kosul_local {
  local KONTROL_LOCAL="${1}"
  shift
  local MESAJ="${@}"
  if [[ "${KONTROL_LOCAL}" = 'true' ]]
  then
    echo "${MESAJ}"
  fi
}

log_kosul_local 'true' 'Burasi yazilacak!!'
log_kosul_local 'false' 'Ama burasi yazilmayacak :('
# bu sekildeki bir syntaxta global bir degiskenin kullanimi da mumkundur.
DOGRULUK='true'
log_kosul_local "${DOGRULUK}" 'Burasi da yazilacak!!'

# global degiskenlerle birlikte readonly komutu kullanilabilmektedir. readonly komutu daha once tanimlanmis bir degisken ile kullanilabilecegi gibi readonly ile birlikte de degisken tanim-
# lanabilir. bu degiskenin degeri script icersinde hicbir kosulda degismez.
readonly DOGRULUK_RO='true'
log_ro(){
  local MESAJ="${@}"
#  DOGRULUK_RO='false' # burda yorumu kaldirip degiskeni degistirmeye calistigimizda hata alacagiz
  if [[ "$DOGRULUK_RO" = 'true' ]]
  then
    echo "$MESAJ"
  fi
}
# DOGRULUK_RO='false' # fonksiyon disinda da degistiremeyiz, bu satirda da yorum kalkinca hata alinir.

log_ro 'Burasi yazilacak!!'

# logger fonksiyonu, verilen bir mesaji, tarih saat ve tag (yazdiran) bilgisiyle birlikte syslog'a yazdiran bir programdir. logger MESAJ syntaxiyla calisir ve default olarak /var/log/messages
# dosyasina kaydedilir. simdi bu sekilde calisan bir script yazalim; verilen mesaji scriptin adiyla beraber kaydetsin. bunu yapmak icin logger ile beraber --tag veya -t opsiyonu da kullanil-
# malidir. -t opsiyonu, mesaji kimin gonderdigini belirtir. tag olarak $0 kullandigimizda scriptin adini (0. pozisyonal parametre!) girmis oluruz.
log_logger(){
  # bu fonksiyon syslog'a ve eger DOGRULUK_LOC dogru ise standart output'a mesaj gondermektedir.
  local TAG=$(basename "$0")
  local DOGRULUK_LOC="$1"
  shift
  local MESAJ="$@"
  if [[ "$DOGRULUK_LOC" = 'true' ]]
  then
    echo "$MESAJ"
  fi
  logger -t "$TAG" "$MESAJ"
}

log_logger 'true' 'Merhaba'
log_logger 'false' 'Burasi ekranda gozukmeyecek ama log mesaji olarak kaydedilecek.'

echo '-------------'
# simdi, verilen dosyanin yedegini olusturan bir fonksiyon yazalim:
backup_olustur(){
  # dosyayi tanimlayalim
  local DOSYA="$1"
  # once dosyanin olup olmadigini kontrol edelim
  if [[ -f "${DOSYA}" ]] # yani soz konusu dosya var ise. -f secenegini simdilik bilmiyorum :/
  then
    # dosyayi kopyalanmis dosyanin adini tanimlayalim cp komutuna tanimlamak icin:
    local YEDEK="/var/tmp/$(basename ${DOSYA}).$(date +%F-%N)" # uzantisi gunun tarihi ve rastgele bir sayi olarak nanosaniye olacak. %F full tarih %N nanosaniye
    # /var/tmp konumundaki dosyalar CentOS7'de 30 gun sonra siliniyor.
    # simdi kopyayi olusturalim
    cp -p "${DOSYA}" "${YEDEK}"
    log_logger 'true' "${DOSYA} basariyla ${YEDEK} olarak kopyalandi"
  else
    return 1 # fonksiyonlarda exit durumunun ayarlanmasi icin exit degil return komutu kullanilir. return exitin local versiyonudur, programi degil fonksiyonu sonlandirir.
  fi
}

# simdi /etc/passwd un backup'ini olusturalim
backup_olustur '/etc/passwd'

# basari durumunu ise bunu syslog'a ve ekrana yazdiralim
if [[ "${?}" -eq 0 ]] # burada exit durumu, fonksiyondan geliyor
then
  log_logger 'true' 'Yedekleme basarili!'
else
  log_logger 'true' 'Yedekleme basarisiz :('
  exit 1
fi
