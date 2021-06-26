# patch fonksiyonunu with bloğu içersinde bir fonksiyon olarak çağırmak yerine bir test metoduna dekoratör olarak çağırmak da mümkün
# ve daha yaygındır. syntax oldukça benzer, yine patch dekoratör fonksiyonuna patch edilmek istenen ismin tüm isim alanı verilir.
# farklı olarak verilen ismi temsil etmesi için as keywordü kullanılmaz, dekore edilen metoda verilen ikinci argüman, patch edilen
# ismi temsil eden mock için değişkendir.

import urllib
import unittest
from unittest.mock import patch

class WebRequest():
    def __init__(self, url):
        self.url = url
    def calistir(self):
        cevap = urllib.request.urlopen(self.url)
        if cevap.status == 200:
            return "BASARILI"
        return "BASARISIZ"

class WRTest(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_basarili_cevap(self, mock_istek): # bu sefer gerekli değişkeni burada yazdık.
        print(mock_istek)
        mock_istek.return_value.status = 200
        wr = WebRequest('https://www.debian.org')
        self.assertEqual(wr.calistir(), 'BASARILI')

    # ornek olması açısından başarısız senaryoyu da patch ile test edelim:
    @patch('urllib.request.urlopen')
    def test_basariz_cevap(self, mock_istek):
        mock_istek.return_value.status = 404
        wr = WebRequest('https://www.debian.og')
        self.assertEqual(wr.calistir(), 'BASARISIZ')

if __name__ == "__main__":
    unittest.main()
