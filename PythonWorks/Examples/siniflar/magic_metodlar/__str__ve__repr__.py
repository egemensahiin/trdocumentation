# hatırlanacağı üzere custom objeleri, print fonksiyonundan geçirdiğimizde, objenin sınıfı ve hafızadaki yerini çıktı olarak verir. fakat pythonun 
# built-in objeleri çoğunlukla print fonksiyonuyla string çıktıları verirler. bunu sağlan __str__ metodudur. __str__ metodu, bir string return eder ve
# bir örneklem objesidir. örneklemimizi print fonksiyonuna girdiğimizde eğer __str__ metodu varsa bu metodun çıktısı yazdırılır.
class Kart():
    def __init__(self, değer, tür):
        self.değer = değer
        self.tür = tür
c = Kart("Vale", "Kupa")
print(c) # görüldüğü gibi çıktı olarak objenin ait olduğu sınıfı ve hafızadaki yerini alıyoruz.

print()

class Kart():
    def __init__(self, değer, tür):
        self.değer = değer
        self.tür = tür
    # şimdi print fonksiyonuyla objemizin oluşturulduğu değer ve türü vermemizi sağlayan bir str metodu yazalım:
    def __str__(self): # str magic metodu bir örneklem metodu. bu sebeple ilk argüman self.
        return f"{self.tür} {self.değer}" 
c = Kart("Vale", "Kupa")
print(c) # burada ise 9. satırın aksine, objenin hafızadaki yeri değil, __str__ metodunun return ettiği string alınır.
# veya str fonksiyonu çıktısını da yazdırabiliriz. str fonksiyonu da çıktı olarak __str__ metodunun return ettiği stringi verir.
print(str(c))

print()

# __repr__ de __str__'a benzer fakat __str__ın aksine daha teknik amaçlıdır. toplulukta genellikle __repr__, verilen objenin nasıl oluşturulacağını an-
# latan bir string verir ki dökümantasyonda da repr() fonksiyonu ve __repr__metodu bu şekilde tanımlanmıştır.
class Kart():
    def __init__(self, değer, tür):
        self.değer = değer
        self.tür = tür
    def __str__(self):
        return f"{self.tür} {self.değer}" 
    # burada da bu objemizi nasıl oluşturabileceğimizi anlatan bir string yazacağız.
    def __repr__(self):
        return f'Kart("{self.değer}", "{self.tür}")'
c = Kart("Vale", "Kupa")
print(c)
# repr metodunun çıktısı repr builtin fonksiyonu ile alınır.
print(repr(c))

print()

# eğer sınıfımızda __str__ metodu yoksa, str fonksiyonu veya print fonksiyonu fallback çıktısı olarak __repr__ metodunun return değerini alır.
class Kart():
    def __init__(self, değer, tür):
        self.değer = değer
        self.tür = tür
    def __repr__(self):
        return f'Kart("{self.değer}", "{self.tür}")'
c = Kart("Vale", "Kupa")
print(c)
print(str(c))
print(repr(c))

print()

# her iki dunder metodunu da düşündüğümüzde esasında str() ve repr() fonksiyonlarını çalıştırdığımızda olan şey, arkaplanda obje.__str__() ve
# obje.__repr__() metodlarının çalıştırılmasıdır.
class Kart():
    def __init__(self, değer, tür):
        self.değer = değer
        self.tür = tür
    def __str__(self):
        return f"{self.tür} {self.değer}" 
    def __repr__(self):
        return f'Kart("{self.değer}", "{self.tür}")'
c = Kart("Vale", "Kupa")
print(c.__repr__())
print(c.__str__()) # giriş kısmında dunder metodlar çoğunlukla kendi başlarına kullanılmaz derken kastettiğimiz şey buydu. eğer yazığımız objenin str-
# ing çıktısını almak istersek objemiz üzerinde __str__ metodunu çalıştırmak yerine str fonksiyonu ile stringi elde ederiz.