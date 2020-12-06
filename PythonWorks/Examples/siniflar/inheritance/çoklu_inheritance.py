# her ne kadar tartışmalı bir pratik olsa da pythonda bir sınıf, birden fazla sınıfın alt sınıfı olabilir. yani birden fazla
# sınıfın niteliklerini miras alabilir. bir sınıfın, diğer iki sınıfa da ait özellikleri gösterdiği fakat kendine ait özel-
# likleri de barındırdığı durumlarda bazı programcılar tarafından tercih edilen bir pratik olmasına karşın, yol açabileceği
# karışıklıklardan dolayı bazı programcılar kullanımını doğru bulmamaktadır.
class DondurulmuşGıda():
    def kafa_dondurma(self, zaman):
        print(f"{zaman} dakika kafayı donduruyor.")
    def saklama(self):
        print("Buzlukta saklayın.")

class Tatlı():
    def kalori_miktarı(self, kalori):
        print(f"Tebrikler, {kalori} yeni kalori kalori kazandın.")
    # burada diğer sınıfta da var olan bir metodu, farklı bir işlevsellikle tanımlayalım.
    def saklama(self):
        print("Buzdolabında saklayın.")

# bir alt sınıf için birden fazla parent tanımlarken basitçe bunları parantez içinde, virgülle ayırarak yazıyoruz:
class Dondurma(DondurulmuşGıda, Tatlı):
    pass

d = Dondurma()
# şimdi subclassımız üzerinde metodları çalıştıralım.
d.kafa_dondurma(5)
d.kalori_miktarı(120)
# beklendiği üzere kafa_dondurma ve kalori miktarı metodlarının ikisi de Dondurma altsınıfına miras kaldı.
# peki iş saklama metoduna gelince ne olacak:
d.saklama()
# çıktıda da gördüğümüz gibi saklama metodunu çalıştırdığımızda Tatlı superclassındaki değil DondurulmuşGıda superclassı-
# ndaki saklama metodu çalıştı. peki python buna neye göre karar veriyor? birden fazla ebeveyn sınıfı olan altsınıfların
# hiyerarşisinde normalde olduğu gibi ilk başta alt sınıfın kendisi var. eğer python söz konusu niteliği alt sınıfın ken-
# disinde bulamazsa, ebeveynleri yazıldığı sırayla arıyor. yani 19'uncu satırdaki yazılma sırasını değiştirdiğimizde fark-
# lı bir çıktı alıyoruz.
# bu tip bir hiyerarşiye pythonda metod çözünürlük düzeni (method resolution order/mro) deniyor ve bunu göstermek için
# pythonda "mro" adlı bir SINIF metodu mevcut:
print(Dondurma.mro())
print()
# bir de tam tersi sırayla bir sınıf tanımlayalım
class DondurmalıPasta(Tatlı, DondurulmuşGıda):
    pass
dp = DondurmalıPasta()
# şimdi bunun üzerinde saklmaa metodunu ve mro sınıf metodunu çalıştıralım:
dp.saklama()
print(DondurmalıPasta.mro())

print()

class Restoran():
    def rezervasyon(self, kişi_saysı):
        print(f"{kişi_saysı} misafir için masa ayrılmıştır.")

class SteakHouse(Restoran):
    pass

class Bar():
    def rezervasyon(self, kişi_saysı):
        print(f"{kişi_saysı} misafir için loca ayrılmıştır.")

class BarNGrill(SteakHouse, Bar):
    pass

