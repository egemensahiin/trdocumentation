# değişken, bir objeye verilen "isim", "etiket" olarak tanımlanabilir. değişken = obje
# şeklinde deklare edilir. değişken atanırken kullanılan "=" operatörüne "atama opera-
# törü" denir.
# = operatörünün sağ tarafı her zaman önce okunur. bu sayede 90-91. satırlardaki işlem-
# leri yapmamız mümkündür.
isim = "Egemen" # isim değişkeni "Egemen" stringini tanımlamaktadır.
yas = 24 # yas degiskeni ise int tipindeki 24 objesini tanımlar.
ogrencilik = True # ogrencilik degiskeni True yani boolean objesini tanımlar.
print(isim) # burada isim bir obje değil bir değişkendir. print fonksiyonu çıktısı
# "isim" değil isim değişkeninin refere ettiği "Egemen" stringi olur.
print(yas)
print(ogrencilik)

print("benim adim", isim, "ben", yas, "yasimdayim") # degiskenler print fonksiyonu
# altında bu şekilde kullanılabilir mesela.

# eğer bir değişken tanımlanmadıysa program içersinde kullanılması NameError oluşturur
#print(tanimlanmamis) # tanimlanmamis değişkeni print fonksiyonu altında kullanılmadan
# önce tanımlanmadığı için başında # kaldırıldığında program NameError verir.

# degiskenler herhangi tipte bir objeyi tanımlayabilir. eğer değişken, matematiksel bir
# işlemi veya bir karşılaştırmayı tanımladığında int, float veya boolean tipinde bir
# değeri yani operasyon sonucunu karşılar.
ders_notu = 80 + 15 # bir zorunluluk olmamakla beraber genellikle python programlarda
# iki kelimeden oluşan değişken isimler bitişik yazılmak yerine kolaylık olması için
# "_" ile ayrılır.
print(ders_notu)
dogru = 6 > 3
print(dogru)
yanlis = 7 == 8
print(yanlis)
bolme = 9 / 2
print(bolme)

# degiskenler program içinde değişebilir. bu noktada bilgisayar programlarının aksi
# şekilde programlanmadığı takdirde (döngüler yardımıyla) her zaman aşağı doğru yani
# bir sonraki satıra ilerlediği unutulmamalıdır.
var = 25
print(var)
var = 27
print(var)

# C, C++, Java gibi statik yazılan dillerin aksine python, dinamik yazılan bir dildir.
# statik yazılan dillerde kullanılan değişkenlerin tipi (class'ı), değişken tanımlan-
# madan önce tanımlanır ve başka tipta bir objenin bu değişkene atanması hata ile so-
# nuçlanır. pythonda ise programın farklı noktalarında aynı değişkene farklı tipte ob-
# jeler atamak mümkündür fakat pratik olmadığı için çok faydalanılan bir yöntem değil-
# dir.
dinamik = 15 # burada dinamik değişkenine int tipinde bir obje atadık
print(dinamik)
dinamik = 9.99 # burada ise aynı değişkene float tipinde bir değişken atadın
print(dinamik)
dinamik = "Na" + "ber" # dinamik değişkenine str tipinde değişken atadık
print(dinamik)
dinamik = 6 < 3 # burada ise bool tipinde bir değişken atadık
print(dinamik)

# değişken isimleri büyük küçük harf duyarlıdır. Buyuk ve buyuk birbirinden farklı de-
# ğişkenlerdir.
buyuk = "kucuk harfli"
Buyuk = "buyuk harfli"
print(buyuk)
print(Buyuk)

# birden fazla değişkenin aynı anda tanımlanması da mümkündür. eğer iki değişken aynı
# objeyi tanımlarsa örneğin a = b = 5 şeklinde iki değişken aynı anda tanımlanabilir.
a = b = 5
print(a)
print(b)
# unutulmaması gereken, 64. satırda a değişkeni ve b değişkeni arasında bir bağlantı
# kurmamış olduğumuz. burada yaptığımız a değişkenini ve b değişkenini aynı objeye
# karşılık gelmek üzere tanımlamak. yani b değişkeninin değerini değiştirdiğimizde a
# değişkeni buna bağlı olarak değişmez
b = 6
print(a)
print(b)

# birden fazla değişkeni aynı anda tanımlamamız için aynı objeye yönlendirmemiz gerek-
# mez. virgülle ayırarak farklı değişkenleri farklı objelere aynı satırda tanımlayabi-
# liriz
a, b, c, d = 2, 5.0, "string", True # üstelik bu değişkenler aynı tipte olmak zorunda
print(a) # da değildir, aynı anda farklı değişkenlere farklı tipte objeler tanımlana-
print(b) # bilir.
print(c)
print(d)

# değişkenlerle ilgili bir başka konsept de artırılmış atama değeri ve artırılmış atama
# operatörleridir. bir değişkene atanan objenin artırılması (stringler için birleşti-
# rilmesi) ve aynı değişkene atanmasına artırılmış atama denir. aynı şeyi diğer ma-
# tematiksel operasyonlarla da gerçekleştirmek mümkündür.
a = 1
a = a + 2
print(a)
# artırılmış atama operatörleri ise bu işlemi kısaltmak için kullanılan operatörlerdir
# toplama işlemi için artırılmış atama operatörü "+="dir. diğer işlemler için de aynı
# mantıkla "*=", "-=" ve "/=" operatörleri kullanılır.
a = 1
a += 2
print(a)
#artırılmış atama (+= ve *= operatörleri ile) stringlerle de kullanılabilir.
b = "bilgi"
b = b + "sayar"
print(b)
# yerine
b = "bilgi"
b += "sayar"
print(b)

c = 2
c = c * 5
print(c)
# yerine
c = 2
c *= 5
print(c)

d = "lo"
d = d * 5
print(d)
# yerine
d = "lo"
d *= 5
print(d)

e = 10
e = e - 5
print(e)
#yerine
e = 10
e -= 5
print(e)

f = 8
f = f / 2
print(f)
#yerine
f = 8
f /= 2
print(f)