# tupple'lar sabit uzunluklu, değişmez (immutable) listeler olarak değerlendirilebilir. bir dizi elementin
# belirli bir sırada sıralanmasıyla oluşturulur ve oluşturulduktan sonra değiştirilemezler. tıpkı listeler
# gibi tuple'lar da heterojen ya da homojen olabilir fakat listeler genellikle homojen olarak kullanılırken
# tuple'lar genelde heterojen verileri saklamada kullanılırlar.
# iki obje arasına virgül (,) konmasıyla tuple oluşturulabilir:
paketler = "i3", "xautolock", "nm-applet"
print(type(paketler))
# ama genel kullanım okunabilirliği daha yüksek olduğu icin bunların parantez içinde tanımlanmasıdır:
paketler = ("i3", "xautolock", "nm-applet") # aynı şeydir ve daha sık kullanılır.
print(type(paketler))
# tıpkı boş listeler ve boş stringler gibi boş tuple'lar d tanımlanabilir ve geçerli objelerdir.
boş = ()
print(type(boş))
# tuple'ları oluşturanın parantezler değil virgüller olduğu unutulmamalıdır. boş parantezler python ta-
# rafından boş tuple'lar olarak okunsa da tek karakter bulunduran parantezler tek karakterli bir tuple
# olarak algılanmaz çünkü tuple oluşması için virgülle birbirinden ayrılmış objeler söz konusu olmalıdır.
tek_eleman = (1) # burada tanımlanan bir tuple değil düz integer'dir
print(type(tek_eleman))
# tuple olusturmak icin virgül kullanmamız gerekir:
tek_eleman = 1, # 17. satır tuple belirtmezken 20. satır bir tuple'dır
print(type(tek_eleman))
# veya:
tek_eleman = (1,)
print(type(tek_eleman))

print()

# tuple'larla listelerin ortak özelliklerinden biri uzunlukları olmasıdır:
print(len(paketler))
# bir diğer özellikleri de indekslenebilmeleridir:
print(paketler[1])
print(paketler[-3])
print(paketler[0:2])
# yine tuple'lar da var olmayan indekslerle IndexError verirler.

# bunların listelerden en önemli farkı ise değişmez (immutable) olmalarıdır. listelerde indeks syntaxı
# ile istenilen indekslere yeni elemanlar atanabilirken tuple'larda aynı syntax kullanıldığında TypeError
# alınır.
# paketler[0] = "i3gaps" # --> yorum kaldırılınca TypeError alınır.

# değişmez oldukları için listelerde kullandığımız methodların pek çoğunu tuplelarda kullanamayız. dir
# fonksiyonuyla tuple'larda geçerli metodlara baktığımızda yalnızca count ve index metodlarını görürüz,
# append, pop, push gibi metodlar tuple'lar için geçerli değildir.

# tuple'ların değişmez olması, tuple'lar içindeki elementleri etkilemez. yani değişebilir bir obje olarak
# listelerden oluşan değişmez bir tuple'a eleman ekleyip çıkaramayız veya tuple'daki bir listeyi, başka
# bir listeyle değiştiremeyiz fakat tuple içindeki listeleri yine de değiştirebiliriz:
adresler = (
    ['Marmara Sokak', 'No:36', 'Çankaya', 'Ankara'],
    ['Emirefendi Sokak', 'No:2', 'Bafra', 'Samsun']
)
print(adresler)
# şimdi 1. indeksteki listenin 2. indeksindeki karakteri değiştirelim:
adresler[1][2] = 'BAFRAAAAA'
print(adresler) # burada değişen tuple değil, tuple içindeki listedir.

print()
# ------------ Unpacking ------------ #

# tuple'ların her bir indeksindeki değeri değişkenlere tek tek atayabiliriz:
çalışan = ("Egemen", "Şahin", "Uzman", "25")
ad = çalışan[0]
soyad = çalışan[1]
görev = çalışan[2]
yaş = çalışan[3]
print(ad, soyad, görev, yaş)
# bunun yerine tüm bu değişkenleri tek satırda atayabiliriz. bu syntaxa unpacking denir.
isim, soyisim, pozisyon, yaş = çalışan # özellikle farklı değişkenler seçtim ki fark belli olsun
print(isim, soyisim, pozisyon, yaş)
# aynı syntax listelerle de kullanılabilir:
adres = ['Marmara Sokak', 'No:36', 'Çankaya', 'Ankara']
sokak, numara, ilçe, il = adres
print(sokak, numara, ilçe, il)
# eğer daha az veya fazla değişken tanımlanırsa ValueError alınır.
# sokak, numara, ilçe = adres veya sokak, numara, ilçe, il, ülke = adres ValueError verir.

# unpacking syntaxından en sık yararlanılan durum, iki değişkenin değerlerinin birbiriyle değiştirilmesidir.
# mesela  a ve b'ye birer sayı atayalım ve bunları birbiriyle değiştirelim:
a = 5
b = 15
print(a, b)
# şimdi bunların değerlerini değiştirelim. bunun için yeniden atama syntaxı saçma olur fakat a, b tuple'ını
# unpacking syntaxıyla kullanabiliriz:
b, a = a, b
print(a, b)

