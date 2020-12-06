# __eq__ metoduna benzer şekilde küçüktür, küçük eşittir, büyüktür, büyük eşittir ve eşit değildir karşılaştırmaları için de python'da dunder metodlar
# bulunur. bunlar sırasıyla __lt__, __le__, __gt__, __ge__ ve __ne__ metodlarıdır ve __eq__ ile aynı şekilde çalışır. yine aynı mantıkla sınıflarımızı
# matematiksel operasyonlarda kullanılabilir hale de getirebiliriz. bu defa elbetteki çıktı olarak boolean değil matematiksel operasyonun sonucunu ve-
# recekler. bu operasyonlar toplama, çıkarma, çarpma ve bölmedir. bunlar için kullanılan dunder metodlar ise sırasıyla; __add__, __sub__, __mul__,
# __truediv__ (/ şeklinde bölme) ve __floordiv__ (// şeklinde bölme), metodlarıdır. ayrıca üs (__pow__) ve moduler aritmetik (__mod__) işlemleri ve da-
# ha da fazlası tanımlanabilmektedir.
class Üçgen():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    @property
    def çevre(self):
        return self.a + self.b + self.c
    # karşılaştırma operatörlerimize bakalım:
    def __eq__(self, anotherObj):
        return self.çevre == anotherObj.çevre
    def __ne__(self, anotherObj):
        return self.çevre != anotherObj.çevre
    def __lt__(self, anotherObj):
        return self.çevre < anotherObj.çevre
    def __le__(self, anotherObj):
        return self.çevre <= anotherObj.çevre
    def __gt__(self, anotherObj):
        return self.çevre > anotherObj.çevre
    def __ge__(self, anotherObj):
        return self.çevre >= anotherObj.çevre
    # şimdi de matematiksel operasyonları tanımlayalım
    def __add__(self, anotherObj):
        return self.çevre + anotherObj.çevre
    def __sub__(self, anotherObj):
        return self.çevre - anotherObj.çevre
    def __truediv__(self, anotherObj):
        return self.çevre / anotherObj.çevre
    def __mul__(self, anotherObj):
        return self.çevre * anotherObj.çevre
    def __pow__(self, anotherObj):
        return self.çevre ** anotherObj.çevre
    def __mod__(self, anotherObj):
        return self.çevre % anotherObj.çevre

ü1 = Üçgen(3, 4, 5)
ü2 = Üçgen(6, 7, 8)
print(ü1 - ü2)
print(ü1 <= ü2)
print(ü1 / ü2)