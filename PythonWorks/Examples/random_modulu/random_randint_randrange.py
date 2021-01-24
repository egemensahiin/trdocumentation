# random modülü, pythonda rastgelelikle ilgili nitelik ve metodları içeren standart bir kütüphanedir.
import random

# random modülündeki aynı isimli random fonksiyonu, 0 ile 1 arasında rastgele bir ondalıklı sayı verir:
print(random.random())
print(type(random.random()))
# %likli sayılar elde etmek gibi amaclarla kullanılabilir. veya farklı bir aralıkta bir ondalıklı sayı elde etmek için başka bir sayıyla çarpılabilir.
# mesela 0 ile 100 arasında bir ondalıklı sayı elde etmek için:
print(random.random() * 100)

print()

# ondalıklı sayılar yerine tam sayılarla çalışmak için randint fonksiyonu kullanılır. randint iki argüman kabul eder ve ilk sayıdan son sayıya kadar 
# rastgele bir tamsayı verir. pythondaki pek çok diğer konseptin (mesela indeksleme gibi) aksine hem başlangıç hem de bitiş noktası DAHİLİdir.
print(random.randint(5, 10))

print()

# randint'e benzer bir fonksiyon da randrange fonksiyonudur. randrange, verilen bir aralıkta rastgele bir sayı verir fakat randint'ten farklı olarak
# 3. bir argüman kabul eder ki o da adım sayısıdır. bir diğer farkı ise indekslere benzer şekilde başlangıç dahili iken bitiş HARİCİdir.
print(random.randrange(0, 50)) # adım default olarak 1'dir. bitişin dahil olmasını istemediğimiz durumlarda kullanılabilir.
print(random.randrange(0, 50, 10)) # bu yazımda ise 0dan 50ye kadar 10 sayıdan birini alırız. yani muhtemel değerler 0, 10, 20, 30 ve 40'tır. mesela 50yi
# de dahil etmek için:
print(random.randrange(0, 51, 10))