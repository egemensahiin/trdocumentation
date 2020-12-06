# list; string, integer, float, boolean gibi bir obje ve veri türüdür. list'lerin en önemli özelliği ve di-
# ğerlerinden farkı tıpkı stringlerin belli sıradaki karakterlerden oluşması gibi listler de belli sıradaki
# objelerden oluşurlar. listler homojen olmak zorunda değildir (programların doğası gereği genelde homojen
# olsalar da) ve içersinde herhangi bir tipte objeyi barındırabilir. list oluşturmak için [] veya list()
# yazılması yeterlidir. bu iki ifade de birer boş list belirtir. listler içerisine objeler virgül ile bir-
# birlerinden ayrılarak verilirler. listlerin önceki diğer objelerden (int, str, boolean, float) diğer bir
# önemli farkı mutable (değişebilir) olmasıdır.
boş = []
boş2 = list() # list() esasında aynı int gibi str gibi içersine verilen ifadeleri list tipine çeviren bir
#               fonksiyondur.
# listler de stringler gibi len() fonksiyonuyla çıktı verirler. len fonksiyonu bir listin içerdiği obje sa-
# yısını çıktı olarak verir.
print(len(boş))

# list'ler string içerebilir:
stringli = ["Egemen", "Gülzeynep"]
# eğer bir list print fonksiyonuna verilirse olduğu gibi []'lerle birlikte print edilir. Dikkat, hep tek
# tırnakla yazdırır stringleri.
print(stringli)
print(len(stringli))
stringli2 = ["Gülzeynep", "Egemen"]
print(["Egemen", "Gülzeynep"] == ["Gülzeynep", "Egemen"]) # görüldüğü üzere list elemanları yer değiştir-
# diğinde list de değişmiş olur. bu yüzden False çıkar.

# list'ler int'leri içerebilir.
intli = [12, 23, 34, 45]
print(len(intli))

# float'larla oluşturulabilirler.
floatlı = [3.14, 2.01, 0.01]
print(len(floatlı))

# boolean objelerinden oluşabilir.
boollu = [True, False, 5 > 3, 7 >= 9]
print(len(boollu))

# başka listelerden bile oluşabilir.
listli = [[True, False, 5 > 3, 7 >= 9], [3.14, 2.01, 0.01]]
print(len(listli))

# dediğimiz gibi homojen olmak zorunda değildir.
heterojen = [True, 3.14, 51, "python", ["farmasötik kimya", "farmasötik teknoloji"]]
print(len(heterojen))

print()

# in ve not in operatörleri tıpkı stringlerde olduğu gibi listlerde de kullanılabilmektedir.
öğünler = ["kahvaltı", "öğle yemeği", "akşam yemeği"]

print("kahvaltı" in öğünler)
print("Kahvaltı" in öğünler) # büyük küçük harf duyarlılığına dikkat!
print("atıştırmalık" in öğünler)
# not in operatörü de aynı şekilde kullanılır.
print("çerez" not in öğünler)
print("öğle yemeği" not in öğünler)

print()

sonuçlar = [100.00, 25.21, 58.03]

print(100.00 in sonuçlar)
print(100 in sonuçlar) # python 100.00 gibi tamsayıya karşılık gelen float'ları anlayabilir.
print(55 in sonuçlar)
print(25.21 not in sonuçlar)
print(3.14 not in sonuçlar)

print()

# in ve not in operatörleri boolean objeleri vermektedir. bu durumda bunları if veya while gibi koşul ifade-
# leriyle kullanmamızın bir sakıncası yoktur. mesela yazdığımız sayının sonuçlar isimli listede olup olma-
# dığını kontrol eden bir fonksiyon yazalım

def kontrol(a):
    if a in sonuçlar:
        print(f"Evet! {a} listede var.")
    else:
        print(f"Malesef {a} listede yok ://")

kontrol(5)
kontrol(58.03)

print()

# stringlerdeki gibi indexing uygulaması listlerde de mümkündür. yine aynı mantıkla çalışır; ilk elemanın
# indeks numarası 0'dır ve [] içersine indeks numarası yazılarak çağrılır.
samsunun_ilçeleri = ["BAFRA", "Atakum", "Yakakent", "ALAÇAM", "çrşb"]

print(samsunun_ilçeleri[2])
print(samsunun_ilçeleri[0])
# negatif indeksing de yine aynı mantıkla mümkündür.
print(samsunun_ilçeleri[-1])
print(samsunun_ilçeleri[-4])
# indeks numarası geçersiz olduğunda indeks error alınır:
# print(samsunun_ilçeleri[20])
# print(samsunun_ilçeleri[-9]) # satırları IndexError verir.

# list içersindeki stringi indeksle çağıırıp bu string içersindeki bir karakteri de yine indeksle çağırabi-
# liriz. bunun için peş peşe iki [] içersinde ilkine list içersinde çağrılmak istenen eleman, diğerine bu e-
# leman içersinden çağrılmak istenen karakter (str ise) veya eleman (list ise) için indeks numarası yazılır.
print(samsunun_ilçeleri[3][4])
print(samsunun_ilçeleri[-2][2])
print(samsunun_ilçeleri[1][-3])
print(samsunun_ilçeleri[-3][-1])

print()

# slicing de tamamen stringlerle aynı mantıktadır. listler mutable olmasına karşın slicing ile elde edilen
# listlerin yeni listler olduğu unutulmamalıdır. slicing ile tek bir eleman da kesilse oluşan çıktı list
# tipindedir. indeksing'de ise alınan indeksteki elementin tipi ne ise o tipte çıktı alınır.
ankaranın_ilçeleri = ["Çankaya", "Keçiören", "Yenimahalle", "Sincan", "Mamak", "Kayaş", "Kahramankazan"]

print(ankaranın_ilçeleri[1:3])
print(ankaranın_ilçeleri[1:2])

print(ankaranın_ilçeleri[0:2])
print(ankaranın_ilçeleri[:2])
print(ankaranın_ilçeleri[2:100])
print(ankaranın_ilçeleri[2:])

print(ankaranın_ilçeleri[-4:-2])
print(ankaranın_ilçeleri[-3:])
print(ankaranın_ilçeleri[:-1])
print(ankaranın_ilçeleri[1:-1])

print(ankaranın_ilçeleri[1:6:2])
print(ankaranın_ilçeleri[::-2])
print(ankaranın_ilçeleri[::-1])