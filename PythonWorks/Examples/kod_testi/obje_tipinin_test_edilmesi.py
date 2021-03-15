import unittest

class Araba():
    
    def __init__(self, hiz, model):
        self.hiz = hiz
        self.model = model

dogan = Araba(70, 1971)

class TypeTesti(unittest.TestCase):
    
    def test_orneklem(self):
        # assertsIsInstance ve assertNotIsInstance fonksiyonları, bir objenin herhangi bir sınıfın örneklemi olup
        # olmadığını test eder. ilk argüman olarak örneklem, ikinci argüman olarak ise sınıfın kendisini (dikkat,
        # string falan değil direkt sınıfın kendisi) alır.
        self.assertIsInstance(1, int)
        self.assertIsInstance("egemen", str)
        self.assertIsInstance({ "a": 5 }, dict)
        # kendi oluşturduğumuz sınıflar için de kullanılabilir:
        self.assertIsInstance(dogan, Araba)

        # assertNotIsInstance da bunun tamamlayicisidir.
        self.assertNotIsInstance(["egemen"], str)
        self.assertNotIsInstance(5.3, int)
        self.assertNotIsInstance(dogan, dict)

if __name__ == "__main__":
    unittest.main()