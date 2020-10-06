# kapsam yani scope, bir ismin programda kullanılabildiği konumları ifade eder. pythonda iki farklı kapsam söz konusudur: global kapsam ve lokal kapsam.
# global kapsam, üzerinde çalışılan dosyayla sınırlıdır. diğer python dosyaları global kapsamın dışındadır ve söz konusu ismin kullanlabilmesi için dos-
# yanın import edilmesi gerekir. mesela;
yaş = 25 # yaş değişkeni global kapsamda bir değişkendir.
# lokal kapsam ise fonksiyon gövdeleriyle kısıtlıdır. daha öncesinden de hatırlayabileceğimiz gibi fonksiyon gövdeleri içinde tanımlanan değişkenler,
# fonksiyonlar vs isimler, fonksiyon dışından çağrılamaz çünkü bu isimler fonksiyonun lokal kapsamı içersindedir.
def bir_fonksiyon():
    bir_şey = 10 # bir_şey değişkeni, tanımlandığı fonksiyon dışarsında tanımlı değildir. söz konusu fonksiyonu çalıştırsak dahi fonksiyon çalıştıktan
    # sonra bu değişkeni çağırdığımızda NameError alırız. bunun sebebi, global kapsamda çalıştığımızda, lokal kapsamdaki isimlere erişememizdir.
bir_fonksiyon()
print(yaş) # bu satırda hata almazken;
# print(bir_şey) # bu satırda NameError alırız.
# global kapsamda iken lokal kapsamdaki isimlere erişemesek de, lokal kapsamda iken global kapsamdaki isimlere erişebiliriz.
def yaş_fonsiyonu():
    print(yaş)
yaş_fonsiyonu()

print()

# python lokal ve global değişkenleri birbirlerinden bağımsız takip eder. yani bir global değişkenin ismiyle bir lokal değişken de tanımlamamız müm-
# kündür. bu durumdaki değişkenlere gölge değişken denir ve genellikle kaçınılmak istenen bir pratiktir.
def gölgeli_şeyler():
    yaş = 24
    print(yaş)

gölgeli_şeyler() # görüldüğü gibi, fonksiyon çalıştırıldığında yaş değişkeni 25 değil 24 olarak print edilir çünkü python, fonksiyon gövdesindeyken
# lokal değişkeni kullanır. fakat yaş değişkeni global kapsamda hala 25tir:
print(yaş)

print()

# global ve lokal kapsam konsepti, sabit (constant) değişkenler kullanıldığında önem kazanır. kodumuzda bir kaç farklı yerde kullanacağımız değişkenleri
# tek bir sefer global kapsamda tanımlamamız yeterlidir. bu sayede söz konusu değişkenin değeri değiştiğinde, tek tek lokal kapsamları taramak yerine
# yalnızca global kapsamdaki değişkenin değerini değiştirmek yeterli olacaktır. bu şekilde kullanılan sabit ve global değişkenler, büyük harflarle tanım-
# lanır.
# mesela senaryomuzda, alınan ürünlerin vergi miktarını hesaplayalım fakat tekel ürünlerinden çift vergi alınsın. bu durumda kullanılacak vergi oranı,
# global olarak sabittir bu sebeple şu şekilde tanımlanır:
VERGI_ORANI = 0.18
def ürün_vergisi(fiyat):
    return round(fiyat * VERGI_ORANI, 2) # round fonksiyonu, ondalıklı sayıları istenen basamak sayısına kadar yuvarlar.

def tekel_vergisi(fiyat):
    return round(fiyat * (VERGI_ORANI * 2), 2)

print(ürün_vergisi(10))
print(tekel_vergisi(100))

print()

# --- Kapsamlar hiyerarşisi ve LEGB kuralı:
# LEGB kısaltması, local/enclosing function (çevreleyen fonksiyon)/global/built-in diziliminin akronimidir ve kapsamlar hiyerarşisinin sırasını ifade e-
# der. kapsamlar hiyerarşisinde ilk önce lokal kapsam gelir. eğer python, bir ismi lokal kapsamda bulamazsa bunu çevreleyen fonksiyonda (varsa) bu ismi
# arar. orada da yoksa global kapsama, yine bulamazsa built-in isimlere bakar ve eğer isim bunlardan hiçbirinde yoksa NameError verir.
# örnek inceleyelim:

# pyhton kütüphaneleri built-in'e karşılık gelir ve bunu çalışılan programda görmeyiz
# --> burası global kapsamdır
değişken = "obje global"
def çevreleyen():
    # --> burası enclosing function kapsamıdır.
    değişken = "obje dış"
    def çevrelenen():
        # burası ise local kapsamdır.
        değişken = "obje iç"
        return değişken
    return çevrelenen()
# şimdi çevreleyen() fonksiyonunu çalıştırdığımızda return olarak çevrelenen() fonksiyonu, o da return olarak değişken'i verecek ve bu değişken lokal
# kapsamda yani hiyerarşideki ilk kapsamda bulunduğu için çıktı olarak ona karşılık gelen objeyi alacağız:
print(çevreleyen())

# tüm değişken ve fonksiyonları bir daha tanımlayalım ve bu sefer değişken'i iç fonksiyonda tanımlamayalım
değişken = "obje global"
def çevreleyen():
    değişken = "obje dış"
    def çevrelenen():
        return değişken
    return çevrelenen()
# bu defa fonksiyon çalıştığında; çevreleyen fonksiyon, çıktı olarak çevrelenen fonksiyonu çalıştıracak, o da değişken'i return edecek. python değişkeni
# önce lokal kapsamda arayacak fakat gördüğümüz üzere lokal kapsamda değişken tanımlanmamış. bu durumda python önce çevreleyen fonksiyonda değişkeni arar
# ve çıktı olarak, çevreleyen kapsamdaki değişkene karşılık gelen objeyi verir.
print(çevreleyen())

# değişken ve fonksiyonları tekrar tanımlayalım
değişken = "obje global"
def çevreleyen():
    def çevrelenen():
        return değişken
    return çevrelenen()
# yukarıdaki duruma benzer şekilde fonksiyonu çalıştırdığımızda python bu defa ne lokal ne de çevreleyen kapsamda değişkeni bulamayacağı için, değişken
# lokal kapsamdan return edilmiş olsa da değerini global kapsamdan alacak:
print(çevreleyen())

# built-in kapsamı görmek için değişken yerine len fonksiyonunu kullanalım:
def çevreleyen():
    def çevrelenen():
        return len
    return çevrelenen()
# bu defa lokal kapsamda return edilen "len" ismi, ne lokal kapsamda, ne çevreleyen kapsamda ne de global kapsamda tanımlanmış bir isim değil. bu durumda
# python bu ismi hiyerarşinin en son kapsamında yani built-in kapsamda arar ve len fonksiyonuna ulaşır.
print(çevreleyen())
# hatta len fonksiyonunu çalıştırabiliriz de:
print(çevreleyen()("egemen"))