# bildiğimiz üzere fonksiyon içersinde tanımlanan değişkenler lokal değişkenlerdir ve global bir değişkeni fonksiyon içersinde değiştirdiğimizde global
# kapsamda değeri aynı kalır. aynı şekilde lokal olarak tanımlanan değişkenler global kapsamda tanımsızdır.
x = 1
def değişemeyiş():
    x = 2
print(x)
değişemeyiş()
print(x) # görüldüğü gibi fonksiyon çalıştırılmadan önce de sonra da x değişkeninin değeri 1'dir.

print()

# lokal kapsamdan global kapsamdaki bir değişkene erişmek veya global kapsamda bir değişken oluşturmak için fonksiyon içersinde global keywordü kulla-
# nılır:
def değişim():
    global x # bu şekilde şunu deklare ediyoruz: bu lokal kapsamda kullanılan "x" ismi, lokal kapsamda değil global kapsamdadır.
    x = 2
print(x) # => 1
değişim()
print(x) # => 2

print()

# eğer global keywordü ile verilen işim, mevcut değilse bu isim global kapsamda oluşturulur:
def oluşum():
    global y
    y = 3
# print(y) # bu satır çalıştırıldığında NameError alınır çünkü oluşum fonksiyonu henüz çelışmadığı için "y" değişkeni de tanımlanmamıştır. bu sebeple
# lokal kapsam içersinde global isimler oluşturmak esasında çok tercih edilen bir pratik değildir.
oluşum()
print(y) # => 3