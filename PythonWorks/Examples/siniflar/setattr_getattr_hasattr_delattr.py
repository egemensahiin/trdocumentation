# setattr ve getattr, pythonda built-in bulunan ve sınıflardaki niteliklere, nokta syntaxını kullanmadan erişmek (getattr) veya atamak (setattr) için
# kullanılırlar. getattr ve setattr genellikle niteliğin dinamik olarak oluştuğu, başka bir objeden veya modülden geldiği durumlarda yani elimizde ke-
# sin bir nitelik ve durum olmadığında tercih edilir.
# setattr fonksiyonu argüman olarak objeyi, atanacak olan niteliğin ismini içeren bir stringi ve bu niteliğe atanacak değeri alır. dinamik olarak ni-
# teliklerin oluşturulmasında oldukça kullanışlıdır. örneğin bir sözlük tanımlayalım ve bu sözlüğün "key"leri nitelik, "value"ları da niteliğe karşı-
# lık gelen değerler olsun (ki pratikte dinamik nitelikler çoğunlukla böyle oluşturulur):
bilgiler = {
    "isim"      : "Bilgisayarlı Medisinal Kimya",
    "ders_saati": 2,
    "anabilimd" : "Farmasötik Kimya",
    "hocalar"   : ["İlkay Yıldız", "Esin Akı Yalçın"]
}
class Ders():
    def __init__(self, bilgiler): # sınıfımızı tanımlarken bir argüman ile örneklendireceğiz Sınıf(sözlük) şeklinde ve nitleikleri bu sözlükten for 
        # döngüsü ile çekerek tanımlayacağız:
        for key, value in bilgiler.items():
            # self.key yazımı ile oluşturulan nitelik "key" niteliği olacaktır fakat bizim burda kullanmak istediğimiz key, bilgiler sözlüğünden di-
            # namik olarak for döngüsüyle atanan key yani bir değişken ismi. bunun için nokta syntaxını dinamik olarak nitelik atarken kullanamıyor
            # ve setattr fonksiyonuna ihtiyaç duyuyoruz:
            setattr(self, key, value) # self objenin kendisini refere eder. ikinci argüman niteliğin ismi, 3.sü ise değeridir.

# sınıfımızı örneklendirelim ve nokta syntaxıyla, tanımladığımız nitleiklerin varlığını kontrol edelim:
medisinal = Ders(bilgiler)
print(medisinal.isim)
print(medisinal.ders_saati)
print(medisinal.anabilimd)
print(medisinal.hocalar) # gördüğümüz gibi sınıfımızı örnekledir ve verdiğimiz sözlükteki tüm key'ler kendilerine karşılık gelen value'ları değer ala-
# rak birer nitelik olarak atandı.

print()

# getattr ise setattr'ın tamamlayıcısıdır ve argüman olarak bir obje, kontrol edilen niteliğin ismini içeren string ve bir yedek değer alır. getattr,
# objede niteliği arar ve niteliğin değerini çıktı olarak verir. setattr'da olduğu gibi dinamik isimleri kullanmamızın yanısıra nokta syntaxından bir
# avantajı da eğer aradığımız isim, nitelik olarak mevcut değilse AttributeError verip programı sonlandırmaz; 3. argümanı verir ve program ça-
# lışmaya devam eder. şimdi bir liste tanımlayıp bu listedeki isimlerin objemizdeki karşılığını kontrol edelim:
arananlar = ["ders_saati", "isim", "akts", "ulusal_kredi"]
for aranan in arananlar:
    # print(medisinal.aranan)#, medisinal objesindeki "aranan" dinamik değişkenini değil; medisinal objesinde aranan ismindeki niteliğin varlığını kon-
    # trol eder ve bu obje de mevcut olmadığı için AttributeError verir.
    print(getattr(medisinal, aranan, "NitelikBulunamadı"))

print()

# hasattr, bir obje ve bir string kabul eder ve söz konusu string, objede nitelik olarak mevcutsa True, değilse False verir. delattr ise hasattr ile
# aynı argümanları alır fakat verilen niteliği siler, eğer nitelik yoksa AttributeError verir. bu iki fonksiyonu birlikte kullanarak hatalardan kaçı-
# nabiliriz:
print(medisinal.ders_saati)
for aranan in arananlar:
    if hasattr(medisinal, aranan):
        delattr(medisinal, aranan)
# print(medisinal.ders_saati) # görülebileceği üzere 47. satırda hata almazken burda hata alıyoruz çünkü 50. satırda ders_saati niteliğini sildik.