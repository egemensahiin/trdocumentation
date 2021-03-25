import unittest
from unittest.mock import MagicMock

# mockların bir özelliği de çağırılıp çağırılmadıkları, kaç defa çağırıldıkları, hangi argümanlarla çağırıldıkları vb. niteliklerini
# saklayabilmeleri ve bu niteliklerin test edilebilir olmasıdır. bu bağlamda uniitestler ile mockları ilk defa bir arada kullanacağız:
class MockCagirimTestleri(unittest.TestCase):
    def test_cagirildi_mi(self):
        # bir mock'un hiç çağırılıp çağırılmadığını test etmek için özel bir örneklem metodu kullanılır; assert_called. önce bir
        # magic mock örnekleyelim:
        mock = MagicMock()
        mock() # şimdi de bunu çağıralım:
        mock.assert_called()
        # assert_called, mock objesinin EN AZ 1 defa çağırıldığını varsayar ve test eder. yani mock objesini bir kaç defa daha çağırıp
        # assert_called metodunu çalıştırırsak yine testimiz geçer. fakat 11. satırı yorumlarsak testimiz geçemez.
    
    def test_cagirilmadi_mi(self):
        # assert_called un tamamlayıcısı niteliğinde bir başka özel mock metodu da assert_not_called metodudur ve tam da adından anlaşıldığı
        # gibi söz konusu mıck objesinin çağırılmamış olduğunu test eder:
        mock = MagicMock()
        mock.assert_not_called()

    def test_ne_ile_cagirildi(self):
        # faydalı bir başka metod da assert_called_with metodudur. bu metod, söz konusu mock objesinin kendisine verilen argümanlarla (kısmi
        # karşılaştırma yapmaz birebir aynı argümanları aynı sırada karşılaştırır) çağırılıp çağırılmadığını test eder:
        mock = MagicMock()
        mock(1, 2, 3)
        mock.assert_called_with(1, 2, 3) # 1, 2 veya 1, 3, 2 vs verildiğinde başarısız test alınır.

    def test_mock_nitelikleri(self):
        # mocklar üzerinde daha spesifik metodlar da mevcuttur; mockun bir defa çağırıldığını varsayan, verilen sayı kadar çağırıldığını varsayan
        # vs. bunlar dökümantasyonda bulunabilir. bir de mockların özel nitelikleri vardır. bu niteliklerden bazıları mockun kaç defa çağırılmış
        # olduğunu, nasıl çağırıldığını verir.
        mock = MagicMock()
        mock()
        mock(1, 2)
        print(mock.called)
        print(mock.call_count)
        print(mock.mock_calls)

if __name__ == "__main__":
    unittest.main()