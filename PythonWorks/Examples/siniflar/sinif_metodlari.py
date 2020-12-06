# sınıflarda tanımladığımız metodlar normalde, sınıfın örneklemleri üzerinde çalıştırılır ve bu sebeple "örnek metodları" (instance methods) olarak ad-
# landırılırlar. bu metodlarda ilk argüman örneklemin kendisidir. fakat sınıflarda tanımlanan başka bir tür metod da "sınıf metodları" olup bu metod-
# lar sınıfın örneklemi değil sınıfın bizzat kendisiyle çalışmamıza olanak tanırlar. mesela bir SushiTabağı sınıfı tanımlayalım:
class SushiTabağı():
    def __init__(self, somon, tuna, karides, ahtapot):
        self.somon   = somon
        self.tuna    = tuna
        self.karides = karides
        self.ahtapot = ahtapot
    # sınıf metodları, builtin classmethod dekoratörü ile çağırılırlar ve ilk argümanları her zaman sınıfın kendisidir. bu sayede sınıf metodundan, ni-
    # telikleri atayarak değil sınıfı metod içersinde örnekleyerek mesela bir default konfigürasyon oluşturulabilir. örneğin bir öğlen menüsü konfigü-
    # rasyonu oluşturulım:
    @classmethod
    def öğlen_menüsü(cls): # örnek metodlarının aksine sınıf metodları örneklemi değil sınıfın kendisini argüman olarak kabul ettiği için bir topluluk
        # kuralı olarak bu argüman self değil class manasında cls olarak atanır.
        return cls(somon = 2, tuna = 2, karides = 2, ahtapot = 1)
    # mesela bir tane de somon sever menü oluşturalım:
    @classmethod
    def somon_sever_menü(cls):
        return cls(somon = 10, tuna = 0, karides = 0, ahtapot = 0)

# kendi siparişimizi normal bir örneklemle oluşturabiliriz:
egemen = SushiTabağı(somon = 4, tuna = 3, karides = 5, ahtapot = 2)
# bikaç niteliğe bakalım:
print(egemen.somon)
print(egemen.karides)
# mesela kendi menüsünü oluşturmak istemeyen biri sınıf metodları yardımıyla default konfigurasyonlardan biritle bir sipariş oluşturabilir:
beyaz_yakalı = SushiTabağı.öğlen_menüsü() # hatırlayacağımız üzere örnek metodlarını, sınıfın örneklemi üzerinde (mesela egemen.metod şeklinde) çalış-
# tırıyorduk. sınıf metodlarını ise doğrudan sınıfın kendisi üzerinde çalıştırıyoruz.
somon_aşığı = SushiTabağı.somon_sever_menü()
# şimdi buradan da bir kaç nitleiğe bakalım:
print(beyaz_yakalı.tuna)
print(somon_aşığı.somon)
