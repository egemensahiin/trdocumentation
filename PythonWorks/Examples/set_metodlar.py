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

# -- Eleman Çıkarılması: 