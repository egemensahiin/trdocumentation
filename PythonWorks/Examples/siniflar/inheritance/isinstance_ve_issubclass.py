# isinstance fonksiyonu; ilk argümanın, ikinci argümanın örneklemi olup olmadığını kontrol eder. yani ilk argümanında
# bir obje, ikinci argümanında da bir sınıf bulunur. eğer verilen obje, verilen sınıfın bir örneklemi ise True, değil
# ise False çıktısı verir. ikinci argüman olarak beslememiz gereken, sınıfın konvansiyonel adı değil pythondaki adı-
# dır. bu da type fonksiyonuyla verdiği çıktıdır.
print(type(1))
print(isinstance(1, int))
print(isinstance({'a': 1}, dict))
print(isinstance(1.99, float))
print(isinstance("", str))
print(isinstance([], list))
# biraz da False versin
print(isinstance("a", int))
print(isinstance((1, 3), list))

print()

# mro metodunda da hatırlayabileceğimiz gibi pythonda sınıfların en üstündeki sınıf object sınıfır. yani pythonda ob-
# je olan her şey (yani daha basit söylemek gerekirse her şey) object sınıfının bir örneklemidir:
print(isinstance(1, object))
print(isinstance([], object))
# sınıfların kendileri de objet'in örneklemidir:
print(isinstance(str, object))
print(isinstance(list, object))
# fonksiyonlar da aynı şekilde
print(isinstance(isinstance, object))
# boolen, none gibi objeler de:
print(isinstance(True, object))
print(isinstance(None, object))

print()

# isinstance fonkyonu, ikinci argüman olarak sınıflardan oluşan bir tuple da alabilir. bu durumda ilk argüman, tuple
# içersindeki herhangi bir sınıfın örneklemi ise True verir, hiçbirinin örneklemi değilse False verir.
print(isinstance("Egemen", (int, str, list)))
print(isinstance(1.99, (int, str, dict)))

print()

# issubclass fonksiyonu ise iki argüman kabul eder ve ilk argüman, ikinci argümanın altsınıfı ise True, değil ise False
# verir. iki yönlü çalışmaz. yani ikinci argüman ilk argümanın altsınıfı olduğunda da False çıktısı verir.
class İnsan():
    pass
class SuperKahraman(İnsan):
    pass

print(issubclass(SuperKahraman, İnsan))
print(issubclass(İnsan, SuperKahraman))
# pythonda tüm sınıflar yine object sınıfının altsınıfıdır:
print(issubclass(İnsan, object))
print(issubclass(SuperKahraman, object))

print()

# kendi sınıflarımızda da isinstance ile kontrol yapmak mümkündür. bu durumda bir subclassın örneklemi aynı anda super-
# classın da örneklemi olacaktır:
egemen = İnsan()
batman = SuperKahraman()
print(isinstance(batman, İnsan))
print(isinstance(batman, SuperKahraman))
print(isinstance(egemen, İnsan))
print(isinstance(egemen, SuperKahraman))

