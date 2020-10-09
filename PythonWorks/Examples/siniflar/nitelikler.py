class Gitar():
    def __init__(self):
        print(f"Yeni bir Gitar yaratıldı. Bu obje {self}")

akustik = Gitar()
elektro = Gitar()

# -- BURADA ANLATILANLAR GENEL KULLANIMA UYGUN DEĞİL -- #
# pythonda diğer dillerin aksine sınıfların nitelikleri, sınıfın örneklendirilmesinden sonra obje oluşsa dahi nitelikler tanımlanabilir. bunun için nok-
# ta syntaxı kullanılır. esasında pythonda da bu kullanım, kodun organizasyonu açısından doğru bir kullanım değildir ve tercih edilmez fakat python di-
# ğer dillerden daha açıktır ve bu kullanımı programcının insiyatifine bırakmaktadır. mesela akustik gitarımız için bir kaç nitelik atayalım:
akustik.malzeme = "Ceviz"
# topluluk standartlarında nitelik isimlendirmesi, değişken isimlendirmesine benzer şekilde küçük harflerle ve kelimeleri "_" ile ayırarak yapılır.
akustik.tel_sayısı = 6
akustik.model_yılı = 1990
# bu nitelikleri de yine nokta syntaxıyla çağırabiliyoruz:
print(akustik.malzeme)
# bu kullanımın başlıca sıkıntısı, obje odaklı kod tasarımına aykırı bir mantıkta olmasıdır. obje odaklı programlamada objelerin taslakları olan sınıf-
# lar, obje her çağırıldığında farklı değerlere ve durumlara sahip olsa da aynı metodları ve nitelikleri içermelidir. mesela elektro objesine de bir
# nitelik atayalım:
elektro.nickname = "Distortion Monster V6"
# obje odaklı programlama standartlarında bir sınıf, tüm örneklendirmelerinde aynı nitelikleri ve metodları içerir. buna karşın nokta syntaxıyla atadı-
# ğımız nitelikler sınıfa değil objeye özgü olur. örneğin nickname niteliğini akustik objesinde göremeyiz, çağırmaya çalıştığımız takdirde de Attribute-
# Error alırız.
# print(akustik.nickname) # AttributeError
# print(elektro.malzeme) # AttributeError

print()

# -- KULLANILAN SYNTAX -- #
# obje odaklı programlama mantığına uygun olan syntax, niteliklerin __init__ metodu ile tanımlanmasıdır. hatırlanacağı üzere __init__ metodunun ilk ar-
# gümanı her zaman örneklendirilmiş objenin kendisine refere eden dinamik bir argümandır ve python bunu otomatik olarak atar. bu sebeple bundan sonra ge-
# len ilk argüman __init__ metodunun ilk pozisyonel argümanıdır. self argümanı da dinamik bir argüman olduğu için __init__ gövdesinde nokta syntaxı ile
# self'e, __init__ in pozisyonel argümanları atanır. bi de örnekle görelim:
class Asa():
    def __init__(self, malzeme):
        self.malzeme = malzeme # burada "=" in sağındaki malzeme, __init__ argümanı iken sol taraftaki malzeme, niteliğin ismidir.

mürver = Asa("Mürver")
snape = Asa("Kavak")
print(mürver.malzeme)
print(snape.malzeme)
# aynı nitelikleri atadığımız farklı objeler birbirleriyle aynı durumda olsa da farklı objelerdir:
lilly = Asa(malzeme = "Kavak")
print(snape)
print(lilly)

print()

# bu durumda sınıfı örneklendirirken bir argümanla beslemediğimize TypeError alırız. bunun önüne geçmek için tıpkı fonksiyonlarda olduğu gibi argümana bir
# default değer atanabilir:
class Masa():
    def __init__(self, malzeme = "Belirtilmedi"):
        self.malzeme = malzeme
    
ikea = Masa()
koçtaş = Masa(malzeme = "Ceviz")
print(ikea.malzeme)
print(koçtaş.malzeme)