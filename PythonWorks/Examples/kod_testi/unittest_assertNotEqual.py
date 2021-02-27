import unittest

# assertNotEqual metodu, tam da isminden anlaşılan şeyi yapar: bir varsayımın eşit olup olmadığına bakar. mesela listelere eleman ekleyen bir 
# fonksiyon yazalım:

def elemanEkle(liste, eleman):
    kopya = liste
    kopya.append(eleman)
    return kopya

def duzgunEkle(liste, eleman):
    kopya = liste[:]
    kopya.append(eleman)
    return kopya

# burada özellikle bir hata yaptık. normalde bir listeyi kopyalayarak eleman eklemek için listenin kendisini kopyalamayız. listeyi baştan sona
# indeksler (liste[:]) ve bunu kopyalarız. çünkü bu durumda kopya değişkeni listenin kendisine referans olduğu için append metodu listenin
# kendisini değiştirecektir. mesela bunu test etmek için assertNotEqual metodu oldukça faydalıdır.

class TestlerTestlerimiz(unittest.TestCase):
    def test_esit_mi(self):
        degerler = [1, 2, 3]
        sonuc = elemanEkle(degerler, 4)
        self.assertEqual(sonuc, [1, 2, 3, 4])
    def test_degisti_mi(self):
        degerler = [1, 2, 3]
        sonuc = elemanEkle(degerler, 4)
        self.assertNotEqual(degerler, [1, 2, 3, 4], "Başlangıçta verilen liste değişime uğramış.")
        # üçüncü argüman olarak verilen string mesajdır ve AssertionError ile gösterilir (assertEqual'da da kullanılabilir).
    def test_olmasi_gereken(self):
        degerler = [1, 2, 3]
        sonuc = duzgunEkle(degerler, 4)
        self.assertNotEqual(degerler, [1, 2, 3, 4], "Başlangıçta verilen liste değişime uğramış.")
        # buradan failure almadık çünkü bu sefer baştaki liste değişmedi.

if __name__ == "__main__":
    unittest.main()