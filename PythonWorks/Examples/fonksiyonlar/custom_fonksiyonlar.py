# pythonda tekrar tekrar kullanılacak kodları, custom fonk-
# siyonlar olarak tanımlamak mümkündür. tıpkı built-in
# fonksiyonlar gibi bunlar da çağrıldığında belli bir iş-
# levi yerine getirirler fakat farklı olarak bu işlem
# programcı tarafından belirlenir.
# bir fonksiyonu tanımlamak için "def" tanımlayıcısı kul-
# lanılır; def fonksiyon_adı(): şeklinde fonksiyon tanı-
# mlanır. parantez içersine fonksiyonu etkileyen paramet-
# reler yazılmaktadır. fonksiyona hiçbir parametre atan-
# masa dahi mutlaka () konulmalıdır. ":"dan sonra bir "TAB"
# veya buna denk gelen "4 SPACE" boşlukla yazılan satırlar
# fonksiyonu tanımlayan satırlardır. fonksiyonu tekrar ça-
# ğırdığımızda tanımladığımız bu kod satırlarını çağırmış
# oluruz
def ornek_fonksiyon():
    print("Bu çalışan bir fonksiyondur.")
    print("Bu da fonksiyonun ikinci satırı")
    print("Ve hatta bu da üçüncü satırı.")
# şimdi aynı built-in fonksiyonlarını çağırdığımız gibi bu
# fonksiyonu çağıralım
ornek_fonksiyon()
# bu fonksiyonu tekrar çağırdığımızda bir daha 3 satır kod
# yazmak yerine aynı kodu tekrar çalıştırabiliriz.
ornek_fonksiyon()

# tıpkı içi boş çift tırnak ("") bir string belirttiği gibi
# içi boş bir fonksiyon da yazılabilir. böyle bir fonksiyo-
# nu tanımlayan bir şey olmayacağı için boş bırakılması ge-
# rekir fakat bu durumda program SyntaxError verir. Bu se-
# beple "pass" ibaresiyle fonksiyon sonlandırılır. pass,
# fonksiyonları sonlandırmak için kullanılabilen genel bir
# ibaredir fakat boş olmayan fonksiyonlarda kullanılmama-
# sı sorun teşkil etmez.
def bos_fonksiyon():
    pass

# custon fonksiyonlara parametre atadığımızda ise fonksi-
# yonun tanımlanması def fonk_adi(parametre): şeklinde olur
# ve tıpkı built-in fonksiyonlarda olduğu gibi fonksiyo-
# na bu parametreyi verdiğimizde kendi tanımladığımız şe-
# kilde işler.
# örnek olarak "print" fonksiyonunu "p" şeklinde kısal-
# talım:
def p(yazi):
    print(yazi)
p("print foknsiyonu")
# örnekte olduğu gibi "p" fonksiyonuna tanımladığımız "yazi"
# parametresini p fonksiyonunun akışı altında print fonksi-
# yonu içersine tanımladık. sonuçta p fonksiyonu altında
# yazdığımız objeler print edilecektir.

# birden fazla parmetre tanımlamak da mümkündür.
def toplama(a, b):
    print(a, "ve", b, "sayılarının toplamı", a + b, "'dir.")
toplama(5, 7)
toplama(-8, 3)
toplama(4.3, 7.2)
# belirlediğimiz fonksiyonlarda objelerin tipi ile ilgili
# bir zorunluluk yoktu. mesela toplama() fonksiyonu altında
# iki sayı değil de iki string kullanıldığında toplama ye-
# rine birleştirme işlemi yapılır.
toplama("bilgi", "sayar")

# fonksiyonlara parametre tanımlarken 2 tip argüman kull
# anılabilir. bunlardan ilki yukarda da kullandığımız po-
# zisyonel argümanlardır. pozisyonel argümanlarda para-
# metrelerin tanımlandığı sıra önemlidir, parametreler
# (a, b) şeklinde tanımlandıysa, ilk yazılan parametre
# a'ya diğeri ise b'ye karşılık gelir. örnek olarak
def cikarma(a, b):
    print(a, "sayısının", b, "sayısından farkı", a - b, "olur.")

cikarma(7, 5) # pozisyonel argümana örnektir.
# eğer parametreler, tanımlandıkları "keyword"lerle tanım-
# lanırsa bunlara da keyword argümanlar denir. burada sıra
# sıra değil hangi parametrenin hangi keywordü tanımla-
# dığıdır.
cikarma(5, 10)
cikarma(b = 5, a = 10)

