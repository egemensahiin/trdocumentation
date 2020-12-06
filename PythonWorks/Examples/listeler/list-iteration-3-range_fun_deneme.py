# range fonksiyonu bir başlangıç noktasından (dahil) bir bitiş noktasına (dahil değil) kadar belirlenen se-
# kansta sayıları içeren, range tipinde generator bir obje oluşturur. bu obje for döngüsüne alındığında be-
# lirlenen bu sayılar teker teker çağırılır. syntax rance(başlangıç, bitiş, aralık) şeklindedir. başlangıç
# için değer girilmediğinde, default 0 olarak alınır. aralık için değer girilmediğinde default 0 olarak alı-
# nır.
range(10) # 0'dan 10'a kadar -10 dahil olmamak üzere- sayıları 1'er aralıkla çağırır.
print(range(10))
print(type(range(10)))

print()

for sayı in range(10):
    print(sayı)

print()

for sayı in range(5, 15):
    print(sayı)

print()

for sayı in range(10, 101, 10):
    print(sayı)

print()

# negatif değerleri de kullanmak mümkündür. aralık olarak negatif değerler girerek de küçükten büyüğe sayı-
# lar çağırılabilir.
for sayı in range(50, -1, -5):
    print(sayı)