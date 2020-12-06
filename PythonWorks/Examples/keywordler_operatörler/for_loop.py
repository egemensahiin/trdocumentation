# for döngüsü; string, list gibi düzenli (belli sıradaki) veri tiplerinin her bir birimini teker teker çağı-
# rıp işler. mesela stringlerde for döngüsüne bir bakalım:
string = "Bu bir string'dir."
for değişken in string: # burada "değişken" her seferinde stringin bir birimi (stringler için bu birimler ka-
    print(değişken) # karakterlerdir.) blok içersindeki işlemden teker teker ve sırayla geçerek okunur.
# görüldüğü gibi stringin bütün karakterleri tek tek bloktaki işlemden yani print fonksiyonundan geçerek tek
# tek ve sırayla yadırılır. illa değişkene bağlı bir işlem olmak zorunda da değildir. mesela stringin uzun-
# luğunu çıktı olarak veren bir for döngüsü yazalım:

toplam = 0
for değişken in string:
    toplam += 1

print(toplam)
print(len(string))
# for döngüsünde tanımlanan değişken her seferinde objenin (stringin) bir sonraki elemanına (karakterine) a-
# tanır. bunu görmek için for döngüsünden çıkan değişkeni print edebiliriz:
print(değişken)

print()

# listlerde de for döngüleri aynı şekilde kullanılır. mesela bir takım numaraları içeren bir listede for dön-
# güsü ile tek tek bunları yazdıralım:
numaralar = [1, 5, 4, 8, 3, 7]

for numara in numaralar:
    print(numara)
# mesela her numaranın karesini de yazdırabiliriz.
for numara in numaralar:
    print(numara ** 2)

# yine son elemanın hala numara değişkeninde tanımlı olduğunu yazdırarak görebiliriz.
print(numara)
# bu sayıları aynı şekilde toplayarak da elde edebiliriz.
toplam = 0
for numara in numaralar:
    toplam += numara
print(toplam)

print()

# stringlerden oluşan listelerle de for döngüsü kurulur.
samsunun_ilçeleri = ["Bafra", "İlkadım", "Atakum", "Yakakent", "çrş", "Havza", "Kavak"]

for ilçe in samsunun_ilçeleri:
    print(ilçe)

# her birinin uzunluklarını da elde edebiliriz. fakat bunun gibi fonksiyonları kullanırken heterojen listler
# konusunda dikkat edilmeli. int tipi veriler len fonksiyonu altında hata verirler.

for ilçe in samsunun_ilçeleri:
    print(len(ilçe))

# veya stringlerin hepsinin ilk karakterlerini yazdırabiliriz.

for ilçe in samsunun_ilçeleri:
    print(ilçe[0])

# yapılabilecekleri çeşitlendirmek mümkün. mesela hepsinin ilk harfiyle bir kısaltma yapalım:
kısaltma = ""
for ilçe in samsunun_ilçeleri:
    kısaltma += ilçe[0]

print(kısaltma)

print()

# for döngülerini, döngü bitmeden sonlandırmak mümkündür. bazen for döngüsüyle bir listeyi veya stringi dön-
# güye aldığımızda bahsi geçen objede belirli bir koşul ararız fakat döngü koşulu bulduğunda sonlanmaz. be-
# lirli bir koşulda döngüyü sonlandırmak için if ifadesiyle koşul belirtilip if gövdesinin sonuna döngüyü so-
# nlandırmak için "break" ifadesi konulmalıdır. mesela bir liste içersindeki tüm elemanların alfabetik st-
# ringler olup olmadığını kontrol eden bir fonksiyon yazalım.
def alfabetik_mi(lis):
    sonuc = True # kontrolümüzün sonucunu tanımlıyoruz
    for eleman in lis:
        eleman = str(eleman)
        if eleman.isalpha() == False: # eğer eleman alfabetik değilse;
            sonuc = False          # sonucu yanlış olarak değiştiriyoruz.
            break # eğer alfabetik olmayan bir eleman bulduysak listenin kalanına bakmamıza gerek yok. break
                  # ifadesiyle döngüyü bitiriyoruz.
    return sonuc

ornek = [1,2,3,"ljsndljan"]
print(alfabetik_mi(samsunun_ilçeleri))
print(alfabetik_mi(ornek))
# bu gibi bir fonksiyonun koşul tanımlanan noktada durduğunu ispatlamak için fonksiyon gövdesini çalıştırıp
# döngü bittiğinde oluşan "eleman" değişkenini çağırabiliriz:
for eleman in ["ljhkn", "hjmşl", 21, "bkjbkjb", "mslka"]:
    eleman = str(eleman)
    print(eleman)
    if eleman.isalpha() == False:
        break
# bu döngü, elemanlardan biri alfabetik olmadığında bittiği için liste bitene kadar sürmez. bu yüzden döngü
# gövdesine if koşulundan önce elemanları yazdırdığımızda ancak koşulu sağlayan elemana kadarki elemanları
# görürüz. (daha fazla örnek: deneme.py # Deneme 7 ve 8)

print()

# continue ifadesi, break ifadesinin tamamlayıcısı niteliğğinde olup döngüyü bitirmez, döngüyü devam etmeye
# zorlar. herhangi bir koşul ifadesinin bloğunda continue ifadesi varsa for döngüsü o element için orada bi-
# tirilip diğer element için devam eder. listedeki sayılardan yalnızca pozitif olanları toplayan iki fonk-
# siyon yazalım:
def pozitif_toplamı(lis):
    toplam =  0
    for el in lis:
        if el > 0:
            toplam += el
    return toplam

print(pozitif_toplamı([1,3,6,-1,-9,10]))
# aynı fonksiyonu continue ifadesiyle kurmak için sayı 0dan küçük olduğunda (if el < 0:) for döngüsünün de-
# vam edip sonraki elemana geçmesi (continue) gerekir. toplam'a elemanın eklenmesi, koşuldan sonra, for blo-
# ğu altında yazılır.
def pozitif_toplamı(lis):
    toplam = 0
    for el in lis:
        if el < 0:
            continue
        toplam += el
    return toplam

print(pozitif_toplamı([1,3,6,-1,-9,10]))
# iki syntax arasında teknik olarak pek fark yok esasında duruma göre her ikisi de değerlendirilebilir.