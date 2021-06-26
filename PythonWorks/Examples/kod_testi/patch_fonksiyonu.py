# patch fonksiyonu hem bir fonksiyon hem de bir dekoratör olarak kullanılabilir. bir modüldeki halihazırda var olan bir objenin yerine
# bir magic mock üretir. bir objeyi işaret eden ismi, geçici olarak bir mock ile değiştirerek çalışmaktadır. bu da kodumuz içersinde
# olmayan hiyerarşik iç içe yapıdaki objeler, sınıflar gibi karmaşık kodların mock edilmesinde oldukça güçlü bir araç olarak
# kullanılmasını sağlar.

# örnek vermek için urllib kütüphanesini import edelim ve bir WebRequest sınıfı oluşturalım:
import urllib
import unittest
from unittest.mock import patch

class WebRequest():
    def __init__(self, url):
        self.url = url
    def calistir(self):
        # bir url'yi açmak için urllib kütüphanesindeki request modülünden faydalanılır. bu modüldeki
        # urlopen fonksiyonu, bir url'ye istek gönderir ve çıktı olarak urlnin cevabını verir.
        cevap = urllib.request.urlopen(self.url)
        # bu cevabın bir status niteliği vardır. status'u 200 olan cevaplar başarılı, 200'den farklı olanlar
        # hatalı cevaplardır.
        if cevap.status == 200:
            return "BASARILI"
        return "BASARISIZ"

# şimdi geldik teste. url istekleri gibi veritabanlarına veya internet adreslerine erişim gerektiren işler yavaş, karmaşık yapılı
# işlerdir. fakat biz testlerimizin hızlı çalışmasını ve olabildiğince izole olmasını isteriz. bütün bir urllib kütüphanesine, test
# edilecek websitesinin durumuna ve internet bağlantısına dayanan bir test, unittest mantığına aykırı olacaktır. bu sebeple, urlopen
# niteliğine erişmek için patch fonksiyonunu kullanabiliriz.
class WRTest(unittest.TestCase):
    def test_basarili_cevap(self):
        # yapmak istediğimiz, test sırasında programın 17. satıra geldiğide bir mock objesi oluşturmasıdır.
        # bu sebeple 'urllib.request.urlopen' niteliğini patch ediyoruz. patch, argüman alırken söz konusu niteliğin
        # çağırımıyla aynı syntaxı bekler yani 'kütüphane.metod.nitelik'. patch edilmiş metodu, with ile test ediyoruz:
        with patch('urllib.request.urlopen') as mock_istek:
            # aşağıdaki kodun çalışmasından da görülebileceği gibi buradaki mock_istek, bir mock objesi ve urllib.request.urlopen'ın
            # yerini tutuyor:
            print(mock_istek)
            # metoddaki cevap ismi, bu urlopen objesini return değeri. o yüzden bu return değeri üzerinde yani magic mocklarda tanımlı
            # return_value üzerindeki status değerine erişmemiz gerek. bunun için nokta syntaxıyla status niteliğini 200 yaparak başarı
            # senaryosunu mock ediyoruz:
            mock_istek.return_value.status = 200
            # şimdi bir webrequest örneklemi üzerinde calistir metodunu çalıştırdığımızda, basarili bir urlopen durumunu taklit edecek:
            wr = WebRequest('https://www.debian.org')
            self.assertEqual(wr.calistir(), 'BASARILI')

    # ornek olması açısından başarısız senaryoyu da patch ile test edelim:
    def test_basariz_cevap(self):
        with patch('urllib.request.urlopen') as mock_istek:
            mock_istek.return_value.status = 404
            wr = WebRequest('https://www.debian.og')
            self.assertEqual(wr.calistir(), 'BASARISIZ')

if __name__ == "__main__":
    unittest.main()
