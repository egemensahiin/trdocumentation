#!/bin/bash

# shell scriptlerinde ilk satirda scriptin nereden okunacagi belirtilir. bunu belirtmek icin shebang adi verilen sembolun (#!) ardindan yorumlayicinin yolu girilir. ozel olarak
# shell scriptlerde ilk satir basindaki hashtag (#) yorum olarak okunmaz. script kendisine verdigimiz kodu, bu yoldaki program tarafindan calistirir. mesela fish shell icin
# script yazmak istersek shebeng'den sonra /usr/bin/fish yolunu vermemiz gerekir.
# shell script dosyasi olustururken belirli bir uzanti girilmesi gibi bir zorunluluk soz konusu degildir. hicbir uzanti verilmeyebilecegi gibi istenilen uzantilar da verilebilir.
# buna karsin okunabilirlik acisindan cogunlukla shell'in kisaltmasi olarak .sh uzantisi verilir. bir scriptin calismasi icin 'calistirilabilir' olmasi yeterlidir. linuxta dosyalara
# 3 tur izin verilebilir: r: okunabilir x: calistirilabilir w: yazilabilir. bir klasor uzun listelendiginde bunlari gormek mumkundur (klasorlerin izni d yani directory'dir).
# yazilan bir scripti calisabilir duruma getirmeden calistirdigimizda "permission denied" uyarisi aliriz. bir dosyanin izinleri 3 tip kullanici icin duzenlenmektedir. ilk sirada
# mevcut kullanici gelir. ardindan tanimlanan izinler diger kullanici icindir. kalan izinler ise herkes icindir. ls -l komutuyla dosya izinleri soyle gorunur:
# drxwrxwrxw----
# ^---|||___ 	^ ile gosterilen d harfi klasorleri tanimlar --- ile gosterilen izinler mevcut kullanicinin izinleridir. ||| ile gosterilen izinler diger kullanicilarin, ___ ile gosterilenler
# ise herkese verilen izinlerdir. bu izinleri degistirmek icin chmod komutu kullanilir. chmod komutu 3 basamakli bir sayi ve dosya adi kabul eder ki bu sayi sagdan sola mevcut kullanici,
# diger kullanicilar ve herkese verilecek izinleri tanimlar. her bir grup icin verilecek sayi, verilmek istenen izinlerin kodlari toplamidir. izinlerin sayilsal degerleri, r=4 x=2 w=1 dir
# mesela (genelde de bunu kullanacagiz) yazdigimiz script basta herkes icin okunabilir ve yazilabilir fakat calistirilamaz olacaktir. biz ise mevcut kullaniciya her uc izni de tanimlarken
# diger iki gruba sadece okuma ve yazma yetkisi verelim. bunun icin ilk grup 4+2+1=7 diger gruplar ise 4+1=5 degerleri ile tanimlanir. yani girmemiz gereken komut 'chmod 755 dosya.uzanti'
# komutudur.
# scriptleri calisabilir duruma getirdikten sonra calistirmak icin scriptin tum yolunu girmemiz gerekir. yani mesela Documents klasorundeki ornek.sh scriptini calistirmak icin terminale
# /home/Document/ornek.sh komutunu girmemiz gerekir. bunun bir kisayolu sudur; eger bu scripti calistirirken soz konusu klasorde isek yapmamiz gereken o klasorun yolunu verek bir kisayol
# kullanmaktir ki bu da . 'dir. bir klasorde . mevcut klasorun, .. ise bir ust klasorun kisayoludur. yani scriptin oldugu klasorde ./ornek.sh komutunu girdigimizde ayni sonucu aliriz.

# simdi ilk scriptimizi yazalim
# echo komutu "" veya '' icersinde kendisine verilen argumani cikti olarak veren builtin bir komuttur. scripti calistirdigimizda Hello World yazmak icin:
echo "Hello World!" # veya
echo 'Hello World!' # syntaxlarini kullanabiliriz. iki syntaxin farki degiskenlerin yazilmasi tarafindadir (birazdan geliyorum oraya)

# scriptlerimize degisken atamak icin kullanmamiz gereken syntax basittir fakat bi takim kurallari vardir:
DEGISKEN='Egemen'
# scriptlerde esitligin basina ve sonuna bosluk konulmaz, gecerli degildir.
# scriptlerde degiskenlere verilen isimler harf (buyuk veya kucuk farketmez fakat buyuk-kucuk harf duyarlidir.), sayi veya '_' icerebilir. buna karsin diger sembolleri '-' iceremez.
# ayni zamanda scriptler buyuk veya kucuk harfle veya _ ile baslayabilir fakat degisken isminde sayi bulunmasi gecerli bir syntax iken degisken sayi ile baslamasi gecersizdir. buyuk
# veya kucuk harf icermesi degiskeni gecersiz yapmaz ama okunabilirlik acisindan sadece buyuk harfleri kullanmak daha pratiktir.
# daha sonra bir degiskenin cagrilmasi icin (burada hep echo kullaniyoruz ama her komut icin ayni seyler gecerli) iki syntax soz konusudur fakat bu iki syntax'ta da degiskenin mutlaka
# cift tirnak arasinda olmasi gerekir. bir degiskenin cagrilmasinda kullanilan syntaxlar "[baska seyler]$DEGISKEN [baska seyler]" veya "[baska seyler]${DEGISKEN}[baska seyler]"
# eger degisken $ altinda braket ({}) icersine yazilirsa verilen adin nerede baslayip nerede bittigi belirlenmis olur. bunun avantaji da yukarda da gorusdugu gibi braket bittikten sonra
# soz konusu degiskenle sonrasindaki objeler arasina bosluk koymamiza gerek olmamasidir. yukaridaki degisken ile benim adim Egemendir yazmak icin ilk syntaxi kullanamayiz.
echo "$DEGISKEN ${DEGISKEN}"
# eger degiskeni '' altinda cagirirsak bunu duz metin olarak okur:
echo '$DEGISKEN'
echo "Adim $DEGISKEN"
echo "${DEGISKEN}dir benim adim, adamin kulagini alirim!!"
# mesela bunu soyle yaparsak
echo "$DEGISKENdir benim adim, adamin kulagini alirim!!" # daha calistirmadan da gorebilecegimiz gibi $DEGISKENdir adinda bir degisken istiyor komut oysa ki oyle bir degisken tanimlamadik
# bu sebeple bu kisim " " olarak cikacak.

# iki degiskeni yan yana da cagirmak icin tabii ki {} syntaxi kullanilir:
EK="dir"
echo "${DEGISKEN}${EK} benim adim admain kulagini alirim."
# shell scriptleri dinamiktir yani bir degiskene daha sonra baska bir obje yeniden atabilir (reassignment):
DEGISKEN="Abizittinni"
echo "$DEGISKEN"
