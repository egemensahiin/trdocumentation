import unittest

class DogrulukTesti(unittest.TestCase):

    def test_dogrumsuluk(self):
        # diğer assett metodlarının aksine dogruluk yanlıslık testleri tek arguman alır ve bunların doğrumsuluğu
        # veya yanlışımsılığını kontrol eder.
        self.assertTrue(3 < 5)
        self.assertTrue(1)
        self.assertTrue("egemen")
        self.assertTrue(["a"])
        self.assertTrue({1, 2})
        self.assertTrue({ "b": 5 })
    
    def test_yanlislik(self):
        self.assertFalse(3 > 5)
        self.assertFalse(0)
        self.assertFalse("")
        self.assertFalse([])
        self.assertFalse({})
        self.assertFalse(dict())

if __name__ == '__main__':
    unittest.main()