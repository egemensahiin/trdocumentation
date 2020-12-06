# ---- Setlerin Değiştirilmesi ---- #
# -- Eleman Eklenmesi: Daha önce de bahsettiğimiz gibi setler, değiştirilebilir objelerdir. setlere eleman
# eklenmesi için iki metod kullanılır:
# add metodu ile set'e bir adet eleman eklenir. yalnız listelerde olduğu gibi eleman setin başına, sonuna
# veya herhangi bir yerine eklenmez çünkü teknik olarak setlerde "herhangi bir yer" yoktur, setler indeks-
# lenmezler.
favorite_wms = { "i3wm", "qtile", "awesomewm" }
print(favorite_wms)
# şimdi bu set'e spectrwm'i de ekleyelim:
favorite_wms.add("spectrwm")
print(favorite_wms) # görüldüğü üzere yeni eklenen elemanın yeri rastlantısaldır çünkü teknik olarak yeri
# yoktur.
# eğer set içersinde olan bir elemanı eklemek istersek bir değişiklik olmaz çünkü setler eleman tekrarına
# izin vermeyen objelerdir.
favorite_wms.add("qtile")
print(favorite_wms)

print()

# update metodu ise argüman olarak bir iterable obje kabul eder ve set'e birden fazla eleman eklemek için
# kullanılır. tekrar eden elemanlar verildiğinde hata alınmaz, basitçe bu elemanların sayısı teke düşürü-
# lür.
favorite_distros = {"Arch", "Debian"}
print(favorite_distros)
favorite_distros.update(["LinuxMint", "Manjaro"])
print(favorite_distros)
favorite_distros.update(["ArchLabs", "Debian"])
print(favorite_distros)

print()

# -- Eleman Çıkarılması: setlerden eleman çıkarılması için iki metod kullanılır:
# remove metodu, kendisine verilen argümanı setten çıkarır ve eğer argüman sette yoksa KeyError verir.
doctors = { "Matt Smith", "David Tennant", "Peter Capaldi", "Jodie Whittaker" }
print(doctors)
doctors.remove("Peter Capaldi")
print(doctors)
# doctors.remove("Jenna Coleman") # bu satır çalıştırıldığında KeyError alınır.

print()

# discard metodu da remove metoduna benzer şekilde çalışır fakat discard metodu, sette olmayan elemanlar
# için hata vermez.
doctors = { "Matt Smith", "David Tennant", "Peter Capaldi", "Jodie Whittaker" }
print(doctors)
doctors.discard("Peter Capaldi")
print(doctors)
doctors.discard("Jenna Coleman") # discard metodunu kullandığımız için bu satır hata vermez set değişmez
print(doctors)

print()

# ---- Karşılaştırma Metodları ---- #
# setlere uygulanan metodlar çoğunlukla matematiksel kümelerdeki kıyaslamalara benzer görevleri yaparlar.
# setleri matematiksel olarak kümelere benzetebiliriz, prensipte her ikisinde de eleman tekrarı olmaz ve
# sırasız objelerdir.
# -- Kesişim (intersection): intersection metodu, bir set üzerinde çalışır ve argüman olarak bir iterable
# obje alır, çıktı olarak ise yeni bir set verir (mevcut seti değiştirmez).
ev_yemekleri = {"Pırasa", "Taze Fasülye", "Enginar"}
favori_yemekler = {"Taze Fasülye", "Kuru Fasülye", "Köz Patlıcan"}
print(ev_yemekleri.intersection(favori_yemekler)) # veya
print(favori_yemekler.intersection(ev_yemekleri)) # bu da aynı sonucu verir.
# intersection metodu yerine "&" operatörü de kullanılabilir:
print(ev_yemekleri & favori_yemekler) # veya
print(favori_yemekler & ev_yemekleri)

print()

# bir örnek de sayılardan yapalım:
sayılar = {3.0, 2.0, 1, 4}
başka_sayılar = {3, 2, 1, 5, 7}
print(sayılar & başka_sayılar) # dikkat edilecek bir nokta çıktıda 2 ve 3ün float tipinde olduğudur. float
# ve integer aynı sayıyı belirttiğinde python daha karışık olan objeyi yani floatı esas alır.

print()

# -- Bileşim (union): tıpkı iki kümenin bileşimini alır gibi union metodu, setlerdeki elemanların tümünü 
# tekrar olmaksızın içeren 3. bir set verir. çalışma şekli intersection metoduyla aynıdır.
print(ev_yemekleri.union(favori_yemekler)) # veya
print(favori_yemekler.union(ev_yemekleri))
# union metodu yerine "|" operatörü de kullanılabilir:
print(ev_yemekleri | favori_yemekler) # veya
print(favori_yemekler | ev_yemekleri)

