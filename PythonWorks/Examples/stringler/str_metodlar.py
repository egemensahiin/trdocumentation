# metodlar, fonksiyonlara benzer şekilde çelışırlar fakat çalışma şekilleri ve amaçları
# daha farklıdır. metodlar, obje.metod(parametre) şeklinde çalıştırılırlar.
# find metodu stringler üzerine uygulanır ve string içersinde başka bir stringin var-
# lığıyla ilgili bilgi verir fakat in ve not in operatörlerinin aksine bu bilgi bir
# boolean objesi değil bir tamsayıdır ve aranan stringin başlangıcının indeks numara-
# sını verir.
degisken = "Bu örnek bir String'dir."
print(degisken.find("b"))
# find metodu aranan obje, string içersinde bulunmadığında çıktı olarak -1 verir
print(degisken.find("z"))
# ayrıca find metodu büyük-küçük harf duyarlıdır.
print(degisken.find("S")) # 13 çıktısını verirken;
print(degisken.find("s")) # -1 çıktısını verir.
# aranan stringden birden fazla olması durumunda find metodu indeks numarası en küçük
# sonucu verecektir.
print(degisken.find("r")) # indeks numarası en küçük olan 4. indekstekidir.
# diğerlerini bulmak için aranan string genişletilebilir.
print(degisken.find("ri"))
# veya find metodunun başka bir özelliği kullanılarak aramaya başlama noktası seçilebi-
# lir. find("aranan", başno) şeklinde başlangıç numarası atanır. bu durumda find metodu
# aramaya bu indeks numarasından başlar.
print(degisken.find("r", 4)) # başlangıç indeksi aramaya dahildir.
print(degisken.find("r", 5))

print()

# indeks metodu da find metoduyla aynı işi yapar. farklı olarak indeks metodunda aranan
# string bulunamadığında çıktı olarak -1 alınmaz. bunun yerine program ValueError ve-
# rir. hangi metodun kullanacağı, aranan stringin varlığı sonucu ne olmasının istendi-
# ğine bağlı olarak seçilmelidir. sonuç, programın tüm mantığını etkileyecek ve yanlış
# çalışmasına sebep olacaksa programı durdurmak için index metodu seçilebilir. progra-
# mın çalışmayı sürdürmesi isteniyorsa find metodu seçilmelidir.
print(degisken.index("b"))
print(degisken.find("z")) # bu satır çıktı olarak -1 verirken:
#print(degisken.index("z")) # yorum kaldırıldığında bu satırda ValueError oluşur.

print()

# rfind metodu da find metoduna benzer şekilde çalışır fakat aynı substringden birden
# fazla olduğunda find metodunun aksine indeks numarası en küçük olanın değil en büyük
# olanın indeks numarasını çıktı olarak verir. rfind, reverse find'ın kısaltması olup
# substringi tersten tarar.
print(degisken.find("r")) # daha önce de gördüğümüz gibi 4 olarak çıkarken;
print(degisken.rfind("r")) # 22 olarak çıkar.
# rfind metodu da yine bulunamayan substringler için -1 çıktısını verir
print(degisken.rfind("z"))

print()

# adından da anlaşılabileceği gibi bu metodlar stringin, aranan substring ile başlayıp
# başlamadığını veya bitip bitmediğini kontrol eder ve bir boolean objesi olarak çıktı
# verirler. büyük küçük harf duyarlıdırlar.
ornek = "En sevdiğim ders Farmasötik Kimya"
print(ornek.startswith("E"))
print(ornek.startswith("En"))
print(ornek.startswith("en"))
print(ornek.startswith("En sev"))
print(ornek.startswith("Alakasız bir şey"))

print()

print(ornek.endswith("a"))
print(ornek.endswith("ya"))
print(ornek.endswith("Kimya"))
print(ornek.endswith("kimya"))
# diğer metodlarda olduğu gibi str.endswith("substr", başno, bitno) şemasıyla aramayı
# belli indeks numaralarıyla kısıtlamak mümkündür.

print()

# count metodu, aranan substringin string içersinde kaç defa tekrarlandığını int olarak
# verir.
tekerleme = "şemsi paşa pasajında sesi büzüşesiceler"
print(tekerleme.count("p"))
print(tekerleme.count("pa"))
# yine count metodu da büyük küçük harf duyarlıdır.
print(tekerleme.count("s"))
print(tekerleme.count("S"))
# birbirinden ayrı duran iki substringin sayısı basitçe count çıktıları toplanarak bu-
# lunabilir.
print(tekerleme.count("p") + tekerleme.count("s"))

print()

# string içersindeki büyük-küçük harflerin değiştirilip yeni bir string elde edilmesi
# için kullanılan 5 metod vardır:
str = "bu örnek bir stringdir."
# capitalize metodu, stringin ilk karakterini büyük harf yapar.
print(str.capitalize())
# title ise stringdeki tüm kelimelerin baş harflerini büyük harf yapar.
print(str.title())
# upper metodu stringdeki tüm küçük harfleri büyük harf yapar.
print(str.upper())
# lower metodu ise stringdeki tüm büyük harfleri küçük harf yapar.
print("LINUS TORVALDS".lower())
# swapcase metodu büyük harfleri küçük, küçük harfleri büyük yapar.
print("aBcÇdEf".swapcase())
# metodların peşpeşe kullanılması da mümkündür. LINUS TORVALDS stringini başharfleri bü-
# yük olacak şekilde elde etmek içinönce lower, ardından title metodları kullanılır.
print("LINUS TORVALDS".lower().title())

print()

