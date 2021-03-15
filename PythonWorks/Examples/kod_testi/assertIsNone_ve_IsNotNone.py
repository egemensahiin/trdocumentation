import unittest
# bir objenin "None" olup olmadığını test etmek mantıklı gelmeyebilir çünkü "None" hariç tüm objeler "None değil"dir.
# fakat yine de bu fonksiyonun da kullanım durumları vardır. mesela bir fonksiyon, hiçbir değer return etmediğine None
# tipindedir ve bunu test etmek için bu fonksiyonlardan faydalanabiliriz.

def icsel_toplama(a, b):
    # bu fonksiyon a ve b'nin toplamını yazdırır ama return etmez yani çıktısı None olur.
    print(a + b)

def dissal_toplama(a, b):
    return a + b

class NoneTesti(unittest.TestCase):
    
    def test_fonksiyonlar(self):
        self.assertIsNone(icsel_toplama(3 ,4))
        self.assertIsNotNone(dissal_toplama(3 ,4))

if __name__ == "__main__":
    unittest.main()