print()

# -- Tüm Farklar (symmetric difference): symmetric_difference metodu, iki sette birbirlerinden farklı tüm
# elemanlardan yeni bir set oluşturur. yani ortak olan elemanlar hariç tüm elemanları yeni bir sete yer-
# leştirir. çalışma şekli diğer iki metodla aynıdır:
print(ev_yemekleri.symmetric_difference(favori_yemekler)) # veya
print(favori_yemekler.symmetric_difference(ev_yemekleri))
# kısa yol olarak "^" operatörü kullanılabilir:
print(ev_yemekleri ^ favori_yemekler) # veya
print(favori_yemekler ^ ev_yemekleri)

print()

# -- Fark (difference): difference metodu, çalıştırıldığı sette, argüman olarak verilen sette olmayan ele-
# manlardan yani farklı elemanlardan yeni bir set oluşturur. diğer metodların aksine metodun hangi set ü-
# zerinde çalıştırıldığı önem arzeder.
print(ev_yemekleri.difference(favori_yemekler)) # çıktısı ile,
print(favori_yemekler.difference(ev_yemekleri)) # çıktısı aynı değildir.
# kısa yol olarak "-" operatörü kullanılır. yine hangi setin önce verildiği, çıktı için önemlidir.
print(ev_yemekleri - favori_yemekler) # çıktısı ile,
print(favori_yemekler - ev_yemekleri) # çıktısı aynı olmaz.

print()

# ---- Diğer Metodlar ---- #
# issubset ve issuperset, iki setin birbirlerinin alt veya üst kümesi olup olmadığını kontrol eder ve bir
# boolean çıktısı verir.
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
# a.issubset(b) çalıştırıldığında, eğer a setindeki tüm elemanlar, b setinde de bulunuyorsa çıktı olarak
# True alınır. aksi takdirde çıktı olarak False alınır.
print(a.issubset(b))
# subset kontrolü için "<=" operatörü de kullanılabilir:
print(a <= b)
# eğer eşitlik durumu kontrol edilmek istenmiyorsa "<" operatörü kullanılır:
print(a < b)
# tersini kontrol ettiğimizde false çıktısı alırız:
print(b.issubset(a))
print(b <= a)

print()

# b.issuperset(a) çalıştırıldığında ise eğer b'deki tüm elemanlar a'da da bulunuyorsa True, aksi takdirde
# False alınır.
print(b.issuperset(a))
# superset kontrolü için ">=" operatörü de kullanılabilir:
print(b >= a)
# eğer eşitlik durumu kontrol edilmek istenmiyorsa "<" operatörü kullanılır:
print(b > a)
# tersini kontrol ettiğimizde false çıktısı alırız:
print(a.issuperset(b))
print(a >= b)

print()

# birbirleriyle aynı elemanları içeren setler her iki metodla da birbirleriyle True çıktısı verir.
a = {1, 2, 3}
b = {1, 2, 3}
print(a.issubset(b))
print(b.issubset(a))
print(a.issuperset(b))
print(b.issuperset(a))

print()

# ---- Frozen Set ---- #
# frozenset basitçe değişmez (immutable) bir settir ve setten farklı bir obje türüdür. tıpkı liste-tuple
# ilişkisinde olduğu gibi bazı durumlarda (mesela sözlüklerde key olarak kullanmamız gerektiğinde) eli-
# mizdeki setin değişmez olmasını isteriz. bu durumda söz konusu seti veya set fonksiyonunda olduğu gibi
# herhangi bir iterable objeyi frozenset() fonksiyonundan geçirerek çıktı olarak değişmez bir set elde
# edebiliriz.
çok_soğuk = frozenset([1, 2, 3, 2, 1]) # setlerde olduğu gibi frozensetlerde de tekrar eden elemanlar
# dikkate alınmaz.
print(çok_soğuk)
print(type(çok_soğuk))
# frozensetler normal setlerin tüm özelliklerini taşır. itere edilebilirler, setlerle çalıştırılan me-
# todları çalıştırabilirler; fakat değiştirilemezler:
for eleman in çok_soğuk:
    print(eleman)
b = {1, 2}
print(çok_soğuk & b) # frozensetlerle yapılan karşılaştırma operasyonlarının veya metodlarının çıktıları
# da frozenset objelerdir.
print(çok_soğuk.symmetric_difference(b))
print(b.symmetric_difference(çok_soğuk)) # burada çıktı normal bir settir çünkü metod, bir set üzerinde
# çalıştırılmıştır, frozenset metodda argüman olarak kullanılır.
print(b.issubset(çok_soğuk))
print(çok_soğuk.issuperset(b))