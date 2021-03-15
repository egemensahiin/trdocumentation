import unittest
# assertIn ve NotIn fonksiyonları, bir objenin başka bir iterable obje içinde bulunduğunu veya bulunmadığını varsayar.
# aslında bu amaçla assertIsTrue ve False, in veya not in keywordü ile kullanılabilir fakat bu durumda hata mesajı,
# ifadenin doğruluğu üzerine olacaktır. kodun okunurluluğu kadar hataların okunurluluğu da önemlidir bu sebeple assertIn
# ve NotIn kullanımı genellikle daha iyi bir pratiktir.

class InVeNotInTestleri(unittest.TestCase):

    def test_icinde(self):
        self.assertIn("e", "egemen")
        self.assertIn(1, [1, 2, 3])
        self.assertIn(7, (6, 7, 8))
        self.assertIn("a", { "a": 1, "b": 2 }) # in ve not in ile sozluklerdeki "key"ler kontrol edilir.
        self.assertIn("a", { "a": 1, "b": 2 }.keys())
        self.assertIn(2, { "a": 1, "b": 2 }.values())
        self.assertIn(55, range(50, 60))
    
    def test_disinda(self):
        self.assertNotIn("b", "egemen")
        self.assertNotIn(5, [1, 2, 3])
        self.assertNotIn(2, (6, 7, 8))
        self.assertNotIn("c", { "a": 1, "b": 2 }) # in ve not in ile sozluklerdeki "key"ler kontrol edilir.
        self.assertNotIn("c", { "a": 1, "b": 2 }.keys())
        self.assertNotIn(5, { "a": 1, "b": 2 }.values())
        self.assertNotIn(60, range(50, 60)) # hatırlatma olsun range fonksiyonu 2. argümanı exclusive

if __name__ == "__main__":
    unittest.main()