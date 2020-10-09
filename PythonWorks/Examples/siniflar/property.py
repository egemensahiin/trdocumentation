# sınıflarda karşılaşılan bir diğer konsept de property'lerdir. propertyler, nitelik gibi görünür, nitelik gibi çağırılır fakat aslında arkaplanda yarı
# özel metodlar çalışrırlar. bir property tanımlamak için getter ve setter denilen iki örnek metodu tanımlanmalıdır ve bu metodlar çoğunlukla korunan
# (yarı özel) metodlardır. getter, adı üstünde niteliği getiren metoddur. setter ise yine adından da anlaşılabileceği gibi niteliği değiştiren, ayarla-
# yan metoddur.
# örneğin bir iş modeli için bir ücret sınıfı yazalım. sınıfımız, verileri lira cinsinden çekiyor, fakat içersinde çalıştırılan metodların mantığı gereği
# yalnızca dolar birimini kullanıyor olsun:
class Ücret():
    def __init__(self, lira):
        # objelerimiz liraya değil yalnızca dolara ihtiyaç duyacak. bu sebeple bir "lira" niteliği oluşturmayacağız. fakat söz konusu dolar niteliği de
        # public olmamalı çünkü bunun lira argümanına bağlı olmasını istiyoruz. bu sebeple korunan bir nitelik olarak atıyoruz:
        self._dolar = lira / KUR
    def dolar_kullanan_metodlar_falan(self):
        pass
    def _get_lira(self): # şimdi getter metodumuzu yazıyoruz. dediğimiz gibi bu sınıf içersinde gerçekleşen mantık, dolar üzerinden de olsa biz bu sınıfı
        # lira cinsinden yazıp okuyoruz. bu sebeple de bu sınıftan "lira"yı çağırabiliyor olmak istiyoruz:
        return self._dolar * KUR # metodumuz _dolar niteliğinden faydalanarak lirayı return ediyor
    def _set_lira(self, lira): # istediğimiz zaman lirayı çağırmanın yanında bir de lirayı public olarak (nokta syntaxıyla) ayarlamak istiyoruz. setter
        # metodumuz da bunu yapacak ve bunu yaparken bir de validasyon (değerlendirme) yapacak. bu da bize lira niteliğini modifiye ederken değerlendirme
        # yapma imkanı sunacak.
        if lira >= 0:
            self._dolar = lira / KUR
    # şimdi geldik property fonksiyonuna. bu fonksiyon, argüman olarak sırayla bir getter ve bir setter fonksiyon alır ve bunu bir değişkene atadığımız-
    # da bu değişken, sınıfa ait bir nitelik gibi davranır. gerçekte arka planda olan ise; bu property çağrıldığında getter metodunun çalışması, nokta
    # syntaxıyla değiştirildiğinde ise değiştirildiği değeri argüman kabul ederek setter metodunun çalışmasıdır.
    lira = property(_get_lira, _set_lira)

KUR = 7.95 # :'(((((((

# bi görelim:
asgari = Ücret(2300)
# __init__ metodunda bir tek nitelik tanımladık aslında. tüm sınıfta da sadece bu niteliği kullandık:
print(asgari._dolar)
# ama "lira" da sanki bir nitelikmiş gibi çağrılabilir.
print(asgari.lira) # burada slında asgari._get_lira() çalıştırır.
# hatta diğer nitelikler gibi nokta syntaxıyla ayarlana da bilir.
asgari.lira = 2350 # burada olansa aslında asgari._set_lira(2350) nın çağrılmasıdır.
print(asgari._dolar)
print(asgari.lira)
# setterda gerçekleştirdiğimiz değerlendirme sayesinde lira'ya negatif bir sayı atayamıyoruz:
asgari.lira = -300
print(asgari.lira)

print()

# sınıflarda property oluşturmak için daha yagın olarak kullanılan yaklaşım ise python built-in property dekoratörüdür.
class Enerji():
    def __init__(self, kalori):
        self._joule = kalori / 0.2388
    def joule_falan_filan(self):
        pass
    # bu sefer getter ve setter metodlarımızın isimleri, property ye vermek istediğimiz isim olacak ama getter metodunu property dekoratörüyle, setter
    # metodunu da isim.setter dekoratörüyle tanımlayacağız:
    @property
    def kalori(self):
        return self._joule * 0.2388
    @kalori.setter
    def kalori(self, kalori):
        if kalori >= 0:
            self._joule = kalori / 0.2388

reaksiyon = Enerji(500)
print(reaksiyon.kalori)
reaksiyon.kalori = 1000
print(reaksiyon.kalori)