#!/bin/bash

# scriptlerimize opsiyon atamak icin "getopts" kullanilir. getopts, while dongusunde kullanilan bir fonksiyon olup syntaxi getopts OPTSTRING NAME [ARG] seklindedir. getopts, while dongusunde
# kullanilir; kullanicinin girdigi opsiyon tanimli ise exit durumu 0, tanimli degilse 0 degildir. simdi parola ureten bir scriptte ornegini gorelim:

# scriptimiz, urettigi parolalar icin 3 secenek kabul edecek:
# -l secenegi parolanin uzunlugunu degistirmek icin (default mesela)
# -s secenegi sifreye ozel karakter de eklemek icin
# -v secenegi ise ciktinin daha detayli olmasi icin

# detay_acik fonksiyonu detayli modun kullanimini kontrol eder ve aciksa yazilacak mesaji tanimlar
detay_acik() {
  local MESAJ="${@}" # yani fonksiyondan sonra yazilan hersey
  if [[ "$DETAY" = 'true' ]]
  then
    echo "$MESAJ"
  fi
}

# gecersiz secenek girilmesi durumunda yazdirilicak kullanilis bilgisi:
kullanilis() { 
  echo "Gecersiz bir secenek veya arguman girdiniz." >&2
  echo "Kullanilis: ${0} [-vs] [-l UZUNLUK]" >&2
  echo "Program rastgele bir parola uretir." >&2
  echo "  -l UZUNLUK Uretilen parolanin uzunlugunu belirler." >&2
  echo "  -s         Parolaya ozel karakterler ekler." >&2
  echo "  -v         Detayli cikti verir." >&2
  exit 1
}

# uzunluk icin default deger tanimladik.
UZUNLUK=48 
while getopts vl:s OPTION # ":", secenekten sonra arguman kabul ettigini belirtiyor. l seceneginden sonra verilen arguman stringin uzunlunu belirler.
do
  case ${OPTION} in # opsiyonlari tanimlamak ve opsiyonlarin islev gormesini saglamak icin case ifadesi kullaniriz.
    v)
      DETAY='true'
      echo "Detayli mod acik." # burayi da detay_acik fonksiyonuyla yazabilirdik ama gerek yok bence. ama oyle yapinca daha okunakli da olabilir.
      ;;
    s)
      OZEL_KARAKTER_KULLAN='true'
      ;;
    l)
      UZUNLUK=${OPTARG} # OPTARG, builtin bir degiskendir ve opsiyon argumani anlamina gelir.
      ;;
    ?) # herhangi bir tek karakter ile pattern matching yapar. opsiyonlarimiz tek karakterli oldugu icin ? yeterli yani secenekler disinda herhangi bir karakterde uyari verecek.
      kullanilis # case ifadesinin daha okunur olmasi icin buraya ekleyecegimiz kullanilisi bir fonksiyona tanimlamak daha mantikli. fonksiyonlari okunurluk acisindan en uste yaziyoruz.
      ;;
  esac
done

# # simdi bu programin pozisyonel arguman kabul ettigini dusunelim. opsiyonlardan sonra girdigimiz bir argumanin pozisyonu ne olacaktir?
# # bunun icin shell degiskenleriyle ve getopts'un ayarladigi bir degiskene bi bakalim. OPTIND, opsiyonlardan sonra gelen komut satiri argumaninin pozisyonunu verir.
# echo "Toplam arguman sayisi: ${#}"
# echo "Tum argumanlar: ${@}"
# echo "Ilk arguman: ${1}"
# echo "Ikinci arguman: ${2}"
# echo "Ucuncu arguman: ${3}"
# echo "OPTIND: ${OPTIND}"
# # programi calistirince gorulebilecegi gibi OPTIND esasinda programa verilen komut satiri argumaninin pozisyonunu verir. diyelim OPTIND degeri 3 cikti. bu durumda opsiyonlari komut satiri
# # argumanlarindan kaldirmak icin shift komutunu kullanabiliriz ve sadece komut satiri argumani olmasini istedigimiz arguman kalsin istiyorsak, OPTIND-1 defa shift etmemiz gerekir.
# # shift komutunu girelim:
shift "$(( OPTIND - 1 ))"
# echo "----------------------------"
# echo "Shiftten sonra:"
# echo "Toplam arguman sayisi: ${#}"
# echo "Tum argumanlar: ${@}"
# echo "Ilk arguman: ${1}"
# echo "Ikinci arguman: ${2}"
# echo "Ucuncu arguman: ${3}"
# echo "OPTIND: ${OPTIND}" # gorulebilecegi gibi OPTIND tabii ki degismiyor.
# calistirinca kalabalik yapmasin diye yorumladim lazim olursa yorumlari kaldir.

# mesela bu scriptte opsiyonlar disindaki argumanlar hata verdirsin.
if [[ "${#}" -gt 0 ]]
then
  kullanilis
fi

# her seferinde detayli modun acik olup olmadigini kontrol etmek icin if kontrolu yapmamiz lazim. ama bunun yerine bunu detay_acik fonksiyonuna tanimlayarak daha temiz bir kod yazabiliriz.
detay_acik "Parola olusturuluyor..."

# simdi parolayi olusturalim
PAROLA=$(date +%s%N${RANDOM}${RANDOM} | sha256sum | head -c${UZUNLUK})

# simdi de -s opsiyonunun girilip girilmedigini kontrol edelim. girildiyse parolaya ozel karakterler de ekleyelim
if [[ "$OZEL_KARAKTER_KULLAN" = 'true' ]]
then
  detay_acik "Rastgele bir ozel karakter seciliyor."
  OZEL_KARAKTER="$(echo '!^+%&/()=?_|*}]][{$#><+-' | fold -w1 | shuf | head -c1)"
  PAROLA="${PAROLA}${OZEL_KARAKTER}"
fi

detay_acik 'Parola basariyla olusturuldu!'
detay_acik 'Iste parolaniz:'

# parolayi goster
echo "${PAROLA}" # detayli mod acik olmasa da parolanin gosterilmesini istiyoruz.

exit 0
