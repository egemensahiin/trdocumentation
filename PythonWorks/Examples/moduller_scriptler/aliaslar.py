# eğer import edilen bir modülü, import ettiğimiz isimle çağırmak istemiyorsak bunu bir alias'a yani takma ada
# tanımlaya biliriz. bunun için modülü import ederken "as" keywordü kullanılmaktadır.
import calculator as calc
# artık calculator modülü calc ile çağrılacak: ln 9
# bazı standart kütüphaneler için yazısız topluluk kuralları vardır. mesela datetime modülü çoğunlula dt ali-
# as'ı ile çağrılır:
import datetime as dt

print(calc.__name__)
print(calc.add(3, 5))

print()

print(dt.__name__)
print(dt.datetime(2020, 8, 9))