# ikiden fazla parametre olduğunda önce pozisyonel argüman-
# lar daha sonra keyword argümanlar kullanılarak da tanım-
# lama yapılabilir. her zaman pozisyonel argümanlar önce
# yazılmalıdır. önce keyword argümanlar yazılıp sonra kalan
# parametreleri tanımlamak için pozisyonel argümanlar kul-
# lanılırsa program SyntaxError verir.
def arguman(a, b, c):
    print("Üç sayının toplamı", a + b + c)
arguman(5, c = 10, b = 2)
#arguman(c = 10, b = 2, 5) #SyntaxError

# bir fonksiyonun sonucunu bir değişkene tanımlayıp bu de-
# ğişkeni print komutuyla yazdığımızda fonksiyon sonucu el-
# de etmeyi beklediğimiz sonucu görmeyiz. örneğin aşağıdaki
# fonksiyonu sonuc değişkenine tanımladığımızda 5 ve 3 pa-
# rametreleriyle 8 sonucunu almayı bekleriz ve yazdırdı-
# ğımızda da bu sonucu görmeyi bekleriz. fakat program ça-
# lıştığında gördüğümüz "None" yazısıdır. None, pythonda
# "hiçliği", "yokluğu" tanımlayan özel bir objedir, bir
# hata değildir.
def none_ornek(a, b):
    c = a + b
sonuc = none_ornek(5, 3)
print(sonuc)
# None bir obje sınıfıdır ve içerdiği tek obje None'dır.
print(type(sonuc))
# bir fonksiyonda elde edilen objeyi, fonksyionun dışına
# çıkartmak için fonksiyon gövdesine return ifadesi ek-
# lenir.
def return_ornek(a, b):
    return a + b
# bu durumda toplama4 fonksiyonundan çıktı olarak a ve b
# sayılarının toplamını almak mümkündür.
sonuc = return_ornek(5, 3)
print(sonuc)
# veya
print(return_ornek(5, 3))
# unutulmaması gereken, return ibaresinin fonksiyonu bi-
# tirdiğidir. bundan sonra fonksiyona eklenecek bir ele-
# man program tarafından kabul edilmeyecektir.
def return_ornek2(a, b):
    return a + b
    print("Bu string çıktıda gözükmeyecek.")
print(return_ornek2(3, 1))

# built-in fonksiyonlarda olduğu gibi custom fonksiyonlarda
# da parametrelere default argümanlar girmek mümkündür. bu-
# nun için parametreler tanımlanırken default olarak atana-
# cak değere eşitlenir. söz konusu değer için fonksiyon i-
# çersinde bir obje belirtilmezse default olarak tanımlanan
# obje ile fonksiyon çalışır
def default_ornek(a = 0, b = 0):
    return a + b
print(default_ornek(5, 2)) # a ve b parametreleri için obje-
# ler verildiğinde fonksiyon objeleri toplamaktadır. normal-
# de bu tür bir programa eksik bir obje tanımlandığında Ty-
# peError vererek bir argümanın eksik olduğunu söyler. fa-
# kat default bir değer atandığında, girilmeyen bir obje
# default kabul edilir ve sonuçta Error açığa çıkmaz.
print(default_ornek(b = 2))
print(default_ornek())

# fonksiyonlar yazılırken ve parametreler belirlenirken bu-
# nlara bir ":" kullanarak notlar yazmak mümkündür. python
# daha önce de söylediğimiz gibi dinamik bir dildir. bu se-
# beple eklediğimiz notlar dinamizmi etkilemez yalnızca ge-
# riye dönük okumalarda, fonksiyona atfedilen parametrele-
# rin ne olması "istendiğiyle" (gerektiğiyle değil) ilgili
# bilgi verir. annotationlar yani notlar, fonksiyonun so-
# nucu ile ilgili ise def fonksiyon(a, b) -> type: şeklinde
# verilir.
def annot_orn(a: str, b: int) -> str:
    return a * b
print(annot_orn("lo", 10)) # str olarak not etsek de a ye-
print(annot_orn(5, 6)) # rine int bir obje de koysak hata
# almayız çünkü bu notlar yalnızca bilgilendirme, hatırlat-
# ma amacı taşır.