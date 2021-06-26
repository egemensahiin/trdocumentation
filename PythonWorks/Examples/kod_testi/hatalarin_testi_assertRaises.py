import unittest

# assertRaises fonksiyonu, bir hataya dair varsayımımızı test etmek için kullanılır. örnek vermek gerekirse:
def sayilari_bol(a, b):
    if b == 0:
        raise ZeroDivisionError # fonksiyona y'nin 0 olması durumunda kasıtlı olarak hata verdirdik.
    return a / b

# şimdi fonksiyonumuzun istediğimiz durumda istediğimiz hatayı verip vermediğini görmek için assertRaises fonksiyonunu kullanalım:
class HatayiTestEt(unittest.TestCase):
    def test_bolum(self):
        # assertRaises 2 argüman kabul eder. bunlardan ilki alınmak istenen hata, diğer ise test edilecek fonksiyondur (fonksiyonun
        # örneklemi değil kendisi). eğer test edilen fonksiyon argüman kabul ediyorsa, bunlar devamında teker teker argüman olarak
        # verilmelidir. assertRaises fonksiyonu verildiği kadar pozisyonel argüman (*args) ve keyword argüman (**kwargs) kabul eder
        # ve bunları, 2. argüman olarak verilen fonksiyondan geçirerek bu durumda ilk argümandaki hatanın verilip verilmediğini test
        # eder.
        self.assertRaises(ZeroDivisionError, sayilari_bol, 10, 0)

    def test_alternatif(self):
        # assertRaises fonksiyonun alternatif bir syntaxı da with keywordü ile birlikte kullanımıdır. yalnızca beklenen hata verilerek
        # assertRaises fonksiyonu with ile açılır ve with bloğunda test edilecek örneklem yazılır.
        with self.assertRaises(ZeroDivisionError):
            sayilari_bol(10, 0)

if __name__ == "__main__":
    unittest.main()
