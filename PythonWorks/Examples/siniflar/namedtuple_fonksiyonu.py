# namedtuple, collections kütüphanesinde yer alan bir fonksiyon olup, yalnızca niteliklerden oluşan, metodu olmayan sınıflar oluşturmak için kullanılır.
# teknik olarak oluşturulan objeler sınıf değil, tuple sınıfı içersinde bir altsınıftır (subclass) ve hem tuple'lar gibi indekslenebilir, sıralı bir
# objedirler hem de kendi oluşturduğumuz sınıflar gibi kendi nitekileri ve bu niteliklere ait durumları içerirler. metodlara ihtiyaç duymadığımız, eli-
# mizdeki verileri veritabanlarında olduğu gibi belirli niteliklerin durumları şeklinde depolamamız gereken durumlarda namedtuple'lar faydalıdır çünkü
# 3, 4, 5 bazen daha da fazla satırda yapacağımız nitelik tanımlama işini tek bir satırda yapmamızı sağlar.
import collections
Molekül = collections.namedtuple("MolekülSınıfı", ["isim", "molekül_ağırlığı"])
# niteliklerin isimleri, string listesi şeklinde olabildiği gibi boşlukla ayrılmış isimlerden oluşan bir string şeklinde de tanımlanabilir.
# namedtupple tanımlanmasında, namedtuple'ı atadığımız değişken sınıf gibi davranır, ama objeyi type fonksiyonundan geçirdiğimizde namedtuple'ın ilk argüma-
# nının sınıf olduğunu görürüz..
fami = Molekül("Famipravir", 300)
print(type(fami))
print(type(Molekül))

# namedtuple'lar, tuple'lara ait bir altsınıf oluşturur. yani hala tuple'lar gibi sıralı ve indekslenebilir objelerdir:
print(fami[0])
print(fami[1])
# ama aynı zamanda da kendisi biri sınıftır yani nokta syntaxı da kullanılabilir.
print(fami.isim)
print(fami.molekül_ağırlığı)