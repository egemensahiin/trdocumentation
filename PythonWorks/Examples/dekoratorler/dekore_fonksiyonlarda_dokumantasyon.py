# hatırlanacağı üzere help fonksiyonu, herhangi bir "şey"in dökümantasyonuna ulaşmak için kullanılır. pythonda kendi yazdığımız kodlara da dökümantasyon
# oluşturmamız mümkündür. fonksiyonlar, ilk satıra yazılan stringi, help fonksiyonuyla döküman olarak verir.
def toplam(a, b):
    "İki sayıyı topluyor.\nBaşka da bir şey yapmıyor."
    return a + b
help(toplam)
print("-----")
# fakat iş dekoratörlerle tanımlanan fonksiyonlara gelince durum biraz değişiyor. tahmin edilebeleceği gibi dekore fonksiyonlar esasında dekoratör fonk-
# siyonun iç kısmını return ettiklerinden, help fonksiyonuyla bizim yazdığımız dökümantasyon yazdırılmıyor.
def karşılama(fn):
    def iç(*args, **kwargs):
        print("Fonksiyonu çalıştırıyorum...")
        sonuç = fn(*args, **kwargs)
        print("Fonksiyonunuzu çalıştırdım, iyi günler.")
        return sonuç
    return iç
@karşılama
def toplam(a, b):
    "İki sayıyı topluyor."
    return a + b
help(toplam) # çıktıda da görüldüğü gibi, ilk help fonksiyonu ile "toplam" fonksiyonu için dökümantasyon alırken bu help fonksiyonu içe "iç" fonksiyonu
# için dökümantasyon alıyoruz. bunu önlemek için  "iç" fonksiyonu, python kütüphanelerinde functools modülündeki bir dekoratör olan wraps dekoratörü ile
# tanımlanmalıdır:
import functools # normalde başta import edilir de neyse.
print("-----")
def karşılama_wrapped(fn):
    @functools.wraps(fn) # wraps dekoratörüne argüman olarak fonksiyon verilmelidir.
    def iç(*args, **kwargs):
        print("Fonksiyonu çalıştırıyorum...")
        sonuç = fn(*args, **kwargs)
        print("Fonksiyonunuzu çalıştırdım, iyi günler.")
        return sonuç
    return iç
@karşılama_wrapped
def toplam(a, b):
    "İki sayıyı topluyor.\nDaha ne yapsın."
    return a + b
help(toplam)
print(toplam(5, 3))