# örnek nitelikleri ve sınıf nitelikleri arasındaki ilişki, örnek metodları ve sınıf metodları arasındaki ilişkiyle aynıdır. bir sınıf nitleiği oluştur-
# mak için, nokta syntaxı kullanılmaz. nokta syntaxı, örnek nitelikleri oluşturmak için kullanılır. sınıf nitelikleri basitçe sınıfın gövdesinde ta-
# nımlanan değişkenlerdir. sınıf nitelikleri, bir örneğe ait olmayan verilerin depolanmak için kullanılır. eğer depolamak istediğimiz veri bir obje-
# nin durumuna bağlı değilse (burada objelerin, sınıfların örneklemleri olduğunu hatırlamakta fayda var), daha üst seviyede bir şeyse yani daha glo-
# balse sınıf niteliği olarak depolanır.
# mesela bir sınıfın kaç defa örneklendiğini takip etmek istiyorsak, bu bilgi, sınıfın örneklemlerinin, objelerin sahip olacağı bir bilgi değildir, da-
# ha üst düzeyde bir bilgidir ve bu bilgiye obje yani sınıfın örneklemi değil, sınıfın kendisi sahip olabilir. başka bir senaryo da sınıfın tüm örnek-
# lerinin sahip olmasını istediğimiz bir veriyi depolamak istediğimiz durumlardır. bu durumda da tüm örneklerde verinin örnek niteliği olarak oluştu-
# rulması yerine sınıf gövdesinde sınıf niteliği olarak tanımlanabilir.
class Sayaç():
    sayı = 0
    def __init__(self):
        # eğer bu bir sınıf metodu olsaydı, sınıfın kendisini içsel olarak refere edebilirdik fakat bu bir sınıf metodu değil, örnek metodu ve bu se-
        # beple sınıfın kendisini dışsal olarak yani sınıfın kendi adıyla refere edeceğiz:
        Sayaç.sayı += 1 # örnek niteliklerine erişirken örneklem ile nokta syntaxı kullanıyorduk. sınıf niteliklerine erişirken ise sınıf metodlarında
        # olduğu gibi sınıfın kendi ismiyle nokta syntaxı kullanılarak çağrılır.
    # sınıf metodlarında durum biraz daha farklıdır. burada içsel olarak sınıf niteliklerine erişmek mümkündür:
    @classmethod
    def iki_örneklem(cls): # bunu da cls ile yapıyoruz.
        iki_sayaç = [cls(), cls()]
        print(f"Toplam örnek sayısı şu an {cls.sayı}")
        return iki_sayaç
# şimdi sayı niteliğine bakalım:
print(Sayaç.sayı)
# sınıfımızı örnekleyip sayı niteliğine tekrar bakalım:
örnek1 = Sayaç()
print(Sayaç.sayı)

print()

# şimdi de sınıf metodumuzu deneyelim:
örnek2, örnek3 = Sayaç.iki_örneklem() # iterable'lar içersindeki değerlerin virgül syntaxı ile birden fazla değişkene atanabildiğini unutma
print(Sayaç.sayı)

print()

# sınıf niteliklerinin bir ilginç özelliği de bunlara tüm örneklemlerden erişilebiliyor olmasıdır. burada yanlış anlaşılmaması gereken bir nokta mev-
# cuttur: sınırın her örneklemi, sınıf niteliğini içermez, sınıf niteliği bir tanedir ve hafızada sadece bir tane mevcuttur fakat sınıfın her örnekle-
# mi bu niteliğe erişebilmektedir ve doğal olarak bu örneklem oluştuğunda bu nitelik hangi durumda olursa olsun, örneklem yoluyla sınıf niteliğine u-
# laşıldığında o anki durumuna ulaşılır.
print(örnek1.sayı)
print(örnek2.sayı)
print(örnek3.sayı)

print()

# sınıf nitelikleri ve örnek nitelikleri arasında bir düzen mevcuttur. pythonda bir örnek üzerinde bir nitelik çağrıldığında, önce örnek niteliklerine
# bakılır. eğer örnek nitelikleri arasında, refere edilen nitelik bulunamazsa bu sefer sınıf nitelikleri arasında söz konusu nitelik aranır.
class Örnek():
    data = "Sınıf niteliği."
örn1 = Örnek()
örn2 = Örnek()
# örneklemlerimizdeki data nitliklerine bakalım:
print(örn1.data)
print(örn2.data)
# şimdi örn1 için aynı isimli bir örneklem niteliği oluşturalım:
örn1.data = "Örnek niteliği."
print(örn1.data) # örneklemler üzerinden sınıf niteliğinin değiştirelemeyeceği bariz fakat burada sınıf niteliğini değiştirmeyip bir örneklem niteliği
# oluşturduğumuzu ispatlamak için örn2 örneklemi veya Örnek sınıfında data niteliğini çağırarak görebiliriz:
print(örn2.data)
print(Örnek.data)
# del keywordüyle örneklem niteliğini silebiliriz:
del örn1.data
print(örn1.data)