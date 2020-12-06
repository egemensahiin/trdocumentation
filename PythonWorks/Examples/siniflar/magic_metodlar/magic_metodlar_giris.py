# magic metodlar, objelerimize pythondaki built-in objelere benzer özellikler kazandırmak için kullanılır. mesela bir objeyi iterable hale getirmek,
# len gibi built-in fonksiyonlarla kullanılabilir kılmak, indexlenebilirlik kazandırmak, aynı sınıftaki iki objenin eşit veya eşit olmama durumları
# gibi özellikler magic metodlarla kazandırılır.
# pythonda sınıflarımız için kullanabileceğimiz bir kaç magic metod mevcuttur. bu metodlar "__" ile başlar ve biter bu sebeple dunder (duble undersc-
# ore) metodlar olarak isimlendirilirler. yani esasında __init__ metodu da bir magic metoddur.
# dunder metodlar, sınıflarımız için birer hook (kanca) gibi davranır. hook; bir işlemi (process'i) yürütüldüğü sırada bir noktada kesen bir prosedür-
# dür. bunu, başka bir kod çalışırken kendini araya yerleştiren bir kod parçası olarak düşünebiliriz. magic metodlar da birer hook'tur; python tara-
# fından doğru anda arka planda dolaylı olarak çağrılırlar.
# normalde dunder metodların programcı tarafından doğrudan çağrılması pek yaygın değildir fakat bu programda neler döndüğünü görmek için bu prensibi
# uygulamayacağız.
# int ve float gibi çok temel objelerde de dunder metodlar mevcuttur. mesela "+" operasyonu kullanıldığında arkaplanda __add__ metodu çalışmaktadır:
print(3.14 + 2.72)
print(3.14.__add__(2.72))
# bir objeyi len fonksiyonundan geçirdiğimizde, arkaplanda obje üzerinde __len__ metodu çalışır:
print(len("Egemen"))
print("Egemen".__len__())
# başka bir örnek de "in" operatörüdür:
print("e" in "Egemen")
print("Egemen".__contains__("e"))
# indeks de esasında bir dunder metoddur:
print(["a", "b", "c"][2])
print(["a", "b", "c"].__getitem__(2))
# magic metodları kullanarak pythonun builtin metodlarını, operasyonlarını ve fonksiyonlarını kendi sınıflarımızda çalıştırabiliriz. bu şekilde kendi
# yazdığımız objeleri toplayabilir, print edebilir, indeksleyebilir, slice fonksiyonuyla kesebilir ve daha pek çok şeyi yapabiliriz.