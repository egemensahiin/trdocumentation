# dictionary (bazı dillerde map, hmap gibi isimleri de vardır.) objeler arasındaki ilişkileri bildiren düzen-
# siz bir objedir. bu objeleri gerçek sözlüklere benzetecek olursak tanımlanan objeye yani sözlükteki keli-
# meye key (anahtar/tanımlayıcı); karşılık gelen tanıma ise value (değer) denir. değerler (value'lar) herhan-
# gi bir python objesidir.
# sözlük tipindeki objeler, değiştirilebilen objelerdir. yeni bir eleman eklenebilir veya silinebilir; ta-
# nımlayıcılar veya tanımlar güncellenebilir.
# bu objelerde key'ler tektir, tekrarlanmaz fakat value'lar tekrarlanabilir. value'lar herhangi bir python
# objesi olabilirken key'ler değişmez bir obje (string, integer, float veya tuple gibi) olmalıdır.
# listelerin aksine sözlükler düzenli objeler değillerdir. yani listeler, objeleri belli bir düzende barın-
# dırırken sözlükler, objeler arasındaki ilişkiyi barındırır.
# listelerdeki [], stringlerdeki "" veya tuple'lardaki () gibi bir sözlük tanımlamak için kıvrımlı paran-
# tezler yani {} kullanılır. tek başlarına {}, boş bir sözlük belirtir.
boş = {}
print(type(boş))
# boş bir sözlük oluşturmak için dict fonksiyonu da kullanılabilir. hiçbir input verilmediğinde dict fonk-
# siyonu boş bir sözlük oluşturur.
boş = dict()
print(type(boş))
# bir sözlük tanımlanırken syntax şöyledir: {key: value, ...}
aile = { # satır başı sadece okunurluk için. zorunlu değil ama güzel.
    "Anne": "Ayten Şahin",
    "Baba": "Mehmet Şahin",
    "Kardeş": "Gizem Şahin",
    "Sırdaş": "Gizem Şahin", # daha önce de dediğimiz gibi; bu sözlüğe bir kardeş daha tanımlayamayız ama 
    # bir değeri yani "Gizem Şahin" stringini birden fazla defa tanımlayabiliriz.
    "Diğerleri": ["Şampiyon", "Annemin çiçekleri"] # değişebilen bir objeyi yani buradaki gibi bir listeyi
    # key olarak kullanamayız ama value olarak kullanabiliriz.
}

# bir sözlüğün elemanları key-value çiftleridir. yani bu sözlüğün uzunluğu 5'tir:
print(len(aile))

print()

# sözlük oluşturmanın bir başka yöntemi de dict fonksiyonudur. bir stringdeki karakterleri listeleyen list()
# fonksiyonu gibi dict fonksiyonu da bir argümanı, sözlük formatında bir objeye çevirir. argüman olarak bir
# iç içe liste kabul eder ve söz konusu liste, key-value çiflerinin listelerinden oluşmuştur. yani dict fonk-
# siyonu için uygun bir argüman; [[key1, value1], [key2, value2], ...] formatında bir listedir.
ülkeler = [
    ["Almanya", "Avrupa"],
    ["Türkiye", "Orta Doğu"],
    ["Çin", "Asya"]
]
print(dict(ülkeler))
# listeler yerine tuple'lar, tuple içinde listeler veya liste içinde tuple'lar vs de kullanılabilir. örnek o-
# larak bir tuple içinde tuple formatını görebiliriz:
ülkeler = (
    ("Almanya", "Avrupa"),
    ("Türkiye", "Orta Doğu"),
    ("Çin", "Asya")
)
print(dict(ülkeler))

print()

