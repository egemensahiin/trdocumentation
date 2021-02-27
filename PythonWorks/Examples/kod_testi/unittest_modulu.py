# kodların test edilmesinde kullanılan bir başka araç da unittest modülüdür. unittest modülünü kullanarak kodlarımızı test etmek için bir test sınıfı olu-
# şturmamız gerekir. bu test sınıfı, unittest modülünde yer alan başka bir sınıf olan TestCase sınıfının alt sınıfı olarak tanımlanmalıdır.
import unittest

class StringMetodTestleri(unittest.TestCase):
    def test_split(self):
        pass
    # TestCase altsınıfları, örneklem metodu olarak verilen ifadeleri test eder. test edilmek istenen modül isimleri, "test" kelimesiyle başlamalıdır. ayrı-
    # ca bunlar örneklem metodları oldukları için en az bir argüman belirtilmelidir ve ilk argüman sınıfın örnekleminin kendisidir.

if __name__ == "__main__":
    # unittest testleri, modüldeki main() fonksiyonuyla çalıştırılır.
    unittest.main()