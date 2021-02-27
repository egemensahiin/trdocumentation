import unittest

# çok uzun kodlarda bazen bir hataya odaklanmak için diğer testleri geçerek programın çalışma süresini kısaltmak isteyebiliriz. bunun için
# unittest modülünde bulunan bir fonksiyon olan skip() fonksiyonundan faydalanırız.

# mesela bu kullanım durumunda saçma sapan işlem fonksiyonları tanımlamış olalım ve bunların testlerini yazalım

def ustel(a, b):
    sonuc = 1
    for _ in range(b):
        sonuc *= a
    return sonuc

def carp(a, b):
    sonuc = 0
    for _ in range(b):
        sonuc += a
    return sonuc

def bol(a, b):
    pass

class IslemTestleri(unittest.TestCase):
    def test_ustel(self):
        self.assertEqual(ustel(3, 2), 9)
    def test_carp(self):
        self.assertEqual(carp(3, 4), 12)
    # içersine pass yazılan veya başka bir deyiişle içersinde test bulunmayan test metodları default olarak başarılı kabul edilir. şimdi bolme
    # işlemi için test yazmadığımızı farz edelim. bu durumda bu testi boş yere çalıştırmamız, özellikle daha uzun programlarda testi gözden
    # kaçırmamıza sebep olabilir. bu sebeple modülü skip dekotatörü ile yazarız:
    @unittest.skip("Daha sonra yazılacak.")
    # skip fonksiyonu bir argüman ister. bu argüman bir string olup esasında 
    def test_bol(self):
        pass

if __name__ == "__main__":
    unittest.main()
    # çıktıyı inceleyecek olursak en üstteki test indikatörlerinde farklı olarak "s" karakterini görürüz. bu da testlerden birinin geçildiği
    # anlamına gelir. testlerin en sonunda da "skipped=1" ifadesi ile bir testin geçilmiş olduğu zaten belirtilmiştir.