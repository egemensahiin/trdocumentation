# zip fonksiyonu, farklı listeleri indeks pozisyonuna dayanarak kombine eder ve çıktı olarak generator tipinde
# bir obje verir. bu obje çağırıldığında ortak indeks pozisyonuna göre farklı listelerdeki objeleri beraber
# çağırır.
öğrenciler = ["Egemen", "Gökhan", "Furkan"]
numaralar = ["15-224", "15-223", "16-088"]
dersler = ["Tekno", "Kimya", "Koloji"]
konular = ["Stabilite", "QSAR", "Farmakokinetik"]

# zip fonksiyonu syntaxı zip(iter1, [iter2, iter3...]) şeklindedir ve listeler dışındaki iterable objeleri de
# argüman olarak kabul eder (mesela stringler).

print(zip(öğrenciler, numaralar, dersler, konular)) # görüldüğü gibi buradan RAM'deki pozisyonu alırız.
print(type(zip(öğrenciler, numaralar, dersler, konular))) # veri tipi ise zip'tir.
# diğer generator tipindeki objelerde de yapabileceğimiz gibi eğer list fonksiyonu altında çağırırsak objenin
# depoladığı verileri liste şeklinde alabiliriz. söz konusu listenin elemanları özel bir veri tipi şeklinde
# olacaktır. söz konusu elemanlar ("1. listedeki obje", "2. listedeki obje"...) şeklindedir.
print(list(zip(öğrenciler, numaralar, dersler, konular)))

print()

# iterable objeler for döngüsüyle de çağırılabilir. bu şekildeki kullanımda, zip fonksiyonuna verilen her lis
# teden çağırılan eleman, farklı bir değişkenle çağırılır. mesela burada 4 liste olduğu için toplam 4 değiş-
# kenle çağrılmalıdır. her bir indeks için bir defa çağrılacağından toplam 3 defa çağrılacak.
for öğrenci, numara, ders, konu, in zip(öğrenciler, numaralar, dersler, konular):
    print(f"{numara} numaralı {öğrenci} isimli öğrencinin {ders} dersinde sorumlu olduğu ödev \
{konu} konusundandır.")
    print()