# setUp ve tearDown, test sınıfları üzerinde çalıştırılan örneklem metodlarıdır. test fixture oluşturmak için kullanılırlar.
# tanım olarak test fixture, test edilen bir sistemi (veya objeyi) oluşturan (construct) ve yapılandıran (configure) kod parçasıdır.
# bu sayede testler, test kurulumunun kendisi yerine varsayımlara odaklanabilir.
import unittest

# python gibi obje odaklı dillerde programlarımız bir iki fonksiyondan ve sınıftan oluşan programlar şeklinde değildir. genellikle bu
# fonksiyonlar, sınıflar, değişkenler vs birbirleriyle bağlantılıdır. bu bağlantıları test etmek istediğimizde veya niteliklerini başka
# sınıflardan/fonksiyonlardan alan sınıfları/fonksiyonları test etmek istediğimizde her test için bir "test ortamı" kurmamız gerekebilir.
# örnek olarak bir restoran tanımlayalım. bir restoranı tanımlamak için adresini ve sahibini de tanımlamalıyız:
class Adres():
    def __init__(self, ilce, sehir):
        self.ilce = ilce
        self.sehir = sehir

class Isletmeci():
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

class Restoran():
    def __init__(self, adres, isletmeci):
        self.adres = adres
        self.isletmeci = isletmeci

    @property
    def isletmeciYasi(self):
        return self.isletmeci.yas

    def ozetle(self):
        return f"Bu restoran {self.isletmeci.isim} tarafindan isletilmektedir ve {self.adres.ilce} ilcesinde bulunur."

# bu restoran objesiyle ilgili bir test yapmak için önce bir adres, sonra bir işletmeci son olarak da bunlarla tanımlanmış bir restoran
# örneklememiz gerekir. bunu her test için ayrı ayrı yapmak kod kalabalığıdır. bu örnekte fazla test yapmayacak olsak da 10-15 test yapılan
# kodlarda bile tek tek bunları tanımlamak testlerin pratikliğini öldürür.

class RestoranTesti(unittest.TestCase):
    # testlerimizi tanımlamadan önce setUp tanımlamamız lazım. adı üstünde setUp metodu altında test ortamımızı kuracağız. daha sonrasında
    # çalışan her testten önce setUp metodu çalışacak ve test ortamını hazırlayacak.
    def setUp(self):
        print("Burasi her testten once yazilacak.")
        adres = Adres("Balgat", "Ankara")
        isletmeci = Isletmeci("Caner", 45)
        # bunları tanımladıktan sonra sınıf içersindeki test metodlarının erişebilmesi için self ile birlikte restoranı tanımlayalım:
        self.niyaziKesim = Restoran(adres, isletmeci)

    def tearDown(self):
        # setUp'ın tamamlayıcısı niteliğinde olan tearDown da her testten sonra çalışır ve eğer gerekliyse her testten sonra test ortamını
        # sıfırlamak veya bilgi vermek için kullanılır. mesela test kurulumunda bir dosya oluşturuyorsak veya bir dosyaya yazıyorsak vs. bunları
        # tearDown metodunda sıfırlayabiliriz. şimdilik sadece bilgi vermek için kullanalım
        print("Burasi her testten sonra yazilacak.")

    # setUp ve tearDown her testten önce ve sonra çalıştığı için veribankalarına bağlanmak, internetten veri almak gibi işlemleri bu metodlarla her
    # testten önce/sonra yapmak pratik değildir. bu sebeple setUpClass ve tearDownClass sınıf metodları kullanılır. bunlar setUp ve tearDown gibi her bir
    # testten önce/sonra değil tüm test suitinden önce/sonra çalışır.
    @classmethod
    def setUpClass(cls):
        print("Burasi tum test suitinden once, bir kere yazilacak.")

    @classmethod
    def tearDownClass(cls):
        print("Burasi tum test suitinden sonra, bir kere yazilacak.")

    def testIsletmeciYasi(self):
        # artık tek yapmamız gereken, sınıf uzayında tanımlı niyaziKesim değişkenini test objesi olarak kullanmak.
        self.assertEqual(self.niyaziKesim.isletmeciYasi, 45)

    def testOzet(self):
        self.assertEqual(self.niyaziKesim.ozetle(), "Bu restoran Caner tarafindan isletilmektedir ve Balgat ilcesinde bulunur.")

    def testIsletmeciIsmi(self):
        self.assertEqual(self.niyaziKesim.isletmeci.isim, "Caner")

if __name__ == "__main__":
    unittest.main()
