# Inheritance (miras), bir sınıfın bir veya daha fazla sınıftan öznitelikleri ve yöntemleri miras aldığı bir model tasarımıdır ve ilişkili sınıfları organize etmemize,
# tekrarlamaları azaltmamıza yardımcı olur. inheritance tasarımında bazı teknik terimler söz konusudur. kendisinden miras alınan sınıf parent (ebeveyn), superclass (üst
# sınıf) veya baseclass (temel sınıf) olarak adlandırılırken miras alan sınıf child (çocuk), subclass (alt sınıf) veya derived class (türev sınıf) olarak adlandırılır.
# nelerin miras edildiğine gelecek olursak; public ve korumalı ("_" ile başlayan nitelikler korumalı nitekilerdir.) tüm nitelikler ve dunder metodlar subclass tarafından
# miras alınırken; özel nitelikler (name-mangled nitelikler denir ve "__" ile başlarlar. dunder metodlar bu tarz niteliklerden değildir karışmasın! bunlar nokta syntaxı
# ile çağrılamayan yalnızca objenin örneklemi içinde başka metodlarla değiştirilip çağrılabilen nitelikler) subclasslar tarafından miras alınmaz.
#
# subclasslar ve superclasslar arasında "type-of" (türüdür) ilişkisi vardır. mesela KahveDükkanı, Dükkan'ın bir türüdür veya ElektroGitar, Gitar'ın bir türüdür. yani
# inheritance tasarımının en büyük avantajı, aynı nitelikleri, metodları tekrar tanımlamadan bir superclassın bütün nitelik ve metodlarına sahip olan ama aynı zamanda
# kendine has nitelik ve metodları olan sınıflar oluşturabilmemizdir. superclass daha generalize, daha kapsayıcı özellikteyken subclass daha spesifiktir.
#
# şimdi ilk subclassımızı tanımlayalım. önce bi superclass tanımlamak lazım tabii:
class Dukkan():
    def __init__(self):
        self.eleman = "Egemen Şahin"
    def karşılama(self):
        print("Merhaba efendim ne arzu etmiştiniz?")

# subclassımızı tanımlayalım:
class KahveDukkanı(Dukkan): # subclass tanımlanırken yine class keywordünü kullanıyoruz fakat bu defa sınıfın adının yanındaki parantezin içine superclassı yazıyoruz.
    pass
# gördüğümüz gibi subclassımızda __init__ ve karşılama metodları yok. 
yeni_yıldız = KahveDukkanı()
# eğer init metodu çalıştıysa yeni_yıldız örnekleminin eleman niteliğine sahip olması gerek:
print(yeni_yıldız.eleman) # gördüğümüz gibi subclass'ta __init__ metodu olmadığından bu metodu superclasstan miras alıyor ve örneklenmesiyle beraber aynı __init__ metodu
# çalışıyor. altsınıfımız hem üst sınıfın niteliği olan eleman niteliğine hem de __init__ metodunu miras almış. bir de karşılama metoduna bakalım:
yeni_yıldız.karşılama()
