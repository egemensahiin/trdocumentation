import unittest
# hatırlayacağımız üzere inheritance'ın mantığı, bir sınıfın sahip olduğu işlevlerin, altsınıflarda da bulunmasıdır. TestCase altsınıflarında da yani test
# sınıflarımızda da sıklıkla TestCase sınıfının isimlerini kullanıyoruz. bunlardan en sık kullanılanı assertEqual metodudur.
# hatırlayacağımız üzere testlerin temelini assertion konsepti oluşturmaktadır. assertEqual metodu, verilen iki ifadenin eşitliğini doğrular. iki argüman
# kabul eder ve bu argümanlardan biri test etmek istediğimiz işlevselliği (sınıf, metod, fonksiyon vs) içeren bir ifadedir ve basitçe bu işlevin çıktısını
# ifade eder; ikincisi ise bizim bu kodun çalışmasından beklediğimiz çıktıdır. bu iki çıktı birbirinin aynı olduğunda, varsayım başarılıdır ve test geçilir.

class StringMetodTestleri(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        # bir metodda yapılan iki varsayım, iki test etmez. her bir test metodu tek bir testtir ve her metodda yalnız bir defa test yapmak daha iyi bir
        # pratiktir. ama tabii ki imkansız değil. eğer kodun daha güvenli olması isteniyorsa farklı bir durumda aynı işlev tekrar teste tabii tutulabilir.
        self.assertEqual("1, 2, 3".split(", "), ["1", "2", "3"])
    
    def testbasarili(self):
        # dikkat edilebileceği üzere main() çalıştırıldığında üstte noktalar çıkmaktadır. bu noktalar yürütülen testleri ifade eder ve test edilen varsayım
        # doğrulanamamışsa nokta yerine "F" yazar.
        pass

    def test_basarisiz(self):
        self.assertEqual("d.e.f".split("."), ["e", "d", "f"])
    
    def test_bu_da_basarisiz(self):
        self.assertEqual("1/2/3".split("/"), [1, 2, 3])
        # görülebileceği üzere başarısız bir çıktıda en üstte FF.. ve altında FAIL uyarısı mevcut. FAIL, bize başarısız olan testin hangisi olduğunu söy-
        # lüyor altında Traceback mesajını görüyoruz çünkü kaynağında assertEqual metodu arkaplanda assert keywordünü çalıştırıyor ve bu da varsayımlar
        # yanlış olduğunda AssertionError veriyor. peki neden assert keywordü yerine unittest kullanalım? çünkü farkedilebileceği gibi hata mesajlarını
        # görmemize karşın ilk hatada yani 35. satırda program durmadı ve bize 38. satırdaki varsayımımızın da yanlış olduğunu gösterdi. Tracebackin ar-
        # dından da doğrulanmaya çalışılan ifadelerin çıktılarını görüyoruz. bundan sonra da diğer yanlış varsayımın çıktılarını gösteriyor ve en son yü-
        # rütülen test sayısı ve başarısız test sayısını yazıyor. biraz gevezelik gibi oldu ama unittest kullanılacaksa bu çıktıların doğru okunması ö-
        # nemli. test sonuçlarını anlamlandıramadıktan sonra unittesti kullanmanın hiçbir anlamı yok.

if __name__ == "__main__":
    unittest.main()