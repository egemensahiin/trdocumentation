# dekoratörler, fonksiyonların temel işlevlerini değiştirmeksizin ek özelliklerle fonksiyonu geliştirirler. basitçe dekoratör, input olarak bir fonksi-
# yon alan ve sonuçta da bir fonksiyon return eden yüksek mertebeli bir fonksiyondur.
# hızlıca basit bir örnek görelim:
def karşılama(fn):
    def iç():
        print("Fonksiyonu çalıştırıyorum...")
        fn()
        print("Fonksiyonunuzu çalıştırdım, iyi günler.")
    return iç
# karşılama fonksiyonunun ne yaptığına adım adım bakalım. "karşılama" argüman olarak bir fonksiyon kabul ediyor. daha sonra karşılama içinde tanımlanan
# "iç", bu fonksiyonu dekore ediyor ve yeni özellikler (bunu sadece bi şeyler yazdırmak olarak düşünmemek lazım. mesela programın çalıştığı esnada bazı
# fonksiyonların belirli zamanlarda çalışmasını istediğimizde bir timer dekoratör oluşturup, bu fonksiyonları bu dekoratörle kullanabiliriz.) ekliyor.
# son olarak karşılama fonksiyonu, içersinde tanımlanan iç fonksiyonunu return ediyor.
# basit bir fonksiyon tanımlayıp bunu karşılama dekoratörüyle çalıştıralım:
def basit_fonksiyon():
    print("Karmaşık işler")
print(karşılama(basit_fonksiyon)) # görüldüğü üzere çıktı olarak bir fonksiyon aldık. şimdi bu fonksiyonu çalıştıralım:
karşılama(basit_fonksiyon)()
print()
# 18. satırda yaptığımız işi yapmak için bir "syntactic sugar" mevcuttur (programlama dillerinde belli işlevleri daha kullanışlı hale getirmek için ge-
# liştirilmiş syntaxlara syntactic sugar denir). bir fonksiyonun tüm çağırımlarının (çalıştırılmalarının) dekoratörle olmasını istediğimizde, fonksiyo-
# nu dekoratörle beraber tanımlarız ve bunun için @dekoratör \n def fonksiyon(): syntaxını kullanırız:
@karşılama
def karmaşık_fonksiyon():
    print("basit işler")
# bundan sonra karmaşık_fonksiyonu her çağırdığımızda fonksiyon, dekoratör içersinde argüman olarak verilecek ve dekoratör fonksiyon çalıştırılacak:
karmaşık_fonksiyon()
print()
# bu syntaxın en önemli faydalarından biri, program içinde parantezlere boğulmadan istediğimiz fonksiyonu dekoratörle çağırabilmemizdir.
@karşılama
def başka_fonksiyon():
    print("ebele hübele")
başka_fonksiyon()

print()

# --- Argümanlar ve Dekoratörler
# dekoratörlerin yukarıdaki gibi kullanımı, argüman kabul eden fonksiyonlarda problem yaratır.
@karşılama
def selam(isim):
    print(f"Selam olsun sana eeey {isim}")
# şeklinde argüman kabul eden bir fonksiyon tanımlayalım.
# selam("Egemen") # fonksiyon çalıştırıldığında TypeError alırız ve hata açıklamasına baktığımızda iç() fonksiyonunun pozisyonel argüman kabul etmediğini
# fakat bir pozisyonel argüman verildiğini görürüz. bunun sebebi, dekoratörlerle bir fonksiyonu çağırdığımızda aslında dekoratördeki iç fonksiyonu çağı-
# rıyor oluşumuzdur ve bu fonksiyona hiçbir argüman tanımlanmamıştır. burada *args ve **kwargs syntaxı imdadımıza yetişir. hatırlanacağı üzere *args,
# fonksiyona verilen tüm pozisyonel argümanları tutan bir "args" tuple'ı oluşturur. benzer şekilde **kwargs da fonksiyona verilen tüm keyword argümanları
# tutan bir sözlük oluşturur.
def karşılama_ar_kw(fn):
    def iç(*args, **kwargs):
        # görmek için args tuple'ı ve kwargs sözlüğünü de yazdıralım:
        print(args)
        print(kwargs)
        print("Fonksiyonu çalıştırıyorum...")
        fn(*args, **kwargs) # eğer oluşturulan args tuple'ı ve kwargs sözlüğünü fonksiyona argüman olarak vermezsek bu sefer de selam fonksiyonu için
        # TypeError alırız çünkü iç() fonksiyonu çalışırken fn argümanını yani bu durumda selam fonksiyonunu çalıştırır ve selam fonksiyonu bir argü-
        # man beklemektedir. bu şekilde (fonksiyonlar çalıştırılırken argüman olarak verilen tuple'lar pozisyonel argüman, sözlüklerse keyword argüman
        # olarak okunduğu için) çalışan fonksiyon ne olursa olsun iç fonksiyonuna verilen parametrelerle çalışır.
        print("Fonksiyonunuzu çalıştırdım, iyi günler.")
    return iç
@karşılama_ar_kw
def selam(isim):
    print(f"Selam olsun dana eeey {isim}")
selam("Egemen") # "Egemen" stringi pozisyonel argüman olarak verildiği için çıktıda tek elemanlı args tuple'ı ve boş kwargs sözlüğü görülür.
print()
selam(isim = "Egemen") # burada ise string, keyword argüman olarak verildiğinden, boş bir args tuple'ı ve tek elemanlı kwargs sözlüğü görülür.

print()

# --- Return Değerleri ve Dekoratörler
# dekoratörlerin kullanımında bir başka problem de dekore etmek istediğimiz fonksiyonun bir değer return etmesi durumudur.
@karşılama_ar_kw
def toplam(*args):
    sonuç = 0
    for i in args:
        sonuç += i
    return sonuç
print(toplam(5, 3)) # görüldüğü gibi çıktıda toplam fonksiyonunun return ettiği değeri görmüyoruz bunun yerine None çıktısını alıyoruz. bunun sebebi,
# dekoratörle bu fonksiyonu çalıştırdığımızda 54. satırda bu fonksiyon çalışıp değeri return etmesine karşın bize çıktıyı veren iç fonksiyonundan bu
# değerin return edilmemesi. bunun için dekoratörleri tasarlarken fonksiyonun return değerini bir değişkene atamak iyi bir pratiktir. iç fonksiyonun
# sonunda da bu değeri return ettiğimizde dekore edilen fonksiyonun return değeri, iç fonksiyondan da return edilir:
print()
def karşılama_return(fn):
    def iç(*args, **kwargs):
        print("Fonksiyonu çalıştırıyorum...")
        sonuç = fn(*args, **kwargs)
        print("Fonksiyonunuzu çalıştırdım, iyi günler.")
        return sonuç # gönül isterdi ki bunu fonksiyon çalıştıktan hemen sonra return edebilelim fakat bu senaryoda iç fonksiyonu return verdikten son-
        # raki kod çalışmayacağı için dekoratör yarıda kalacaktır.
    return iç
@karşılama_return
def toplam(*args):
    sonuç = 0
    for i in args:
        sonuç += i
    return sonuç
print(toplam(5, 3)) # görüldüğü gibi return edilen değer en son yazılıyor fakat esasında fonksiyonumuz çalışmasını istediğimiz yerde çalışıyor.