print()

# tuple'larla unpacking syntaxında bir değişkene birden fazla eleman atanması, *degisken syntaxıyla müm-
# kündür. *deg, deg1, deg2 = tuple syntaxıyla son iki elemanı deg1 ve deg2'ye; kalan degiskenleri deg de-
# ğişkenine atamaış oluruz. bu durumda birden fazla eleman atanan değişken bir liste olur, tuple değil.
# aynı syntaxı kullanarak ilk x elemanı ayrı ayrı değişkenlere, kalanları ise tek bir değişkene atamak
# da mümkündür.
isim, soyisim, *detaylar = çalışan
print(isim)
print(soyisim)
print(detaylar)
print(type(detaylar)) # <class 'list'>
# aynı syntazı ilk değişkenler için de uygulayabiliriz:
*detay, ilçe, il = adres
print(ilçe)
print(il)
print(detay)
# hatta ortadaki değişkenler için bile uygundur:
sokak, *detay, il = adres
print(sokak)
print(il)
print(detay)
# dikkat edilmesi gereken; bir unpacking'de bu syntaxı bir defa kullanabiliyoruz.

print()

# * syntaxı ile bir fonksiyona sınırsız sayıda pozisyonal arguman tanımlanabilmektedir. bunun icin genel-
# likle args degiskeni kullanılır. bu bir zorunluluk olmamakla beraber sıklıkla kullanılmaktadır. bir
# fonksiyona parametre olarak (*args) veya * ile baska bir parametre tanimlandığında fonksiyon içerdinde
# bu parametrelerin hepsi args tuple'ı içersinde tanımlanır.
def fonksiyon(*args):
    print(args) # fonksiyon icinde soz konusu tuple çağırılırken değişken ile çağırılır. *, yalnızca fon-
               # ksiyona tanımlanan tüm pozisyonel parametrelerin bir tuple olduğunu belirtir.
    print(type(args))

fonksiyon(1)
fonksiyon(1, 2, 3, 4, 5)

print()

# örnek olarak istenilen sayıda pozisyonal argüman kabul edip, verilen sayıların en büyüğünü çıktı olarak
# veren bir fonksiyon tanımlayalım:
def en_büyük(*sayılar):
    en_büyük = sayılar[0]
    for sayı in sayılar:
        if sayı >= en_büyük:
            en_büyük = sayı
    print(en_büyük)

en_büyük(1, 5, 987, 32, 5465, 21274, 2132, 68, 8793)

print()

# bu syntax ile tıpkı tuple'ların unpacklenmesinde olduğu gibi *'lı değişkenden önce veya sonra başka pa-
# rametreler de tanımlamak mümkündür. def fonks(par1, *pars) syntaxı da mümkündür. burada '*' dışında 
# kalan argüman, bir tuple elemanı olarak atanmaz, hangi türde objeleyse, fonksiyon içersinde de öyledir.
# fakat par1, *pars, par2 veya *pars, par1 syntaxı error verir çünkü python * ile oluşturulan tuple'ların
# ardından atanacak keywordleri, doğrudan belirtilmediğinde (tıpkı print fonksiyonunun sep, end gibi para-
# metreleri gibi) hata verir.
def func(a, *args):
    print(f"{a}'nın veri tipi {type(a)}")
    print(f"Kalan argumanlar ise bir tuple'dır: {args}")

func("adald", "aldkad", 13213, 545, 48745, 3.14)

def bir_func_daha(a, *args, b):
    print(f"{a}'nın veri tipi {type(a)}, {b}'nin veri tipi ise {type(b)}")
    print(f"Kalan argumanlar ise bir tuple'dır: {args}")

bir_func_daha("adald", "aldkad", 13213, 545, 48745, b = 3.14)

print()

# fonksiyonlar ve parametrelerle oluşturulan bu syntaxın tersi de mümkündür. bu durumda '*', fonksiyonun
# tanımlanmasında değil çağırılmasında kullanılır. mesela iki argüman kabul eden bir fonksiyon tanımlaya-
# lım. eğer bir tuple içersinde tanımlı iki objeyi bu fonksiyonun parametreleri olarak kullanmak için
# fonksiyonu tuple'la çalıştırırsak basitçe hata alırız çünkü tuple'lar birer objedir ve fonksiyon bunu
# ilk parametre olarak okur. bunun için tuple'ın başına * koyarak unpack edebiliriz. bu durumda fonksiyon
# parametre olarak tuple'ın unpack edilmesiyle açığa çıkan elemanları alır.
def çarpım(a, b):
    return a * b

sayılar = (15, 20) # unpack syntaxları listelerle de kullanılabilir!!
# print(çarpım(sayılar)) # bu satır çalıştırılınca tabii ki de hata verir.
print(çarpım(*sayılar))