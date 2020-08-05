#!/bin/bash

# bu scriptte case ifadesine bakacagiz. once karsilastirmak icin bir if blogu olusturalim:

# if [[ "${1}" = 'basla' ]]
# then
#   echo "Baslatiliyor."
# elif [[ "${1}" = 'durdur' ]]
# then
#   echo "Durduruluyor."
# elif [[ "${1}" = 'durum' ]]
# then
#   echo "Durum:"
# else
#   echo "Lutfen gecerli bir secenek giriniz!" >&2
#   exit 1
# fi

# şimdi aynı ifadeyi case ile olusturalim. case, bir "kelimenin", bir patern icerisinde olup olmadidigini kontrol eder fakat if ifadesi oluştururken oldugu gibi farklı paternlerde farklı
# komutlar calistirmak icin elif kullmamiz gerekmez. patern'den sonra bir parantez kapatilir, sonraki satirdaki komutlar calisir. komut blogunu bitirmek icin de ;; kullanilir. ifadeyi son-
# landirmak icin if'teki fi gibi case'in tersi esac kullanilir.

# case "${1}" in # yani 1. pozisyondaki arguman,
#   basla) # basla ise;
#     echo "Baslatiliyor."
#     ;;
#   durdur|bitir) # durdur veya bitir ise; # | kullanarak birden fazla patern icin kontrol gerceklestirebiliriz.
#     echo "Durduruluyor."
#     ;;
#   durum) # durum ise;
#     echo "Durum:"
#     ;;
#   *) # pattern matching'de *, kisaca herhangi bir seydir. yani herhangi bir şey varsa (boşluk ve yokluk da dahil);
#     echo "Gecerli bir secenek giriniz!" >&2
#     exit 1
#     ;;
# esac

# ayni isi yan yana syntax ile de yapabiliriz. pattern ve komutlar arasina ayirici bir sey koymamiza gerek yok esasinda fakat bosluk koydugumuzda okunurluk daha iyi olur.
case "${1}" in
  basla) echo "Baslatiliyor." ;;
  durdur|bitir) echo "Durduruluyor." ;;
  durum) echo "Durum:" ;;
  *) echo "Gecerli bir secenek giriniz!" >&2; exit 1 ;; # birden fazla komut birbirinden ";" ile ayrilir.
esac
