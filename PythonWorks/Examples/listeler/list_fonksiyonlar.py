# listelerdeki elemanların her birini bir fonksiyona tabii tutmak için yaygın yaklaşım, liste-anlayisi.py
# syntaxidir. farklı bir yaklaşım ise map fonksiyonudur. map fonksiyonu temel olarak pythonda fonksiyonların
# hem çalıştırılabilir hem de çağırılabilir olmasına dayanır. yani her fonksiyon esasında bir objedir ve
# başka fonksiyonlarda (mesela help fonksiyonunda da) kullanılabilir. map fonksiyonu da iki argüman kabul e-
# der. bunlardan ilki bir fonksiyon, ikincisi ise bir listedir. dikkat edilmesi gereken burada map fonksiyonu
# altında başka bir fonksiyon çalıştırılmamaktadı; map fonksiyonunun bir girdisi olarak bir fonksiyon ve-
# rilmektedir.
sayilar = [2, 4, 6, 15, 21, 50]
# bu listedeki her sayının küpünü almak için genel yaklaşım şu şekildedir:
print([sayi ** 3 for sayi in sayilar])

# map fonksiyonu için girdi olarak önce bir fonksiyona ihtiyacımız var:
def küp(sayi):
    return sayi ** 3
# şimdi map fonksiyonunu çalıştıralım. syntaxı şöyle: map(func, iter(s))
print(map(küp, sayilar)) # görülebileceği gibi map fonksiyonu çıktı olarak generator tipinde bir obje olan
# map objesidir ve tekrar çağırılabilir.
print(type(map(küp, sayilar)))
# bu tip objeleri liste olarak elde etmek için basitçe list fonksiyonundan geçirebiliriz:
print(list(map(küp, sayilar)))

print()

#--------------------------------------------------------------------

# filter fonksiyonu da yine liste anlayışıyla çözülebilecek bir probleme alternatif olarak kullanılabilecek
# bir fonksiyondur. syntaxı map fonksiyonuna benzer fakat input olarak verilen fonksiyonun çıktı olarak bool
# tipinde bir obje vermesi gerekir. listedeki her eleman söz konusu fonksiyondan geçer ve çıktı olarak True
# veren elemanlarla yeni bir liste oluşturulurken diğer elemanlar atılır. normalde bunun için koşullu bir
# for döngüsü şöyle yazılabilir:
şehirler = ["Samsun", "Ankara", "Muş", "Afyonkarahisar", "Uşak", "Gaziantep"]
uzun_şehirler = [şehir for şehir in şehirler if len(şehir) > 6]
print(uzun_şehirler)

# filter fonksiyonuyla aynı çıktıyı elde etmek için önce bir fonksiyon tanımlamak gerek
def uzun_mu(kelime):
    return len(kelime) > 6
# filter fonksiyonu da generator tipinde bir obje verir:
print(filter(uzun_mu, şehirler))
print(type(filter(uzun_mu, şehirler)))
# list fonksiyonuyla veya bir for döngüsüyle bu obje liste olarak elde edilebilir:
print(list(filter(uzun_mu, şehirler)))

print()

#-------------------------------------------------------------------

# lambda bir fonksiyon değildir fakat fonksiyonlar içersinde kullanılan oldukça kullanışlı bir keyworddur.
# tanım olarak lambda, anonim yani isimsiz bir fonksiyondur. tek satırda tanımlanır ve ismi olmadığı için
# yalnızca tanımlandığı satırda çalışır, sonrasında tekrar çalıştırılamaz. özellikle filter ve map gibi
# hızlıca fonksiyon tanımlamamız gereken durumlarda kullanışlıdır. syntaxı şu şekildedir:
# lambda değişken: fonksyondan elde edilmesi istenen return

# şehirler listesiyle örnek verelim. uzun_mu fonksiyonunu tanımlamak yerine:
print(list(filter(lambda şehir: len(şehir) > 6, şehirler)))
# veya tek satırda, içinde "ş" harfi olan şehirleri listeleyelim:
print(list(filter(lambda şehir: "ş" in şehir, şehirler)))

# aynı syntax map fonksiyonu ile de kullanılabilir:
print(list(map(lambda şehir: şehir.count("a") + şehir.count("A"), şehirler)))

print()

#------------------------------------------------------------------

# all ve any fonksiyonları, listelerdeki elemanların doğru veya doğrumsu olup olmadığını kontrol eder ve
# buna göre bir boolean verirler. all fonksiyonu; verilen objedeki tüm elemanlar doğru veya doğrumsu oldu-
# ğunda True çıktısı verir, listedeki elemanlardan biri bile yanlış veya yanlışımsı (int olarak 0, string
# olarak "") olduğunda False çıktısı verir. Boş bir liste all fonksiyonu ile True çıktısı verir.
print(all([True, True]))        #True
print(all([True, True, False])) #False
print(all([1, 2]))              #True
print(all([1, 2, 0]))           #False
print(all(["a", "b", "c"]))     #True
print(all(["a", "b", "c", ""])) #False
print(all([" "]))               #True
print(all([]))                  #True

# any fonksiyonu ise, listede herhangi bir doğru veya doğrumsu olduğunda True çıktısı verir. yalnızca lis-
# tedeki tüm elemanlar yanlış veya yanlışımsı olduğunda False çıktısı verir. boş listelerle any fonksiyonu
# False çıktısı verir.
print(any([True, False]))       #True
print(any([False, False]))      #False
print(any([0, 1, 2]))           #True
print(any([0, 0.000]))          #False
print(any(["a", "b", ""]))      #True
print(any([""]))                #False
print(any([" "]))               #True
print(any([]))                  #False

print()

#--------------------------------------------------------------------

# max ve min fonksiyonları adından da anlaşılabileceği gibi harf veya sayılardan oluşan objeler içinde en
# büyük/küçük sayıyı veya alfabetik olarak en sonda/önde olan harfi çıktı olarak verir. girdi olarak liste
# veya string kabul eder; bunlar içinde max veya min olanı çıktı olarak verir. list veya stringlerin yanı
# sıra sıralı argümanları da karşılaştırıp max veya min çıktısı verir. burada harflere dikkat edilmelidir;
# zira fonksiyonlar birden fazla stringi karşılaştırmaz eğer tek bir harften oluşan stringler verildiyse
# bunları karşılaştırır fakat eğer birden fazla karakter içeren bir string verilirse bunun karakterlerini
# karşılaştırıp çıktı verir.
print(max([1, 3, 5, 7]))            #7
print(max(1, 3, 5, 7))              #7
print(min([1, 3, 5, 7]))            #1
print(min(1, 3, 5, 7))              #1
print(max(["a", "b", "t", "v"]))    #v
print(max("a", "b", "t", "v"))      #v
print(min(["a", "b", "t", "v"]))    #a
print(min("a", "b", "t", "v"))      #a
print(max("abtv"))                  #v
print(min("abtv"))                  #a
# print(max("ab", "tv")) # yorum kaldırıldığında bu satır hata verir.

print()

#---------------------------------------------------------------------

# sum fonksiyonu basitçe numerik elemanlardan oluşmuş bir listedeki tüm elemanların toplamını verir.
# listeden sonra bir start değeri girilirse tüm toplamı ayrıca bu değerle toplar.
print(sum([1, 2, 5]))
print(sum([-1, 2, -5]))
print(sum([1, 2, 5], 5))