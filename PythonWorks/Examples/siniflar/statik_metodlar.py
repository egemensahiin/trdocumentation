# hatırlanacağı üzere örneklem metodları, objenin kendisini; sınıf metodları ise sınıfı refere eden metodlardı. statik metodlar ise sınıfı veya örneği
# refere etmezler ve kullanmazlar. hem sınıfın kendisi hem de objelerinde çalıştırılabilen bu metodlar esasında kolaylık sağlaması için sınıfın gövde-
# sinde tanımlanan normal fonksiyonlardır ve staticmethod dekoratörüyle tanımlanırlar. bazı geliştiriciler statik metodların gereksiz olduğunu ve düz
# fonksiyonların bu amaçla daha kullanışlı olduğunu düşünmektedir. haksız sayılmazlar fakat en nihayetinde statik metodlar vardır.
# hava tahminlerini içeren bir sınıf ve bu sınıf için, listedeki tüm sıcaklıkları fahrenheit a çeviren bir örneklem metodu yazalım. örneklem metodumuzu
# list comprehension mantığıyla yapmak, bu durumda mantıklı olacaktır fakat çevrilen sayının hesaplanması ve yuvarlanması tek satırda yazılamayacağın-
# dan (esasında yazılır da örnek olsun işte) sınıf içersinde bir statik metod tanımlayarak hesaplamayı yapabiliriz.
class HavaTahmini():
    def __init__(self, sıcaklıklar):
        self.sıcaklıklar = sıcaklıklar
    # şimdi de statik metodumuzu tanımlayalım:
    @staticmethod # burada statik metod kullanmak istememizin sebebi, yapacağımız hesaplamanın sınıfın kendisi veya objeyle bir işi olmaması.
    def çevir(celcius): # statik metodlarda obje veya sınıf refere edilmediğinden doğrudan kullanılacak nitelikler tanımlanır.
        hesap = celcius * (9 / 5) + 32
        return round(hesap, 2)
    # örnek metodumuzu tanımlayalım:
    def fahrenheit_olarak(self):
        return [self.çevir(sıcaklık) for sıcaklık in self.sıcaklıklar] # görüldüğü gibi çevir metodunu obje üzerinde çağırdık.

tahmin = HavaTahmini([20, 25, 30, 35])
print(tahmin.fahrenheit_olarak())

# statik metodlar ayrıca sınıf metodları gibi de kullanılabilir:
print(HavaTahmini.çevir(40))