# boolean metodları, stringin karakteriyle ilgili boolean türünde çıktılar verir.
# islower metodu, stringdeki bütün alfabetik karakterler küçük olduğunda "True" olur.
print("küçük harfler".islower())
print("küçük harfler 123'^+".islower()) # sadece alfabetik karakterleri okur.
print("Küçük Harfler".islower()) # herhangi biri büyük olduğunda "False" olur.

# isupper metodu da aynı şekilde alfabetik karakterlerin hepsi büyükken "True" olur.
print("BÜYÜK HARFLER".isupper())
print("BÜYÜK HARFLER 123+*-".isupper()) # yine isupper da sadece alfabetik karakter okur.
print("BÜYÜK HARFLEr".isupper()) # herhangi bir karakter küçükken "False" olur.

# istitle metodu, stringdeki büyük-küçük karakterler title formatında (her kelimenin baş
# harfi büyük) olduğunda "True" olur.
print("Title Formatı".istitle())
print("Title formatı".istitle()) # kelimelerden herhangi biri küçük harfle başlarsa "Fal-
# se" olur.
print("Title Formatı 123".istitle()) # yine sadece alfabetik karakterler okunur.

# isalpha metodu, stringdeki karakterlerin hepsinin alfabetik olup olmadığına bakar. hep-
# si alfabetik olduğunda "True" çıktısını verir.
print("Alfabetik".isalpha())
print("Aldabetik123".isalpha()) # alfabetik olmayan bir karakter varsa "False" olur.
print("Alfabetik karakterler".isalpha()) # boşluk, alfabetik değildir!!

# isnumeric metodu ise aynı şekilde tüm karakterlerin numerik olup olmadığını kontrol
# eder.
print("08031995".isnumeric())
print("08031995%&".isnumeric()) # semboller numerik karakter değildir.
print("08031995 ".isnumeric()) # boşluk da numerik değildir.

# isalnum metodu ise numerik ve alfabetik karakterlerden oluşan stringlerde "True"dur
print("esahin95".isalnum())
print("esahin".isalnum()) # yalnız alfabetik veya
print("95".isalnum()) # yalnız numerik karakterlerden oluşan str'ler de "True"'dur.

# isspace metodu yalnızca space'ten oluşan str'lerde "True"'dur
print(" ".isspace())
print("   ".isspace())
print(" g ".isspace())
print("".isspace()) # space bir karakterdir. hiç karakter içermeyen bir string, isspace
# metodu ile "False" olur.

print()

# strip metodları, stringi keser. default olarak boşlukları keserler fakar içersine bir
# string tanımlandığında bunla ilgli karakterleri de keserler.
str2 = "            ornek           "
print(str2)
print(len(str2))
# 28 karakterli bu stringin sağında ve solunda pek çok boşluk var. bunları kesmek için
# strip metodları kullanılır.
print(str2.rstrip()) # rstrip metodu, stringin sağındaki boşlukları keser.
print(len(str2.rstrip()))
print(str2.lstrip()) # lstrip metodu, soldaki boşlukları keser.
print(len(str2.lstrip()))
print(str2.strip()) # regular strip metodu ise stringi her iki taraftan okur ve keser.
print(len(str2.strip()))
# belli bir substring kesmek için metod parametresi olarak istenen string tanımlanır.
# fakat tanımlanan substringin ancak sağ veya sol uçta mevcut olduğu sürece kesileceği
# ve metodların büyük küçük harf duyarlı olduğu unutulmamalıdır.
site = "www.bombabomba.com"
print(site.lstrip("w"))
print(site.lstrip("w.")) # diğer metodların aksine strip metodları tanımlanan substring-
# teki herhangi bir karakteri veya sekansı arar yani w yazdığımızda baştaki 3 w karakteri
# de kesilir. w. nokta yazdığımızda önce w karakterlerini sonra da . karakterini keser.
print(site.lstrip(".w")) # .w yazdığımızda da aynı sonucu alırız.

print(site.rstrip("m"))
print(site.rstrip("com"))
print(site.rstrip("moc"))
print(site.rstrip(".commm"))

print(site.strip("womc.")) # strip metoduyla birlikte silinmek istenen karakterler, sek-
# anslar istenen sırayla yazılabilir. başta veya sonra bunlar varsa kesilecektir.
print(site.strip("ba")) # stringin ortasından bir substr girdiğimizde, buraya kadar olan
# (baştan veya sondan) bütün karakterleri yazmadığımız müddetçe bu string kesilmez.

print()

# replace metodu basitçe aranan bir substringi, başka bir substringle değiştirir. formatı
# "string".replace("substr1", "substr2") şeklindedir. burada substr1, stringde aranan
# substringdir. substr2 ise yerine konmak istenen substringdir.
tekerleme2 = "dal kalkar kartal sarkar kartal sarkar dal kalkar"
print(tekerleme2)
print(tekerleme2.replace("a", "e")) # stringdeki bütün karakterler değişir. unutma!!
print(tekerleme2.replace("d", "daaaaa")) # substr'ler aynı uzunlukta olmak zorunda değil
print(tekerleme2.replace("ka", ""))
print(tekerleme2.replace("ke", "")) # aranan string yoksa hata alınmaz.

# metodların birlikte kullanımına örnek. metodların sırası önemlidir.
agugugu = "          aksd akjs          "
b = agugugu.strip().replace(" ", "!")
print(b)
# önce strip çalışır, sonra replace
c = agugugu.replace(" ", "!").strip()
# burada ise önce replace çalışır.
print(c)

help('FORMATTING')