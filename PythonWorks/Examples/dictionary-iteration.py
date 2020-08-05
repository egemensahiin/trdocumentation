quick_china = {
    "Wonton Çorbası"        : 24,
    "Çin Böreği"            : 25,
    "Yeşil Biberli Dana Eti": 59
}

# sözlüklerin iterasyonunda ilk yöntem, listelerde olduğu gibi for keywordudür fakat sözlüklerin listeler gibi
# sıralı objeler olmadığı unutulmamalıdır. sözlükler for keywordüyle itere edilirken sadece keyler çağırılır.
# value'lar [] syntaxıyla for döngüsünde çağrılabilir.
for yemek in quick_china:
    print(f"{yemek} yemeğinin fiyatı {quick_china[yemek]} liradır.")

print()

# daha "pythonik" bir yaklaşım ve pratik bir kullanım için items() metodu kullanılır. items metodu, bir söz-
# lük üzerinde çalıştırılır ve çıktı olarak bir iterator obje verir. bu objenin tipi dict_items'dir ve key-
# value çiflerinin oluşturduğu tuple'ların bir listesidir.
print(quick_china.items())
print(type(quick_china.items()))
# bu objeyi for döngüsüne soktuğumuzda her bir key-value çifti için bir tuple elde ederiz:
for çift in quick_china.items():
    print(çift)
# fakat bu gibi bir syntaxta, tuple unpacking syntaxını kullanarak key ve value'ları ayrı değişkenlere atamak
# oldukça pratiktir. hatırlanacağı gibi unpacking syntaxında tuple'ı bir yerine bir kaç değişkene atayarak
# her bir indeksin farklı değişkenlere atanması söz konusuydu. bunu doğrudan for döngüsünde kullanmamız da
# mümkün. tuple'ın 0. indeksi key, 1. indeksi ise valueya karşılık gelir.
for key, value in quick_china.items():
    print(f"{key} yemeğinin fiyatı {value} liradır.")
# bir kural, zorunluluk olmasa da bu syntaxta eğer key veya value'ya iterasyonda ihtiyacımız yoksa _ değiş-
# kenine atanır. bu python kullanıcıları arasında yaygın bir kullanımdır ve karşılaşılabilir.
for _, fiyat in quick_china.items():
    print(f"Adisyona {fiyat} lira ekle.")

print()

# benzeri bir iterasyonu, keys ve values metodlarını kullanarak da uygulamak mümkündür. bunlar da yine items
# gibi itere edilebilen objeler olan dict_keys ve dict_values tipinde objeler verirler.
print(quick_china.keys())
print(type(quick_china.keys()))
print(quick_china.values())
print(type(quick_china.values()))
for yemek in quick_china.keys():
    print(f"Sıradaki yemek {yemek}.")
for fiyat in quick_china.values():
    print(f"Adisyona {fiyat} lira ekle.")
# keys ve values metodları liste, tuple veya sözlük tipinde objeler olmamasına karşın in keywordü ile kullanı-
# labilirler. bu da bize value'lar veya key'ler için ayrı ayrı sorgu yürütme imkanı sunar:
print("Çin Böreği" in quick_china.keys()) # esasında doğrudan "Çin Böreği" in quick_china ile hemen hemen ay-
# nı fakat daha anlaşılır.
print("California Roll" in quick_china.keys())
print(75 in quick_china.values())
print(59 in quick_china.values())
# ayrıca bu objeler, len gibi fonksiyonlara da sokulabilir fakat zaten key'ler ve value'lar aynı sayıda ol-
# duğu için gereksizdir esasında.

# itere edilebilen bu objelerle çalışan fonksiyonlara bir başka örnek de sorted fonksiyonudur. sözlüklerde
# olduğu gibi sözlüklerden türetilen iterable objelerde de sorted fonksiyonu öncelikle key'leri sıralar.
for yemek, fiyat in sorted(quick_china.items()):
    print(f"Sıradaki yemek {yemek}, {fiyat} lira.")
# valueları sıralamak için basitçe values metodu kullanılabilir.
for fiyat in sorted(quick_china.values()):
    print(f"Bir sonraki yemeğin fiyatı {fiyat} liradır.")

# pythonla yazılmış programlarda sık karşılaşılan bir konsept, iç içe objelerdir. örneğin bir liste içinde
# sözlükler tanımlayalım
konser_katılımcıları = [
    { "isim": "Abuzittin",  "bölüm": 400, "fiyat": 49.99 },
    { "isim": "Muhittin",   "bölüm": 200, "fiyat": 99.99 },
    { "isim": "Şerafettin", "bölüm": 100, "fiyat": 00.00 },
]
for katılımcı in konser_katılımcıları:
    print("--------------------")
    for key, value in katılımcı.items():
        print(f"{key}: {value}")
