# len fonksiyonu, uzunluğu olan veri tipleri için geliştirilmiş bir built-in fonksiyon
# olup input olarak verilen objenin içerdiği birim sayısını çıktı olarak verir ve
# çıktısı veri tipi olarak int tipindedir.
print(len("Python")) # string tipinde bir veri. stringlerin birimleri içerdikleri ka-
# rakterlerdir.
print(len("12(&%)(")) # bu da string tipinde bir veri
print(len(" ")) # bu da
print(len("")) # ve hatte bu da
print(len({1, 2, 3, 4, 5})) # list tipinde bir veri
print(len({"a": "b"})) # dict tipinde bir veri
# len fonksiyonu içersine int, float, bool veya none tipinde bir obje konulduğunda
# TypeError verir. list, dict, string gibi uzunluğu olan veri tipleriyle çıktı verir.

# len fonksiyonuyla ilgili örnekler:
# mesela 16 -   . satırlar arası tanımlanan fonksiyon, içersindeki stringin uzaklığına
# göre bool tipinde bir veri vermektedir.
def uzunluk(text):
    a = len(text) > 10 # girilen stringin uzunluğu 10'dan büyük olduğunda çıktı olarak
    return a # boolean tipinde True verir çünkü kıyas operatörleri ile bir değişken
# oluşturulmuştur.
print(uzunluk("Python"))
print(uzunluk("bu string 35 karakter icermektedir."))

# bu örneği bir input fonksiyonuyla da taçlandırabiliriz.
sonuc = uzunluk(input("Write sth! "))
print("Is the thing you wrote longer than 10 characters?: ", sonuc)