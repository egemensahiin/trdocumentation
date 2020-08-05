# enumerate fonksiyonu da reversed fonksiyonuna benzer şekilde generator tipinde bir obje oluşturur. bu obje
# print fonksiyonuyla yazdırıldığında benzer şekilde hafızadaki konumu çıktı olarak görülür. yine reversed
# fonksiyonu gibi sıralı tipteki objelerde (string ve list) kullanılmaktadır. enumerated bir list veya string
# for döngüsüne sokulduğunda eleman veya karakterleri tek tek çağırmakla kalmaz bunların indeks numaralarını
# da çağırır. iki örnekle inceleyelim:
dersler = ["Farmasötik Kimya", "Farmasötik Teknoloji", "Farmasötik Toksikoloji", "Farmasötik Bakım"]
# şimdi bunu enumerate edelim:
print(enumerate(dersler))
# bir de hangi tip olduğuna bir bakalım:
print(type(enumerate(dersler)))
# bir for döngüsünde bu objeyi kullanalım:
for indeks, ders in enumerate(dersler): # enumerated (numaralandırılmış) bir objeyi for döngüsünde kullanırken
    print(f"{indeks} numaralı ders {ders} dersidir.") # iki değişken tanımlanır. ilk değişken, indeks numarası
    # ikinci değişken ise elemanın kendisi için kullanılır.
print()
# daha kullanıcı dostu ve saymaya birden başlayan bir program oluşturmak için indeks numarasına tanımlanan
# değişkenle matematiksel işlemler yapabiliriz.
for indeks, ders in enumerate(dersler):
    print(f"{indeks + 1} numaralı ders {ders} dersidir.")
print()
# veya aynı şeyi yapmak için enumerate fonksiyonun start parametresini değitirebiliriz. bu parametre default
# olarak 0'dır. bunu 1 yaptığımızda indeks'leri saymaya 1'den başlar. dikkat, objeleri okumaya 1. indeksten
# başlamaz, yine 0. indeksten başlar ama numaraları atamaya 1den başlar. aslında indeks numarası atama olayı
# fonksiyonun defaultudur. fonksiyon bir hangi sayıdan başlayarak numaralandırmak istersek elemanları öyle
# numaralandırır.
for numara, ders in enumerate(dersler, 1):
    print(f"{numara} numaralı ders {ders} dersidir.")
print() # farklı bir şeyler deneyelim:
sayı = 0
for numara, ders in enumerate(dersler, 1):
    print(f"{ders}, ", end = "")
print(f"olmak üzere toplam {numara} ders vardır.")

print()

# aynı syntax, stringler için de geçerlidir.
deneme = "jfalkfmaln"
print(enumerate(deneme))
print(type(enumerate(deneme)))

print()

for indeks, harf in enumerate(deneme):
    print(f"Stringin {indeks}. indeksteki karakteri {harf} karakteridir.")
print() # veya
for numara, karakter in enumerate(deneme):
    print(f"Stringin {numara + 1}. karakteri {karakter} karakteridir.")
print() # veya
for numara, karakter in enumerate(deneme, 1):
    print(f"Stringin {numara}. karakteri {karakter} karakteridir.")