# yukarıdaki sınıf-altsınıf ilişkisinde cevabını aradığımız soru, bir BarNGRill örneklemi üzerinde çalıştıracağımız rezer-
# vasyon metodundan ne sonuç alacağımız. bunu anlamak için önce programlama dillerinin tree-like (ağaç benzeri) yapılarda-
# ki arama davranışlarını anlamamız lazım.
#
# # # # # # # # # # # #     Ağaç benzeri veri yapılarında programlama dillerinin iki farklı arama algoritması gözlenir:
#                      #        1- Depth-First Arama: Bu tip bir arama davranışında program, önce en gidebildiği kadar de-
#    A                 #    rindeki verileri aramaya çalışır. Mesela yandaki ağaç benzeri yapıda en alt katmanda yani baş-
#    |                 #    langıçta A olsun ve program J'ye ulaşmaya çalışsın. Bunun için program önce A'ya bakar. Daha
#    |---> B           #    sonra B'ye bakar. Depth-first yaklaşımında program B'ye baktıktan sonra aynı seviyedeki diğer
#    |     |           #    veriler yerine daha derindeki verileri tarar. Sırayla E, F ve G'yi taradıktan sonra daha de-
#    |     |---> E     #    rinde veri bulamayan program bir üst derinliğe gider ve aramaya C'den devam eder. Yani prog-
#    |     |           #    ram J'ye gidene kadar A-B-E-F-G-C-H-I-D-J yolunu izler.
#    |     |---> F     #        2- Breadth-First Arama: Bu tip bir arama davranışında ise program A'yı ve ardından B'yi a-
#    |     |           #    radıktan sonra derine inmez, B ile aynı seviyedeki bilgiyi arar. C'ye ve D'ye baktıktan sonra
#    |     |---> G     #    B'nin derinine iner ve aynı seviyede aramayı sürdürür. Sonuç olarak program A'dan J'ye ulaşa-
#    |                 #    na kadar A-B-C-D-E-F-G-H-I-J yolunu takip eder.
#    |---> C           #    
#    |     |           #        Python, Depth-First bir programlama dilidir. Bu durumda yukarıdaki sınıfları ağaç benzeri
#    |     |---> H     #    bir hiyerarşiye yerleştirirsek:
#    |     |           #    
#    |     |---> I     #    
#    |                 #       BarNGrill                            görüldüğü gibi Depth-First yaklaşımıyla ilk ulaşılan
#    |---> D           #       |                                    rezervasyon metodu, Restoran superclassındaki rezer-
#          |           #       |---> Steakhouse                     vasyon metodu olur. eğer ki python Breadth-First bir
#          |---> J     #       |       |                            dil olsaydı bu sefer ilk önce Bar superclassının re-
#                      #       |       |---> Restoran               zervasyon metodu okunacaktı ve alacağımız çıktı fark-
# # # # # # # # # # # #        |               |                    lı olacaktı.
#                              |               |---> rezervasyon    
#                              |                                    
#                              |---> Bar                            
#                                    |                              
#                                    |---> rezervasyon              
#                           
# şimdi bir de moduülümüzü çalıştırıp görelim:
şahin_kardeşler = BarNGrill()
şahin_kardeşler.rezervasyon(5)
# yine mro moduülünü, metodların çözünürlük sırasını görmek için kullanabiliriz. bu sıra yukarıda bahsettiğimiz prensibe
# göre hesaplanır.
print(BarNGrill.mro())

print()

# çoklu inheritance ile ilgili bilinmesi gereken bir başka konsept de Elmas-Şekilli inheritance. bu durum, bir subclassın
# miras aldığı iki superclassın, aynı sınıfın subclassları olması durumunda gözlenir ve istisnai bir durum söz konusudur.
# şematize edildiğinde elmas benzeri bir yapı ortaya çıktığı için bu isim verilmiştir.
class Filmci():
    def mülakat(self):
        print("Film yapmayı seviyorum.")

class Yönetmen(Filmci):
    pass

class Senarist(Filmci):
    def mülakat(self):
        print("Senaryo yazmayı seviyorum.")

class JokerEleman(Yönetmen, Senarist):
    pass

# yukarıda tanımladığımız sınıfların inheritance yapısını inceleyecek olursak, JokerEleman sınıfı, hem Yönetmen hem de
# Senarist sınıflarını miras alıyor. JokerElemanın her iki ebeveyn sınıfı da aynı sınıftan yani Filmci sınıfından mi-
# ras alıyor. bu durumu şematize edecek olursak:
#
#             /---> Yönetmen (1)                    Normal bir derinlik önceli algoritmanın bakacağı sıra yandaki gibi
#            /      \                               olacaktır. Önce Yönetmene, oradan daha derine gidip Filmciye ulaşır
#           /        \                              ve Filmci sınıfında tanımlanan mülakat metodunu çalıştırır fakat
#          /          \                             eğer ki bir sınıf, inheritance ağacında birden fazla kez refere e-
#   JokerEleman      Filmci (2) (4) ---> mülakat    dilmişse, python bu sınıfın önceki bütün referanslarını yok sayar.
#          \          /      |                      burada Filmci sınıfı önce Yönetmenden sonra yani 2. sırada, ardın-
#           \        /       |---> bu referans      dan da Senaristten sonra yani 4. sırada refere edilir. bu durumda
#            \      /               alınmaz         python 2. sıradaki yani Yönetmenden sonraki referansını yok sayar
#             \---> Senarist (3) ---> mülakat       ve mülakat metodunu Yönetmende aradıktan sonra Filmciye değil, Se-
#                                                   nariste bakar. haliyle beklediğimizden farklı bir çıktı verir. 
# bunu genişlik önceli algoritmayla karıştırmamak lazım. burada olan genişlik önceli bir arama değil, miras ağacında
# birden fazla kez refere edilen bir objenin önceki referanslarının kaldırılmasıdır.
# şimdi metodu çalıştırıp görelim. ardından da mro çıktısını alalım:
tarantino = JokerEleman()
tarantino.mülakat()
print(JokerEleman.mro())
