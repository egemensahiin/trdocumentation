# "type" fonksiyonu, input olarak verilen objenin, ne türden bir obje olduğunu çıktı
# olarak vermektedir. burada gösterilen örneklerin görülebilir olması açısından type
# fonksiyonu, print fonksiyonu içersine yazılarak gösterilecektir fakat esasında type
# kendi başına bir fonksiyondur.
type(5) # bu fonksiyonun çıktısı <class 'int'> dir. yani input olarak verilen obje (5)
# int yani integer (tamsayı) sınıfına ait bir objedir.

print(type(5)) # <class 'int'> #
print(type(5.3)) # <class 'float'> # float, floating pointin kısaltması olup ondalıklı
# sayılardan oluşan objeler sınıfının adıdır.
print(type(5.0)) # <class 'float'> # matematiksel olarak 5.0 tamsayı olmasına karşın
# burada da görülebileceği üzere ondalıklı yazıldığı için float sınıfına aittir.

print(type("python")) # <class 'str'> # str, stringin kısaltmasıdır.

print(type(True)) # <class 'bool'> # bool, boolean sınıfının kısaltmasıdır.
print(type(False)) # <class 'bool'> # type fonksiyonu içine, boolean objesi veren bir
# operasyon yazdığımızda da sonuç 'bool' olarak çıkar.
print(type(3 < 4)) # <class 'bool'> #

print(type([1, 2, 3])) # <class 'list'> # list, parantez içinde sıralanmış sayıların
# oluşturduğu objelerdir.

print(type({"ab": "cd"})) # <class 'dict'> # dict ise ":" ile ayrılmış parantez içindeki
# iki stringden oluşan bir objedir.

# type fonksiyonunun çıktısını da "==" ve "!=" operatörleriyle kıyaslamak ve boolean
# tipinde objeler elde etmek mümkündür.
print(type(5) == type(10)) #True#
print(type(5) == type(5.0)) #False#
print(type("arch") == type(5)) #False#
print(type(True) == type(False)) #True#