# kodların test edilmesinde kullanılan bir başka araç da unittest modülüdür. unittest modülünü kullanarak kodlarımızı test etmek için bir test sınıfı olu-
# şturmamız gerekir. bu test sınıfı, unittest modülünde yer alan başka bir sınıf olan TestCase sınıfının alt sınıfı olarak tanımlanmalıdır.
import unittest

class StringMetodTestleri(unittest.TestCase):
    def test_split(self):
        pass
    # TestCase altsınıfları, örneklem metodu olarak verilen ifadeleri test eder. test edilmek istenen modül isimleri, "test" kelimesiyle başlamalıdır. ayrı-
    # ca bunlar örneklem metodları oldukları için en az bir argüman belirtilmelidir ve ilk argüman sınıfın örnekleminin kendisidir.

# if __name__ == "__main__":
#     # unittest testleri, modüldeki main() fonksiyonuyla çalıştırılır.
#     unittest.main() # main() çalıştırıldıktan sonra program çıkış yapar. bu sebeple buraları commentliyoruz.

# ~~~~~~~~~~~~~~~~~~ assertEqual ~~~~~~~~~~~~~~~~~~ #
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
        # görülebileceği üzere başarısız bir çıktıda en üstte F.. ve altında FAIL uyarısı mevcut. FAIL, bize başarısız olan
    
    def test_bu_da_basarisiz(self):
        self.assertEqual("1/2/3".split("/"), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()