# sınıflara metod tanımlarken daha önce de bahsettiğimiz gibi fonksiyon tanımlama syntaxını kullanırız.
class Büyücü():
    # her şeyden önce __init__ metodumuzu tanımlayıp nitletiklerimizi atayalım:
    def __init__(self, isim, bina, sağlık = 100):
        self.isim = isim
        self.bina = bina
        self.sağlık = sağlık
    # şimdi de diğer metodlarımızı tanımlayalım. 
    # mesela metodlarda fonksiyon çalıştırabiliriz.
    def büyü(self): # tüm metodların ilk argümanı zorunludur ve örneğin, objenin kendisini refere eder.
        print("Expeliarmus!")
    # metodlarda, sınıfa ait nitelikleri kullanabiliriz:
    def tanım(self):
        # nitelikleri metodların içersinde çağırırken nokta syntaxını kullanırız çünkü niteliklerin isim alanı objenin kendisitle sınırlıdır.
        print(f"Benim adım {self.isim} ve {self.bina} binasındanım.")
    # ayrıca metodlarda mevcut niteliklerin durumunu da değiştirebiliriz:
    def hasar_alım(self, hasar_miktarı): # __init__ metodunda olduğu gibi diğer metodlar da objenin kendisinden başka argümanlar kabul edebilir.
        self.sağlık -= hasar_miktarı
    
# şimdi sınıfımızı örneklendirip metodlarımızı test edelim:
malfoy = Büyücü("Draco Malfoy", "Slytherin")
potter = Büyücü(
    isim = "Harry Potter",
    bina = "Griffindor",
    sağlık = 110
)

malfoy.büyü() # çıktıda gördüğümüz gibi metodumuz çalıştı ve "Expeliarmus!" stringi print edildi.
potter.tanım() # yine çıktıda gördüğümüz gibi örneklendirme yaparken atadığımız niteliklerin durumları metodda kullanılmış.
print(malfoy.sağlık)
malfoy.hasar_alım(20)
print(malfoy.sağlık) # malfoy için sağlık niteliğini ilk çağırdığımızda 100 çıktısını alırken hasar_alım metoduyla sağlık niteliğinin durumunu değiştir-
# dik ve sağlık niteliğini tekrar çağırdığımızda farkı gördük.
# mevcut nitelikleri nokta syntaxıyla değiştirmemiz de mümkün:
print(potter.sağlık)
potter.sağlık = 60
print(potter.sağlık)