#!/bin/bash

# bu scriptte, hesabini bir sureligine kullanmayacak olan kullanicilarin hesaplarini askiya alacagiz. eger bir kullanicinin hesabini tamamiyla kaldirmak istiyorsak userdel komutunu kullan-
# mamiz gerekir. 
# userdel komutu cogu sistemde sadece su tarafindan gorulebilmektedir. tum sistemlerde sadece su tarafindan calistirilabilir. userdel ile kullaniciyi kaldirdigimizda kullaniciya ait home 
# dir silinmez. bunu kaldirmak icin -r opsiyonu kullanilabilir. kullaniciyi ve home dir'i kaldirirken kullanicinin verilerini arsivlemek icin userdel kullanmadan once tar ile kullanicinin
# home dir'i arsivlenmelidir. 
# tar kullanirken -c, arsiv olusturmak; -t, arsiv icerigini goruntulemek; -x [HEDEF_DIR] ise arsiv icerigini cikarmak icin kullanilir. -f [ARG] opsiyonu ile oluşturulacak, cikarilacak 
# veya goruntulenecek arsiv dosyasinin adini veriyoruz. -v detayli ciktilar icin kullaniliyor. -z ise compressed arsiv dosyalari olusturur. bunlarin uzantilari .tar.gz veya .tgz olabilir. 
# ornegin deneme klasorunu, deneme.tar.gz seklinde arsivlemek icin "tar -zcvf deneme.tar.gz deneme/" komutunu, bu arsivi yedek klasorune cikartmak icin "tar -zxvf deneme.tar.gz ./yedek"
# komutu kullanilir.
# bir kullanicinin hesabini askiya almak icin bir kac yontem vardir. bunlardan biri parolayi kitlemektir. bu da "passwd -l KULLANICI_ADI" seklindedir. parolayi acmak icin ise passwd -u
# KULLANICI_ADI komutu kullanilir. fakat bu yontemle, kullanicinin SSH anahtari kullanmasini onlemez. bir baska yontem de bazi sistemlerde /etc/shells icerdinde bulunan shell'lerden
# /sbin/nologin shell'ini kullanmaktir. shell olarak bunu tanimladigimizda kullanici giris yapamaz. kullaniciya bu shell'i tanimlamak icin usermod komutunu kullaniriz. -s secenegi shell'i
# belirtmek icin kullanilir. yani "usermod -s /sbin/nologin KULLANICI_ADI" komutuyla kullanicinin giris yapmasini engeller ve "usermod -s /kullanilan/shell/yolu KULLANICI_ADI" ile tekrar
# izin verebiliriz. SSH anahtarlariyla sisteme ulasilmasini engellese de interaktif olarak kullanicinin giris yapmasini gerektermiyen isleri (port iletimi gibi) yapmasini engellemez.
# en kullanisli ve en guvenli yontem chage komutudur. chage komutu, kullanicinin sifresinin suresini degistirir ve kullaniciya erisimi tamamen engeller (SSH anahtarlari dahil.) -E opsiyonu 
# ile sona erme suresi, 01.01.1970ten bu yana gun formatinda veya YYYY-MM-DD tarih formatinda belirtilir. basitce -E 0 kullanicinin hesabini aninda askiya alacaktir. -E opsiyonundan -1
# sayisini gecirdigimizde hesabin sona erme suresi kaldirilir yani tekrar erisime acilir. bir kullaniciyi askiya almanin en guvenli yolu budur.

# bu script kullanicilari silecektir.
if [[ "${UID}" -ne 0 ]]
then
  echo "Lutfen sudo ile veya root kullanici olarak calistirin." >&2
  exit 1
fi

# bir pozisyonel arguman oldugundan emin ol
if [[ "${#}" -lt 1 ]]
then
  echo "Kullanilis: ${0} KULLANICI_ADI" >&2
  exit 1
fi

# ilk argumani silinecek kullanici kabul edelim
KULLANICI="${1}" # aslinda cok gerek yok ama boyle daha aciklayici oluyor.

# kullaniciyi sil
userdel ${KULLANICI}

# kullanicinin silindiginden emin ol
if [[ "${?}" -ne 0 ]]
then
  echo "${KULLANICI} hesabi silinemedi." >&2
  echo "Lutfen tekrar deneyiniz." >&2
  exit 1
fi

# hesabin silindigini soyle
echo "${KULLANICI} basariyla silindi!"

exit 0
