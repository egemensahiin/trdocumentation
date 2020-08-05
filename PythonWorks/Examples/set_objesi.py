# set; değiştirilebilen (mutable), sırasız ve tekrarlanan elemanları barındırmayan bir obje türüdür. sözlük-
# lerde olduğu gibi {} içerisinde tanımlanırlar fakat "," ile birbirinden ayrılan elemanlardan oluşurlar.
# setler kendileri değişebilir olmasına karşın elemanları değişmez (immutable) tipte objeler olmalıdır. lis-
# teler ve sözlükler gibi değişebilen objeler setler içerisinde eleman olarak tutulamaz.
# setlerin listelerden farklarını iyi kavramak gerekir. setlerin en karakteristik özellikleri eleman tekra-
# rına izin vermemeleridir. eğer bir set tanımlanırken aynı eleman birden fazla sefer yazılırsa set bu ele-
# mandan yalnızca bir tane tutar. ayrıca setler sıralı objeler değildir ve özellikle eleman tekrarı ile ta-
# nımlandıkları durumlarda elemanların sırası oldukça rastlantısaldır (döngülere sokulmaları gibi durumlar-
# da). sırasız objeler olması dolayısıyla indekslenmezler ve set[index] gibi bir kullanım TypeError meydana
# getirir.
# bir set tanımlayalım:
dosya_sistemleri = {"NTFS", "BTRFS", "EXT", "NTFS"}
# yukarıdaki sette "NTFS" stringinin tekrarlandığını görüyoruz fakat set içersinde tek bir "NTFS" bulunur
# çünkü setler, tekrarlanan objeleri dikkate almaz:
print(dosya_sistemleri)
print(len(dosya_sistemleri))

print()

# in ve not in operatörlerini setler ile kullanmak mümkündür.
print("NTFS" in dosya_sistemleri)
print("ZFS" in dosya_sistemleri)
print("FAT" not in dosya_sistemleri)

print()

# for döngülerinde de setleri kullanmak mümkündür.
for sistem in dosya_sistemleri:
    print("Dosya sistemi:", sistem)

print()

# şekil olsun bir de tuple'lı bir set tanımlayıp iç içe for döngüsü kuralım:
loto = {
    (1, 16, 23, 37, 38, 40),
    (3, 11, 27, 30, 41, 44),
    (3, 11, 27, 30, 41, 44),
}
print(loto)
for numaralar in loto:
    toplam = 0
    for numara in numaralar:
        toplam += numara
    print(toplam)

print()

# comprehension anlayışı, listeler ve sözlüklerde olduğu gibi setlerde de mümkündür. başka bir iterable
# objeden set oluştumak için kullanılabilir fakat eleman tekrarı durumları göz önünde bulundurulmalıdır.
# güzel bir örnek, negatif ve pozitif sayılardan oluşan bir listeden bunların kareleri ile bir set oluş-
# turulmasıdır:
sayılar = [-3, -2, -1, 1, 2, 3]
print(sayılar)
kareler = {sayı ** 2 for sayı in sayılar}
print(kareler)
# görebileceğimiz gibi 6 elemanlı bir listeden, elemanların tekrarlanması dolayısıyla 3 elemanlı bir set el-
# de ettik.
print("Sayılar listesinin uzunluğu:", len(sayılar))
print("Kareler setinin uzunluğu:   ", len(kareler))

print()

# list(), dict() gibi fonksiyonlara benzer olarak; iterable bir objeden, set oluşturmak için set() fonksiyo-
# nu kullanılır. pythonda boş set oluşturmanın tek yolu da set() fonksiyonudur çünkü {}, boş bir set değil
# boş bir sözlük tanımlar.
print(set())
print(set([1, 2, 3]))               # listeler,
print(set((1, 2, 3, 3, 2, 1)))      # tuple'lar,
print(set("Egemen"))                # stringler
print(set({"k1": "v1", "k2": "v2"}))# ve sözlükler set oluşturmak için set fonksiyonundan geçirilebilir.
# sözlüklerden set, liste veya tuple oluşturmak istediğimizde söz konusu objeler sözlüğün key'leriyle o-
# luşturulur.