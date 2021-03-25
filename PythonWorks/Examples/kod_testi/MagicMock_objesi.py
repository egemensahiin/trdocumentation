from unittest.mock import Mock, MagicMock

# normal mock objeleri, magic metodları desteklememektedir. bu sebeple len, bool gibi arkaplanda magic metod
# çalıştıran fonksiyonlarla, indeksleme gibi yine arkada magic metod çalıştıran operasyonlarla hata verirler.
# bunun için default olarak tanımlı magic metodları içeren MagicMocklar kullanılmaktadır. bunlar magic metodları
# destekler ve magic metodlar üzerinde return_value niteliğini değiştirerek istediğimiz davranışları sergileyebilirler.

duz_mock = Mock()
magic_mock = MagicMock()

# print(len(duz_mock)) # burası çalışınca TypeError alınır.
print(len(magic_mock)) # fakat burada TypeError yerine 0 alınır.
print(magic_mock.__len__())

# magic mock'un uzunluğunu, __len__ metodunun return_value niteliğini değiştirerek ayarlayabiliriz. aslında __len__
# metodu da yeni bir magic mock objesi üretir:
print(magic_mock.__len__)
# şimdi bunun return değerini değiştirelim:
magic_mock.__len__.return_value = 50
print(len(magic_mock)) # veya
print(magic_mock.__len__())

# print(duz_mock.__bool__()) # if ile kullanıldığında default olarak truthie olsa da düz mocklarda __bool__ metodu yoktur.
# bu sebeple 23. satır hata verir. fakat magic mockların __bool__ metodları vardır ve varsayılan olarak doğrudur.
print(magic_mock.__bool__())
# bu da yine farklı bir magic mock objesidir:
print(magic_mock.__bool__)
if magic_mock:
    print("merhaba")
# şimdi bunu false yapalım:
magic_mock.__bool__.return_value = False
if magic_mock:
    print("gule gule")

# magic mocklarda faydalı olan bir başka magic metod da, custom objelerin indekslenebilmesini sağlayan __getitem__ metodudur.
# print(duz_mock[2]) # görülebileceği gibi bu satır çalıştığında TypeError alınır çünkü düz mocklarda __getitem__ metodu yoktur.
print(magic_mock[3]) # magic mocklarda ise indeksleme durumunda başka bir magic mock üretilir. yalnız bu magic mock her indeks
# için farklı değildir. aslında bu magic mock __getitem__ metodudur ve her indeks için aynıdır:
print(magic_mock[100])
print(magic_mock["string"])
print(magic_mock.__getitem__())
# bu da yine return_value ile özelleştirilebilir.
magic_mock.__getitem__.return_value = 25
print(magic_mock[3])
print(magic_mock[100])
print(magic_mock["string"])
print(magic_mock.__getitem__())