# listelerde, tuplelarda ve stringlerde bir eleman, indeks numarasıyla çağrılır. fakat sözlükler, bunların
# aksine düzensiz yani sırasız objelerdir; indeks numaraları ile sözlüklerin elemanları çağırılamaz. indeks
# syntaksına benzer şekilde sözlüklerde tanımlar çağrılır. bunun için indeks numarası yerine tanımlayıcılar
# yazılır:
uçuş_fiyatları = {
    "Helsinki": 600,
    "İstanbul": 120,
    "Samsun": 250
}
# samsuna uçuş fiyatını almak için uçuş_fiyatları[2] geçerli bir syntax değildir. bunun için:
print(uçuş_fiyatları["Samsun"])
# sözlükte olmayan bir key ile bu syntax kullanılırsa indexerror'a benzer şekilde KeyError alınır. Ayrıca
# büyük küçük harf duyarlılığı da söz konusudur. yani:
# print(uçuş_fiyatları["helsinki"]) # veya
# print(uçuş_fiyatları["Londra"]) # çalıştırıldığında KeyError verir.

# bir örnek daha yapalım:
oda_içeriği = {
    30: ["Tek kişilik yatak"],
    50: ["Tek kişilik yatak", "Odada banyo"],
    70: ["Çift kişilik yatak", "Odada banyo", "Havuz"]
}
# 50 tllik odanın içeriği:
print(oda_içeriği[50])

# başka bir yöntemse get metodudur. get metodu iki argüman kabul eder: ilk argüman tanımına ulaşılmak is-
# tenen tanımlayıcıdır. ikinci argüman ise tanımlayıcı bulunamadığında verilmesi istenen çıktıdır. eğer
# ikinci argüman girilmezse python bulunamayan objeler için None çıktısını verir (obje olan). yani get
# metoduyla KeyError alınmaz; eğer programın key bulunamasa dahi yürümesi gerekiyorsa uygun bir yöntemdir.
# programın yürümesi için geçerli bir key şart ise ve aksi halde durması isteniyorsa key metodu kullanı-
# labilir.
print(oda_içeriği.get(30, ["Tuvalet"]))
print(oda_içeriği.get(100, ["Tuvalet"]))
print(oda_içeriği.get(100, ["Tuvalet"]))

print()

# in ve not in operatörleri sözlüklerde key'leri arar, tanımları aramaz. eğer aranan key, sözlükte varsa
# in operatörüyle true, not in operatörüyle false alınır. aksi halde in operatörü false, not in operatö-
# rü ise true çıktısı verir.
print("Samsun" in uçuş_fiyatları) # True
print("Muş" in uçuş_fiyatları) # False
# büyük küçük harf duyarlılığı, dikkat edilmesi gereken bir noktadır:
print("helsinki" in uçuş_fiyatları) # Fale
print("helsinki" not in uçuş_fiyatları) # True

# bir key'i kontrol ederken if ifadesiyle beraber in-not in operatörlerini kullanmak, uzun da olsa bir
# yöntemdir:
if "20" in oda_içeriği:
    print(oda_içeriği[20])
else:
    print("Verilen fiyatta bir oda mevcut değildir.")
# tabii ki tüm bu uzun syntax yerine get metodu daha pratik ama başka kodlarda kullanılabilir veya get me-
# todunun yerine aranan tanımlayıcı bulunamadığında, bir fonksiyon çalıştırılabilir.

print()

# SÖZLÜKLERİN DEĞİŞTİRİLMESİ

# sözlüklerde bir key,[] syntaxı ile çağrılırken bulunamadığı takdirke KeyError verdiğini söylemiştik. lis-
# telerin aksine sözlüklerde, var olmayan bir key'i çağırıp, = operatörüyle bir value atayabiliriz. aynısını
# listelerde var olmayan bir indeks numarasına eleman atamak için uygulamayamıyorduk fakat bu syntax söz-
# lüklerde var olmayan bir key için value atarken geçerlidir.
oyun_ayarları = {}
print(oyun_ayarları)
# şimdi bu ayarlara, ayar: değer şeklinde ayarlar ekleyelim:
oyun_ayarları["altyazı"] = True
oyun_ayarları["zorluk"]  = "orta"
oyun_ayarları["ses"]     = 70
print(oyun_ayarları)

