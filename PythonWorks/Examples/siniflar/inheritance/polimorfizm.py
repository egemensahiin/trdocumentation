import random
# poliprfizm, obje odaklı programlamanın üç prensibinden biridir. polimorfizmde ana fikir, birden fazla objenin aynı metod çağrımına tepki vermesidir.
# fikrin temelinde kod, objenin ne tip bir obje olduğundan daha çok, hangi metodlara veya mesajlara cevap verdiğiyle ilgilenir. poli çok, morf da şekil
# demektir. bu durumda polimorfizm, farklı objelerin aynı metodun bunlar üzerinde çağrımıyla farklı şeylere dönüşmesine karşılık gelir. 
# polimorfizmin pythondaki en iyi örneği len fonksiyonudur. tanım düşündüğüldüğünde len bir metod değildir fakat arka planda len fonksiyonunun yaptığı
# şey, argüman olarak verilen obje üzerinde __len__ metodunu çalıştırmasıdır ve __len__ metodu, objenin tipine, ne olduğuna bakmaksızın listeler, strin-
# gler, tuplelar, sözlükler ve kendi yazdığımız objeler üzerinde aynı şekilde, aynı stabilitede çalışır.
class Şahıs():
    def __init__(self, isim, boy):
        self.isim = isim
        self.boy = boy
    def __len__(self):
        return self.boy
değerler = [
    "Egemen",
    [1, 3, 5],
    (2, 4, 6, 8),
    {"a": 1, "b": 2},
    Şahıs("Egemen", 175)
]

for değer in değerler:
    print(len(değer))
# görüldüğü gibi çeşit çeşit objeyi aynı fonksiyondan geçirsek de cevap alabiliyoruz çünkü __len__ metodu bu objelerde tanımlandığı müddetçe, objenin ne
# olduğu önemli olmuyor.

print()

# şimdi polimorfizmi sub-superclass hiyerarşisinde nasıl kullanacağımızı görmek için basit bir satranç bildirimi yazalım.
# insan ve bilgisyar olmak üzere iki farklı tip oyuncumuz olsun. bunların ikisi de oyuncu olduğundan, oyuncunun sahip olması gereken ortak özellikler ba-
# rındıracaklar:
class Oyuncu():
    def __init__(self, oyun_sayısı, zafer_sayısı):
        self.oyun_sayısı = oyun_sayısı
        self.zafer_sayısı = zafer_sayısı
    # bir de oyuncuların kazanma oranını görelim:
    @property
    def kazanma_oranı(self):
        return self.zafer_sayısı / self.oyun_sayısı

# insan oyuncumuzu tanımlayalım:
class İnsanOyuncu(Oyuncu):
    def hamle_yap(self):
        print("Oyuncunun karar vermesi bekleniyor..")
# bir de bilgisayar oyuncumuzu tanımlayalım:
class BilgisayarOyuncu(Oyuncu):
    # burada iş polimorfizme geliyor. hem insan hem de bilgisayar oyunda hamle yapacaklar. yani hamle yapma şekilleri farklı olsa da hamle yapmak davranışı
    # subclasstan bağımsız olarak her iki tip Oyuncu objesinde de olacak.
    def hamle_yap(self):
        print("Bilgisayar en iyi hamleyi bulabilmek için algoritmalar yürütüyor..")
# en başta import ettiğimiz random modülünü kullanarak polimorfizmin işlevselliğini göreceğiz. random modülü adı üstünde rastgelelikle ilgili işlevler ba-
# rındıran bir modül. biz bu modülde, bir sıralı objeden rastgele bir elemanı çıktı olarak veren choice fonksiyonunu kullanacağız. önce oyuncularımızı ta-
# nımlayalım:
insan = İnsanOyuncu(oyun_sayısı = 50, zafer_sayısı = 22)
bilgisayar = BilgisayarOyuncu(oyun_sayısı = 1000, zafer_sayısı = 999)
# iki sınıfın da Oyuncu alt sınıfı olmalarından ileri gelen nitelikleri mevcut. bunlardan biri de kazanma oranı:
print(insan.kazanma_oranı)
print(bilgisayar.kazanma_oranı)
# oyuna başlayacak oyuncu rastgele seçilsin:
beyazlar = random.choice([insan, bilgisayar])
# oyuna kim başlarsa başlasın hamle yapacak. polimorfizmin güzelliği de burada. kimin hamle yapacağını bilmiyoruz fakat davranışları farklı olsa da her iki
# sınıfta da hamle_yap metodunun tanımlı olduğunu biliyoruz:
beyazlar.hamle_yap()
# bu sayede rastgele bir obje üzerinde her seferinde aynı metodu çalıştırarak farklı bir sonuç elde ediyoruz.
