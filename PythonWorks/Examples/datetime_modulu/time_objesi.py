# time objesi de date objesine benzer şekilde datetime modülünde yer alan bir sınıf olup, herhangi bir tarih olmaksızın zaman ifadesidir (yani saat)
from datetime import time

# date objesinin aksine, hiçbir argüman verilmediğinde time objesi gece yarısını verir. date ise argüman verilmediğinde TypeError verir.
geceYarısı = time()
print(geceYarısı)
print(type(geceYarısı))

# time objeleri, saat, dakika, saniye ve mikrosaniye argümanları kabul eder ve verilmeyen argümanlar default olaraz 0'dır.
print(geceYarısı.hour)
print(geceYarısı.minute)
print(geceYarısı.second)
print(geceYarısı.microsecond)

# mesela yalnızca 6'yı argüman olarak girersek saat 6'yı elde ederiz.
print(time(6))
# veya keyword argümanları da kullanabiliriz:
print(time(hour = 6))
print(time(18))
print(time(13, 27))
print(time(hour = 13, minute = 27))

# date objelerinde olduğu gibi uygun olmayan kullanımlarda ValueError alınır.