# sözlüklerdeki bir key-value çiftinin değiştirilmesi listelerdeki syntaxa benzer. sözlükteki key, [] ile
# çağırılır ve yerine başka bir value atanır:
oyun_ayarları["altyazı"] = False
oyun_ayarları["ses"]     = 52
print(oyun_ayarları)

# çağrılan key yoksa oluşturur yukarıda dediğimiz gibi
oyun_ayarları["vsync"]   = False
print(oyun_ayarları)

# key olarak kullanılan objeler statik olmak zorunda değildir. değiştirilemez objeler oldukları müddetçe
# list iteration gibi yöntemlerle çağrılan dinamik objeler de olabilirler. mesela bir listede bir kelime-
# nin kaç defa geçtiğini sözlük formatında veren bir fonksiyon yazalım:
def uzunluk(liste):
    # önce boş bir liste oluşturalım:
    uzunluklar = {}
    for eleman in liste:
        if eleman in uzunluklar: # eleman uzunluklarda hali hazırda tanımlıysa:
            uzunluklar[eleman] += 1 # karşılık geldiği değeri bir arttır.
        else: # eleman uzunluklarda tanımlı değilse:
            uzunluklar[eleman] = 1 # o zaman 1 değerine tanımla.
    return uzunluklar

kelimeler = ["aman", "aman", "kimler", "buradaymış"]
print(uzunluk(kelimeler))
vay_be = ["hey", "gidi", "günler", "hey", "hey"]
print(uzunluk(vay_be))

# sözlüklere eleman eklemenin bir diğer yolu da setdefault metodudur. setdefault metodu, get metoduna ben-
# zer bir mantıkla çalışır; ilk argüman sözlükte aranır, eğer yoksa None çıktısı alınır eğer ikinci bir
# argüman verilirse bu argüman value olarak alınır fakar get metodunun aksine setdefault metodu, sözlükte
# olmayan key'leri söz konusu value ile birlikte (None veya verilen argüman) sözlüğe yazar.
oyun_ayarları.setdefault("ses", 75) # eğer aranan key, sözlükte varsa değişiklik olmaz
print(oyun_ayarları)
oyun_ayarları.setdefault("tamekran") # bir argüman verilmediğinden 'tamekran': None listeye eklenir.
print(oyun_ayarları)
oyun_ayarları.setdefault("çözünürlük", "1920x1080") # key, sözlükte yok. verilen default ile listeye eklenir.
print(oyun_ayarları)

print()

# sözlülerden key-value çiftlerinin çıkarılması için ilk yöntem del keywordüdür. del keywordü basitçe []
# içinde verilen key'i ve karşılık gelen value'u siler. bir çıktı vermez; eğer sözlükte olmayan bir key
# verilirse KeyError verir.
tarkan_albümleri = {
    "Yine Sensiz"  : 1992,
    "Acayipsin"    : 1994,
    "Düş Bahçeleri": 1996,
    "Ölürüm Sana"  : 1997,
    "Karma"        : 2001,
    "Dudu"         : 2003
}
# şimdi buradan düş bahçelerini silelim çünkü tarkanın değil sezen aksunun albümü.
del tarkan_albümleri["Düş Bahçeleri"]
print(tarkan_albümleri)
# del tarkan_albümleri["Sen Ağlama"] # bu satırı çalıştırdığımızda hata alırız çünkü sözlükte böyle bir key
# yok zaten Sen Ağlama da tarkanın değil sezen aksunun albümü.

