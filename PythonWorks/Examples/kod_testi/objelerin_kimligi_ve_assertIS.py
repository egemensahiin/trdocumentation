import unittest

# daha önce objelerin eşitliğinin ve aynılığının birbirinden farklı olduğundan bahsetmiştik. eşit objeler, birbirinin aynı
# değerleri içermesine karşın fakrlı değişkenlere atandıkları için hafızada farklı yerlerde tutulurlar. birbirinin aynı olan
# yani aynı "kimliğe" sahip objeler ise birbirine eş olmakla kalmaz hafızada da aynı yeri tutarlar. assertEqual ve assertNotEqual
# iki objenin eşitliğini veya eşitsizliğini varsayarken assertIs ve assertIsNot iki objenin aynılığını veya aynı olmayışını
# varsayar.

class KimlikTestleri(unittest.TestCase):

    def test_esitlik(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        # bu durumda a ve b birbirinin aynıdır, hafızada aynı yere işaret eden değişkenlerdir fakat c hem a'ya hem de b'ye eşit
        # olmasına karşın bunlardan farklıdır.
        self.assertEqual(a, b)
        self.assertEqual(a, c)
        # bu iki test de başarılı olur.
    
    def test_aynilik(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        self.assertIs(a, b)
        self.assertIsNot(a, c)
        self.assertIsNot(b, c)
        # bu testlerin üçü de başarılıdır. çünkü a b'dir ve b de a'dır fakat c, a da b de değildir.

    def test_basarisiz(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        self.assertIsNot(a, b)
        self.assertIs(a, c)
        self.assertIs(b, c)
        # bu testlerin 3'ü de hatalıdır. verir.

if __name__ == '__main__':
    unittest.main()