import collections
# strinler, listeler, sözlükler, tuplelar gibi objeler, len fonksityonu ile kaç eleman barındırdığını verir. aslında burada gerçekleşen, len fonksiyonu çalış-
# tırıldığında obje üzerinde __len__ metodunun aranması ve çağrılmasıdır.
kelime = "abuzittin"
print(len(kelime))
print(kelime.__len__())
# kendi oluşturduğumuz objelerde de __len__ metodu tanımlayarak bunların istediğimiz şekilde uzunluk kazanmasını ve len fonksiyonu ile çıktı vermesini sağla-
# yabiliriz.
Kitap = collections.namedtuple("Kitap", ["isim", "yazar"])
hayvan_çiftliği = Kitap("Hayvan Çiftliği", "George Orwell")
hatıra_defteri = Kitap("Bir Delinin Hatıra Defteri", "Nikolay Gogol")
incognito = Kitap("Incognito", "David Eagleman")
# şimdi de bir kütüphane sınıfı tanımlayalım ve bu sınıfın örneklerinin boyu, kaç kitap barındırdıklarıyla ilişkili olsun.
class Kütüphane():
    def __init__(self, *kitaplar): # hatırlanacağı üzere "*", pozisyonel argümanların tümünü içeren bir tuple oluşturur. toplulukta yaygın olarak bu değişken
        # args olarak atanır ama bunu kitaplar yapmamak için bi sebep yok.
        self.kitaplar = kitaplar
        self.kütüphaneciler = []
    def iş_ver(self, eleman):
        self.kütüphaneciler.append(eleman)
    def işten_cikar(self, eleman):
        self.kütüphaneciler.remove(eleman)
    def __len__(self):
        return len(self.kitaplar)
# şimdi birkaç kütüphane tanımlayıp uzunluğuna bakalım
milli_kütüphane = Kütüphane(hayvan_çiftliği, hatıra_defteri)
eczacılık_kütüphane = Kütüphane(hatıra_defteri, hayvan_çiftliği, incognito)
eczacılık_kütüphane.iş_ver("Egemen Şahin")
print(len(milli_kütüphane))
print(len(eczacılık_kütüphane))