# bir başka ve daha kullanışlı yöntem ise listelerde de kullandığımız pop() metodu. listelerde pop metoduna
# bir argüman verilmediğinde son indeksteki elemanı siler fakat sözlükler sırasız objeler oldukları için son
# indeks gibi bir kavram sözlükler için geçersizdir, böyle bir durumda TypeError alınır. del keywordunden
# farklı olarak pop metodu listeyi değiştirmekle kalmaz, çıkarılan key'e karşılık gelen value'u çıktı olarak
# verir, yani bunu bir değişkene atayabiliriz.
en_iyi_yıl = tarkan_albümleri.pop("Karma")
print(tarkan_albümleri)
print(en_iyi_yıl)
# pop metodu da verilen tanımlayıcıyı sözlükte bulamadığında KeyError verir. fakat bunu önlemek için pop
# metodunu ikinci bir argümanla besleyebiliriz. pop metodunun kabul ettiği ikinci argüman, sözlükte key'i
# bulamadığında çıktı olarak verilir. eğer key sözlükte varsa çıktı olarak bu argüman verilmez.
# tarkan_albümleri.pop("10") # bu satır çalışınca KeyError alınır. ama tarkanın bu albümü çıkarması daha
# büyük bir hata...
ikinci_argüman = tarkan_albümleri.pop("10", "Bu albüm bunu haketmiyor...") # bu durumda sözlükte bir deği-
# şiklik olmaz çünkü eleman zaten listede yok. ama keyerror yerine çıktı olarak ikinci argüman alınır.
print(tarkan_albümleri)
print(ikinci_argüman)
sözlükte_var = tarkan_albümleri.pop("Yine Sensiz", "Bunu bilmiyordum :/") # bu sefer key-value çifti sili-
# necek ve çıktı olarak ikinci argüman değil 1992 alınacak.
print(tarkan_albümleri)
print(sözlükte_var)

print()

# clear metodu listelerde olduğu gibi çalışır, sözlükteki tüm key-value çiflerini silip boş bir sözlük o-
# luşturur. sözlük silinmez, içi boşaltılır:
websiteleri = {
    "DuckDuckGo": "http://www.duckduckgo.com",
    "ArchWiki"  : "http://wiki.archlinux.org",
    "Reddit"    : "http://www.reddit.com"
}
print(websiteleri)
websiteleri.clear()
print(websiteleri)
# listeyi tamamen hafızadan silmek için hiçbir argüman kullanmaksızın del keywordu kullanılır:
del websiteleri
# print(websiteleri) # bu satır çalışınca NameError alınır çünkü artık böyle bir değişken yoktur.

print()

# sözlüklerin değiştirilmesinde bir başka yaklaşım da update metodudur. update metodu bir sözlük ile çalış-
# tırılır ve argüman olarak da başka bir sözlük alır ve argüman olarak verilen sözlüğü, değiştirilen sözlü-
# ğe katar. metodun çalıştırıldığı sözlük değişir fakat eklenen sözlük aynı kalır. önemli bir nokta da şu-
# dur; eğer eklenen sözlükte, ana sözlükte de olan bir key varsa (key'ler tekrarlanamadığı için) ana sözlük-
# teki key value çifti, ana sözlüktekiyle değişir.
maaşlar = {
    "Abuzittin"  : 6000,
    "Abdurrezzak": 4000,
    "Mahmut"     : 7000,
}
print(maaşlar)
ekstra_maaşlar = {
    "Ciguli"     : 4500,
    "Mahmut"     : 5000
}
maaşlar.update(ekstra_maaşlar)
print(maaşlar) # görüldüğü gibi güncel haline ciguli eklenmiş ve mahmutun karşılık geldiği value değişmiş.
print(ekstra_maaşlar) # görüldüğü gibi ana sözlük değişirken eklenen sözlük değişmedi.

print()

# listelerde kullandığımız sort() fonksiyonunu sözlüklerde de kullanmak mümkündür. sort fonksiyonu çıktı o-
# larak liste vermektedir ve söz konusu sözlükler olduğunda bu liste, key'lerin alfabetik veya numerik ola-
# rak sırayla bulunduğu bir listedir.
döviz = {
    "Dolar"      : 6.86,
    "Euro"       : 7.73,
    "Isveç Kronu": 0.74
}
print(sorted(döviz))