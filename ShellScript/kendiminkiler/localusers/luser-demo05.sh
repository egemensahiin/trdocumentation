#!/bin/bash

# bu scriptte rastgele parolalardan olusan bir liste olusturacagiz.
# bash'in manualine baktigimizda random random sayilar olusturan builtin bir degisken oldugunu gorebiliriz. bu degisken RANDOM degiskenidir. RANDOM her cagirildiginda 0 ila 32767 arasinda bir
# tamsayi olusturmaktadir. bu degiskeni cagirip baska bir degiskene (bu programda PAROLA) kaydettigimizde script calistiginda olusturdugumuz rastgele degeri bir daha cagirabiliriz.

# Parola olarak rastgele bir sayi olustur.
PAROLA="${RANDOM}"
echo "${PAROLA}"

# Daha guvenli bir parola olusturmak icin PAROLA degiskenine birden fazla RANDOM degiskenini yan yana atayalim:
PAROLA="${RANDOM}${RANDOM}${RANDOM}"
echo "${PAROLA}"

# mantiken her saniye, birbirinden farklidir. yani her saniye icin olusturacagimiz tarih ve saatten olusan sayilar birbirinden farkli olacaktir. parola olarak parolanin olusturuldugu tarih ve
# saati kullanan bir script yazalim. date komutunun manual sayfasina baktigimizda farkli formatlarla farkli tipte sayilar olusturabilecegimizi goruruz. kullanisli formatlardan biri %s for-
# matidir. bu format 01.01.1970 UTC'den beri gecen saniyelerin sayisini verir ve dolayisiyla her saniye bir oncekinin bir fazlasidir yani her saniye birbirinden farkli sayilar verir. buna
# bazi kaynaklar UNIX zamani, EPIC zaman veya PSIOX zamani demektedir.

# Parolayi tarih ve saate gore UNIX zamani olarak atayalim:
PAROLA="$(date +%s)" # + isareti date programinin syntaxindan geliyor. format girmeden once + konuluyor.
echo "${PAROLA}"

# biraz ekstrem olsa da %s ile olusturulan sifreler bulunabilir. gunluk calisma saatleri hesaba katildiginda 28-29bin kombinasyon soz konusudur. fakat ilginc bir date komutu formati daha var-
# dir. %N yani nanoseconds formati, date komutunun calistigi andaki nanosaniyeyi verir ki bu tahmin etmesi cok daha zor, rastgele bir 9 basamakli sayidir. bunu UNIX zamani ile yan yana ge-
# tirdigimizde cok daha uzun ve zor bir sayi elde edebiliriz.

# Parolayi nanosaniye ve unix time olarak atayalim:
PAROLA="$(date +%N%s)"
echo "$PAROLA"

# checksum ile daha da guvenli paralolar olusturmak mumkundur. programlarin kendi kaynaklarinda sum numaralarini bulmak mumkundur. bu numaralar programin icerigine gore, farkli sayida karak-
# terden olusmus numaralardir. numara desek de bazilari (ornegin sha256sum) harf de icermektedir. programda yapilacak en kucuk degisiklikler bile tamamen farkli bir sum olusmasina sebep olur
# ve birebir ayni olan programlar birebir ayni sum'a sahiptir. bir programin istenilen programla ayni olup olmadigi, degistirilip degistirilmedigi programin yayincilarinin yayinladigi sum
# numaralariyla kolaylikla kontrol edilebilmektedir. sum programlari /usr/bin klasorundedir ve yaptiklari basitce cok buyuk verileri, birkac karakterden olusturan verilere (sumlara) donustur-
# mektir. bunlar genellikle (?) heksadesimal numaralardir; 0dan 9a kadar rakamlar ve a'dan f'ye kadarki harfler olmak uzere toplam 16 farkli karakterin kombinasyonlaridir. sha256sum ile
# olusturulan numaralar 64 karakterden olusmaktadir. yani o anin tarih ve saatini sha256sum'dan gecirirsek bu formatta bir sayi elde ederiz ki oldukca rastgele ve guvenlidir. bunun icin
# date'in standart outputunu pipe ile sha256sum'a input olarak verecegiz. sha256sum ile cikti aldigimizda sayinin yanina dosya adinin yazilmasi icin "  -  " ibaresi konur fakat bizim buna
# ihtiyacimiz yok. bunun icin verilen inputun istenilen uzunlugunu (default olarak bastan) output olarak veren head komutunu pipelayabiliriz. man sayfasindan baktigimizda head komutunun
# -n opsiyonuyla belirtilen sayida satiri, -c opsiyonuyla belirtilen sayida karakteri cikti olarak verdigi gorulmektedir. head -c32 dersek ilk 32 karakteri parola olarak atamak icin yeterlidir
PAROLA=$(date +%s%N | sha256sum | head -c32)
echo "$PAROLA"

# Daha da iyi bir sifre icin biraz da rastgele numara ekleyelim:
PAROLA=$(date +%s%N${RANDOM}${RANDOM} | sha256sum | head -c48)
echo "$PAROLA"

# ozel karakterler de ekleyebiliriz parolamiza. bunun icin ozel bir degisken vs yok ama kendimiz neden olusturmayalim. ilk yapmamiz gereken tum ozel karakterleri yazdirmaliyiz. bunun icin de
# kullanmamiz gereken komutu biliyoruz, echo. echo "!^+%&/()=?_-|\}][{$#Â><" ile tum karakterleri cagirdik. bu karakterleri rastgele karistirmak icin bir komutumuz var, shuf komutu fakat
# man sayfasina baktigimizda shuff ile sadece satirlarin karistirilabildigini goruruz. o zaman once tum karakterleri bir satÄ±ra yerlestirmeliyiz. bunun icin de kullanabilecegimiz bir komut vr
# o da fold komutu. man sayfasini inceledigimizde farkli secenekler oldugunu gormek mumkun. bu secenekleri denedigimizde -b1 ve -c1 secenegiyle en sona bir bosluk karakteri eklendigini goruyo-
# ruz fakat -w1 komutuyla dogrudan bu stringdeki her elemani bir satira yazdiriyor. daha sonra head komutuyla ilk karakterini aldigimizda ise rastgele bir ozel karakter almis oluruz.
# yani:
RASTGELE_OZEL_KARAKTER="$(echo '!^+%&/()=?_-|\}][{$#Â<>' |fold -w1 | shuf | head -c1)"
echo "${PAROLA}${RASTGELE_OZEL_KARAKTER}"
