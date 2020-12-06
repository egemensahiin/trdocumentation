class Hayvan():
    def __init__(self, isim, tür, yaş):
        self.isim = isim
        self.tür = tür
        self.yaş = yaş
    def yemek(self, yemek):
        return f"{self.isim}, {yemek} yemeyi sever."

# şimdi boş bir subclass tanımlayıp öncelikle argüman kabul etme durumundaki davranışı görelim:
class At(Hayvan):
    pass

# boldy = At() # yazımı TypeError verir çünkü __init__ metodu miras alındığında, subclassın örneklemlerinden de aynı argümanları bekler.
boldy = At("Bold Pilot", "Equus ferus caballus", 12)
print(boldy.isim)
# şimdi super fonksiyonuna geçebiliriz. super fonksiyonu, bir altsınıfta ihtiyaç duyduğumuz durumlarda üst sınıfı refere eder. mesela bir köpek altsınıfı
# tanımlayalım ve hayvan sınıfına ek olarak cins argümanı da alsın. bunu şu şekilde yapmak inheritance'ın bütün mentalitesine AYKIRIdır:
class Köpek(Hayvan):
    def __init__(self, isim, tür, yaş, cins):
        self.isim = isim
        self.tür = tür
        self.yaş = yaş
        self.cins = cins
        # bu yöntem, gereksiz bir şekilde kodu uzatmaktan ziyade mesela isim niteliğini, tüm Hayvan ve altsınıfları için ön_isim şeklinde değiştirmek is-
        # tediğimizde işimizi uzatır. bunun için super fonksiyonu kullanılır:

class Kedi(Hayvan):
    def __init__(self, isim, tür, yaş, cins):
        super().__init__(isim, tür, yaş) # yani ne yaptık; superclassın init metodunu, subclassın pozisyonal argümanlarıyla çalıştırdık. şimdi de ekstra
        # yanımlayacağımız cins niteliğini tanımlayabiliriz.
        # esasında Hayvan üst sınıfı, doğrudan da altsınıflarının gövdesinde çağrılabilir. yani 29. satır ile Hayvan.__init__(...) aynı şeydir fakat super
        # fonksiyonu daha iyi bir pratiktir çünkü birden fazla kez üstsınıfı refere ettiğimiz durumlarda, üst sınıfın ismini değiştirdiğimizde yalnızca
        # altsınıf tanımlanırken verdiğimiz argümanı değiştirmemiz yeterli olacaktır.
        self.cins = cins

bor = Köpek("Bor", "Canis familiaris", 6, "Alabay")
şampiyon = Kedi("Şampiyon", "Felis catus", 2, "Chinchilla")
print(bor.isim)
print(şampiyon.isim)
print(bor.cins)
print(şampiyon.cins)
# gördüğümüz gibi her iki alt sınıf da istediğimiz niteliklere sahip ama super fonksiyonu ile kedi altsınıfında yaptığımız nitelik ataması hem daha şık
# hem daha fonksiyonel hem de inheritance tasarımına daha uygun.
