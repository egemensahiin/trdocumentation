# bir modülü import ederken uzantıları kullanmıyoruz. import edeceğimiz modül, scriptimizle aynı klasörde ol-
# duğu için yalnızca modülün adıyla çağırıyoruz. tüm modüllerin programın başında import edilmesi gerekir ki
# yazısız bir kural olmasına karşın oldukça önemlidir. python bir modülü, bir kez import eder.
import calculator
# programı bu noktada çalıştırdığımızda çıktı olarak $ 4 çıktısını alırız. bunun sebebi modülde çalıştırdı-
# ğımız print fonksiyonudur. program çalıştığında python import keywordünü görür ve my_program.py'dan çıkıp
# calculator.py'ı çalıştırır; ardından kaldığı yerden devam eder. bunu görmek için importtan sonra bir print
# fonksiyonu çağıralım:
print("Bu satır my_program.py'da çalışıyor.")

print()

# artık "calculator"ı, bir değişkendir ve nitelikleri (attributes) depolayan bir modül objesini tanımlar:
print(type(calculator))
# "." notasyonunu (module.attribute) kullanarak bu modül objesindeki niteliklere ulaşabiliriz.
print(calculator.creator)
print(calculator.PI)
# bu değişkenleri "creator" veya "PI" olarak çağıramayız çünkü bu değişkenler bizim programımızda tutulan
# değişkenler değillerdir. bu değişkenleri calculator modülünden çağırabiliriz.
# print(creator) # bu satırlar çalıştırıldığında NameError alınır çünkü bu isimler my_program.py'da tanım-
# print(PI)      # lı değildir; bir modülü import etmek bunları tanımlı yapmaz.

print()

# bir de modülden bir fonksiyon çağırıp çalıştıralım:
print(calculator.add(3, 5))
print(calculator.area(5))