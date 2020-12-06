# __eq__ metodu, aynı sınıftan iki objenin eşitliği için aranan koşulu tanımlamada kullanılır. ilk argüman olarak aldığı mevcut objeyle ikinci argüman
# olarak aldığı obje arasında tanımlanan bir ilişkiye bağlı boolean değerini return eder.
class Öğrenci():
    def __init__(self, matematik, tarih, edebiyat):
        self.matematik = matematik
        self.tarih     = tarih
        self.edebiyat  = edebiyat
    # Öğrenciyi tanımlarken notlarını verelim ama sınıf içersinde not ortalamasını kullanalım ve eşitliğini buna göre değerlendirelim. hem property kon-
    # septine de bir pratik olur:
    @property
    def ortalama(self): # hatırlanacağı üzere modülün adı, sınıfı çağırırken kullanacağımız niteliğin de adı esasında. bu property'mizde sadece setter
        # kullanıyoruz. aslında bunun yerine doğrudan __init__ altında da ortalamayı tanımlayabilirdik fakat bunun bir sınıf niteliği gibi çağrılması
        # problem yaratırdır o yüzden property yaklaşımı daha temiz, daha anlaşılır.
        return (self.matematik + self.tarih + self.edebiyat) / 3
    def __eq__(self, diğeri): # diğer objenin adıyla ilgili bir standart yok. zaten neyin ifade edildiği gayet açık. normalde bu objelerin kıyaslanma-
        # sı yanılmıyorsam hafızadaki konumlarına göre oluyor. fakat __eq__ metoduyla biz, hafızadaki yerinden bağımsız olarak bizim istediğimiz koşul-
        # da da objelerin eşit (aynı değil, aynılık sadece hafızada aynı yeri işgal eden birimler arasında söz konusu) olmasını sağlıyoruz.
        return self.ortalama == diğeri.ortalama # bu şekilde iki öğrencinin eşit olmasının koşulunu, öğrenci objelerinin "ortalama" niteliklerinin eş-
        # it olması koşuluna bağladık.

egemen = Öğrenci(
    matematik = 90,
        tarih = 80,
     edebiyat = 70
)

sefa = Öğrenci(
    matematik = 80,
        tarih = 80,
     edebiyat = 80
)

erzan = Öğrenci(
    matematik = 20,
        tarih = 30,
     edebiyat = 25
)

# görülebileceği gibi egemen ve sefa için ortalama niteliği aynı değere sahip:
print(egemen.ortalama)
print(sefa.ortalama)
# bu durumda __eq__ tanımımıza göre bu iki obje eşittir:
print(egemen == sefa)
# bir de eşit olmayan duruma bakalım:
print(egemen == erzan)
# eşitliğin tanımlanması demek, eşitsizliğin de tanımlanması demektir:
print(sefa != egemen)
print(erzan != sefa)
# esasında burada arka planda gerçekleşen şey, objemiz üzerinde __eq__ metodunun çalışmasıdır:
print(egemen.__eq__(sefa))
print(sefa.__eq__(erzan))