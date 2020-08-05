# count metodu adından da anlaşılabileceği gibi listede bir elemanın kaç kez göründüğünü çıktı olarak verir ve
# herhangi bir şekilde listeyi değiştirmez. tek bir argüman kabul eder o da listede sayılan elemandır.
envanter = ["Mouse", "Klavye", "Mouse", "RTX Anakart", "Kulaklık", "Kulaklık", "Mouse"]
print(envanter.count("Mouse"))
# büyük küçük harf duyarlılığı akılda bulundurulmalıdır.
print(envanter.count("Kulaklık"))
print(envanter.count("kulaklık"))
# listede mevcut olmayan bir eleman count metoduyla çağırıldığında hata alınmaz, basitçe 0 çıkar.
# diğer veri tipleriyle de count metodu kullanılır.
haftalık_uyku_saatleri = [7.5, 6.2, 7.5, 8.0, 5.3, 8.0]
print(haftalık_uyku_saatleri.count(7.5))
# python int ve floatlar arasında bağlantı kurabilmektedir.
print(haftalık_uyku_saatleri.count(8.0))
print(haftalık_uyku_saatleri.count(8))

print()

# index metodunun çalışma şekli ve syntaxı stringlerdekiyle aynıdır. aranan elemanın ilk defa görüldüğü in-
# deks pozisyonunu çıktı olarak verir. iki argüman kabul eder: aranan eleman ve başlangıç indeksi. başlangıç
# indeksi dahildir ve default olarak sıfırdır.. indeks metodu, listede olmayan bir eleman verildiğinde 
# ValueError verir.
print(envanter.index("Klavye"))
# büyük küçük harf duyarlı
# print(envanter.index("klavye")) # yorum kaldırıldığında bu satırdan hata alınır.
print(envanter.index("Mouse")) # ilk görüldüğü indeksi verir.
print(envanter.index("Mouse", 1)) # aramaya 1. indeksten başlar, önce 2. indekstekini bulur.

print()

# copy metodu basitçe listenin bir kopyasını verir. fakat yalnızca basit veri tiplerinden (string, float, in-
# teger, boolean) oluşan verilerde başarılı çalışmaktadır; başka listelerden oluşan listeleri veya daha kar-
# maşık veri yapılarından oluşan listeleri kopyalamakta çok başarılı değildir. argüman kabul etmez. oluşan
# yeni liste diğerinden tamamen bağımsızdır; eski liste değiştirildiğinde, oluşturulan ve başka bir degis-
# kene atanan kopya etkilenmez.
units = ["meter", "kilogram", "second", "ampere", "kelvin", "candela", "mole"]
more_units = units.copy()
print(units)
print(more_units)
units.remove("kelvin")
print(units)
print(more_units)
even_more_units = units[:] # aslında daha kısa bir syntaxla aynı iş yapılabilir. bu şekilde de oluşan yeni
print(even_more_units) # liste orjinalinden bağımsızdır.
units.remove("candela")
print(even_more_units)

print()

# split metodu esasında listeler ile çalıştırılmaz fakat output olarak bir liste verir. split metodu bir
# substring ve isteğe bağlı bir int kabul eder ve stringi bu substringin olduğu yerlerden ayırır. eğer mak-
# simun split sayısı da verilirse stringi bu sayıda substringlere böler. bölünen tüm substringler bir lis-
# te halinde metoddan çıkar.
kullanıcılar = "Egemen, Gökhan, Oğuz, Beko, Sefa, Taha, Salim"
print(kullanıcılar)
print(kullanıcılar.split(", ")) # bütün stringi ", " substringlerinden kesiyoruz.
print(kullanıcılar.split(", ", 2)) # bu sefer stringi iki kere kesiyoruz. böylece 3 tane substring oluşacak
# ilk iki substring, birer isim içerirken 3. substring, ", " ile ayrılmış 5 isim içerir.
# eğer ayırıcı olarak bir boş string ("") konulursa beklendiği gibi harf harf ayrım gerçekleşmez, ValueError
# alınır.

print()

# join metodu ise split metodunun tamamlayıcısıdır. bir string üzerinde çalışır ve argüman olarak bir liste
# kabul eder. çıktı olarak listenin elemanlarının söz konusu stringle birleştirildiği bir string verir.
adres = ["Emniyet Mah", "Dögol Cad", "Ankara Ünv", "Eczacılık Fak", "No:4", "06560", "Yenimahalle/Ankara"]
# syntaxı şu şekildedir: ayırıcı_string.join(liste)
print(", ".join(adres))
# splitin aksine join metodunda "" stringi geçerlidir ve listenin elemanları boşluksuz birleştirir.
print("".join(adres))