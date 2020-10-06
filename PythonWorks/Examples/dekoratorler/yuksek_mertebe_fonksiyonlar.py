# yüksek mertebeden fonksiyonlar; argüman olarak bir fonksiyon kabul eden veya çıktı olarak bir fonksiyon veren fonksiyonlardır. esasında fonk-
# siyonlar bir dizi talimattır yani objelerden farklıdır fakat bildiğimiz üzere pythonda her şey özünde nesnedir. bunu ispatlamak için basit
# bir fonksiyon tanımlayıp objelerin hangi tipte olduğunu görmek için kullandığımız type fonksiyonundan geçirebiliriz:
def bir():
    return 1
print(type(bir)) # fonksiyonu bir() şeklinde çağırdığımızda çalıştırarak geçirmiş oluyoruz ve fonksiyonun çıktısı type fonksiyonundan geçiyor.
                 # bu sebeple fonksiyonu () kullanmadan geçiriyoruz.
# tanımı düşündüğümüzde type'ın bu şekilde kullanımı da yüksek mertebeden fonksiyonlara bir örnektir.
# bu konsepti sadece yüksek mertebeden fonksiyonlarla kısıtlı düşünmemize gerek yoktur. bir liste, sayıları depolayabildiği gibi fonksiyonları
# da depolayabilir veya bir sözlük, value veya key olarak stringleri tutabildiği gibi fonksiyonları da tutabilir. burada fonksiyondan kastedi-
# len çalışmış bir fonksiyonun çıktısı değil, çalışmamış bir fonksiyon yani "mantık" veya "adımlar dizisi"dir. çalıştırılan bir fonksiyon,
# çıktı değerini verir mantığı değil.
# mesela bir kaç fonksiyon tanımlayıp bunları bir listede tutalım:
def kare(sayı):
    return sayı ** 2
def küp(sayı):
    return sayı ** 3
def carpı10(sayı):
    return sayı * 10
işlemler = [kare, küp, carpı10]
# hatta bunu itare bile edebiliriz:
for işlem in işlemler:
    print(işlem(5))

print()

# şimdi bir de yüksek mertebe fonksiyon konseptini görmek için kendimiz bir yüksek fonksiyon yazalım:
def ekle(a, b):
    return a + b
def çıkar(a, b):
    return a - b
def hesapla(func, a, b):
    return func(a, b)
# ekle ve çıkar fonksiyonları normal fonksiyonlardır. fakat hesapla fonksiyonu, argüman olarak başka bir fonksiyon kabul eden ve verilen fon-
# ksiyonun çıktısını veren bir yüksek mertebeli fonksiyondur.
print(hesapla(ekle, 3, 5)) # hesapla fonksiyonuna argüman olarak bir fonksiyonun çıktısını vermiyoruz, doğrudan fonksiyonu veriyoruz.
print(hesapla(çıkar, 3, 5))

print()

# yukarıda da belirttiğimiz gibi yüksek mertebeden bir fonksiyon, argüman olarak bir fonksiyon alabildiği gibi çıktı olarak da bir fonksiyon verebilir.
# mesela hesapla fonksiyonunu bir de bu yaklaşımla tanımlayalım. bu durumda fonksiyon bir iç içe fonksiyon olarak tanımlanacak:
def hesapla2(işlem):
    # hesapla2 fonksiyonuna argüman olarak verilen "işlem" bir stringdir. bu stringi koşullayarak fonksiyonumuz bir fonksiyonu çıktı olarak verecek;
    # öncelikle fonksiyonlarımızı tanımlayalım
    def ekle(a, b):
        return a + b
    def çıkar(a, b):
        return a - b
    # şimdi verilen operasyonu koşullayalım:
    if işlem == "ekle":
        return ekle # görüldüğü gibi çıktı olarak bir fonksiyon tanımladık, fonksiyonu çalıştırmadık.
    if işlem == "çıkar":
        return çıkar
print(hesapla2("ekle")) # görüşdüğü gibi bu şekilde fonksiyonu çalıştırdığımızda çıktı olarak obje halinde fonksiyonu alırız. çıktı olarak aldığımız fon-
# ksiyonu da çalıştırmak istiyorsak onu da çalıştırmamız gerekir:
print(hesapla2("ekle")(3, 5))
print(hesapla2("çıkar")(3, 5))