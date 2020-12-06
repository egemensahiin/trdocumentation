# inheritance tasarımında hiyerarşi, kapsamlar hiyerarşisinde olduğu gibi içten dışa doğrudur. python ilk önce istenen nitelik veya metodu subclass'ta arar.
# eğer aynı isimli nitelik subclassta varsa bu çalışır, yoksa superclassta arar.
class Dukkan():
    def __init__(self):
        self.eleman = "Kuzey Tekinoğlu"
    def mekan_sahibi(self):
        print("Sami Tekinoğlu")
    def karşılama(self):
        print("Merhaba efendim ne arzu etmiştiniz?")

class Fırın(Dukkan):
    def karşılama(self):
        print("Hayırdır birader! Simit var poğaça var ne bakıyon!")

# gördüğümüz gibi subclassımızda __init__ ve mekan_sahibi metodları yok. ama karşılama metodu var. şimdi sınıfımızı örnekleyip bu iki metodun davranışlarını
# inceleyelim:
tekinoğlu = Fırın()
# eğer init metodu çalıştıysa tekinoğlu örnekleminin eleman niteliğine sahip olması gerek:
print(tekinoğlu.eleman) # gördüğümüz gibi subclass'ta __init__ metodu olmadığından bu metodu superclasstan miras alıyor ve örneklenmesiyle beraber aynı 
# __init__ metodu çalışıyor. altsınıfımız hem üst sınıfın niteliği olan eleman niteliğine hem de __init__ metodunu miras almış. bir de mekan_sahibi metoduna
# bakalım:
tekinoğlu.mekan_sahibi()
# ama karşılama metodu subclassta da olduğu ve subclassın nitelikleri hiyerarşik olarak öncelikli olduğu için karşılama metodyla aynı çıktıyı almıyoruz:
tekinoğlu.karşılama()
