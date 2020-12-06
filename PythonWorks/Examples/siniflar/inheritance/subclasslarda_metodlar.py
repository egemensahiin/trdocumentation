# elbette inheritance tasarımını, sınıftaki tüm nitelikleri aktarmak için değil, ek özelliklere sahip bir altsınıf oluşturmak için kullanıyoruz. bu nedenle
# genellikle altsınıflara ek özellikleri, işlevselliği kazandıran fonksiyonlar tanımlıyoruz:
class Çalışan():
    def çalış(self):
        print("Çalışıyorum.")
# müdürler de bir çalışandır fakat çalışanlar gibi devamlı çalışmaz, arada bir de boş yaparlar:
class Müdür(Çalışan):
    def boş_yap(self):
        print("Bak bak izle az şunu çok komik.")
# super-subclass ilişkisi iki yönlü olmak zorunda değildir. yöneticiler müdürlerin sahip olduğu özelliklerin yanı sıra işten insanları kovabilirler
class Yönetici(Müdür):
    def elemanı_kov(self):
        print("Kovuldun canım muhasebeye söyle de çıkışını versinler.")

ç = Çalışan()
m = Müdür()
y = Yönetici()

ç.çalış()
m.çalış()
y.çalış()
# her üç sınıfımız da çalış metoduna sahiptir çünkü ç, Çalışan sınıfından diğerleri de onun alt sınıflarından objelerdir.
# fakat dıştan içe miras alma söz konusu değildir. yani:
# ç.boş_yap() # AttributeError verir.
m.boş_yap()
y.boş_yap()
# aynı şekilde:
# m.elemanı_kov() # bu satır da AttributeError verir.
y.elemanı_kov()
