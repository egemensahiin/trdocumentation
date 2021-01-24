import random

# ranodom modülünde iterable objelerden seçim yapmamıza olanak veren iki fonksiyon choice ve sample fonksiyonlarıdır.
# choice fonksiyonu, argüman olarak verilen iterable objeden (hatırlamak gerekir ki iterable objeler, stringler, listeler veya tuple'lar gibi sıralı ob
# jelerdir. choice ile set veya sözlüklerden eleman seçilemez) rastgele bir elemanı çıktı olarak verir.
print(random.choice(["Egemen", "Gülzeynep", "Gökhan"]))
print(random.choice((1, 2, 5, 9, 10, 22)))
print(random.choice("EgemenŞahin"))

print()

# sample fonksiyonu ise yine iterable bir objeden bir örneklem seçer ve bunun listesini verir. seçilen örneklemin eleman sayısı ise 2. verilen argümana 
# göre belirlenir. eleman sayısı 1 olarak belirlense dahi çıktı bir elemanlı bir liste olur.
rastgele_sayılar = [random.randint(1, 50) for _ in range(50)]
print(rastgele_sayılar)
print(random.sample(rastgele_sayılar, 1))
print(random.sample(rastgele_sayılar, 6))