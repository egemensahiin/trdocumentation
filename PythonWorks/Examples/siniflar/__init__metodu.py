# paketlerdeki __init__.py modülüne benzer bir konsept sınıflarda da vardır. sınıf gövdesinde __init__ metodu tanımlandığında, diğer metodların aksine
# çağrılmaksızın, sınıfın her örneklendirilmesinde çalışır. bu yüzden buna magic metod da denir.
class Gitar(): # daha önceki derste metod tanımlamamıştık. python sınıflarına metod tanımlanması, fonksiyon syntaxıyla aynıdır. başka bir deyişle me-
    # todlar, sınıfların gövdesinde tanımlanan fonksiyonlardır.
    def __init__(self): # __init__ dosyası en az bir argüman tanımlanır ve python topluluğunda bu argüman çoğunlukla "self"tir. ne kadar argüman tanım-
        # lanırsa tanımlansın __init__ metoduna verilen ilk argüman, objenin kendisini refere eder. toplulukta genel kabul gören bir başka yazısız ku-
        # ral da; sınıf gövdesinde ilk tanımlanan metod (eğer kullanılıyorsa) __init__ metodudur.
        print(f"Yeni bir Gitar yaratıldı. Bu obje {self}")

akustik = Gitar() # self argümanının, bizim objemiz olduğunu görmek için akustik değişkenini print edebiliriz:
print(akustik)
elektro = Gitar()
print(elektro)