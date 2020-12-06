# bir list veya stringi tersten çağırmanın bir yolu da reversed fonksiyonudur fakat bu fonksiyonla indeks sli-
# cing yönteminde olduğu gibi (obje[::-1]) yeni bir list veya string değil farklı tipte bir objedir ve print
# fonksiyonuna sokulduğunda objenin tersine sıralanmış halini değilobjenin RAM içersinde depo edildiği konu-
# mu alırız. reversed fonksiyonuyla oluşan objelerin genel adı generator'dür. reversed fonksiyonu altındaki
# stringlerin tipi 'reversed', listlerin tipi ise 'list_reverseiterator'dur. bu fonksiyon esasında çok bü-
# yük verileri depolamada kullanılan yöntemlerden biridir. mesela çok uzun bir metindeki her satırı string
# olarak kaydetmek için tek tek programa yerleştirirsek program çökebilir veya çok yavaşlar fakat bu gibi
# fonksiyonlar yardımıyla metni doğrudan programa eklemek, kopyalamak yerine bir bağlantı gibi çalışır ve
# teker teker çağırır, hepsini aynı anda hafızaya almadığı için program çökmez.
liste_örnek = ["Snape", "Dumbledore", "Sirius", "Lupin"]
# reversed fonksiyonuyla bu listeyi çağırdığımızda RAM'deki konumunu görürüz, ters çevrilmiş halini değil:
print(reversed(liste_örnek))
# bi de bu objenin tipine bakalım:
print(type(reversed(liste_örnek)))

print()

# bir de string inceleyelim:
string_örnek = "Bu örnek bir stringdir."
print(reversed(string_örnek))
print(type(reversed(string_örnek)))

print()

# bu objeleri for döngüsü içersinde kullanabiliriz.
for element in reversed(liste_örnek):
    print(f"{element} kelimesi {len(element)} adet karakterden oluşmuştur.")
# veya string için
for harf in reversed(string_örnek):
    print(harf, end = "") # şeklinde stringi tersten yazdırabiliriz. aynısı [::-1] ile de yapılabilir ama
# çok uzun verilerde reversed fonksiyonu daha kullanışlıdır.