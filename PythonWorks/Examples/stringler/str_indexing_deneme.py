# stringlerden istenilen sıradaki bir karakterin çekilip yeni bir string olarak alın-
# ması işlemine "string indexing" denir ve "[]" içersine, alınmak istenen karakterin
# index numarası yazılarak yapılır. index numarasıyla ilgili önemli nokta index nu-
# marası sayılırken python'un 0'dan başladığıdır. length gibi diğer fonksiyonlar st-
# ringlerle ilgilenirken ilk karakteri 1. karakter olarak alırlar fakat indexing iş-
# leminde ilk karakterin indeksi 0'dır.
kelime = "bilgisayar"
# bu kelimenin ilk harfini (unutma harf olmak zorunda değil bu bir string, bahsedilen
# de bir karakter.) çekmek için karşılık gelen değişken ile [0] şeklinde çekebiliriz.
print(kelime[0])
print(kelime[1]) # ikinci karakteri çekmek için de 1 numaralı indeksi çağırırız.
# indeks olarak negatif sayılar da kullanılabilir. bu durumda karakter, stringin sonun-
# dan çekilir. negatif indeksing'de ilk karakter (yani stringin sonuncu karakteri)
# -1 numaralı indekstir.
print(kelime[-1])
print(kelime[-4])
# stringi bir değişkene atamadan da indeks işlemlerini gerçekleştirebiliriz
print("bu bir stringdir."[5])
# veya aşağıda anlatılan string slicing de yapılabilir.
print("bu bir stringdir."[3:8])

# indeks braketi ([]) içersine stringin uzunluğundan daha uzun bir sayı yazıldığında
# IndexError alınır. indeks kullanılarak stringin bir karakteri değiştirilmeye çalı-
# şıldığında (kelime[a] = "x") ise TypeError hatası verir çünkü stringler, int'ler,
# float'lar, boolean'lar gibi veri türleri immutable yani değiştirilemez türlerdir.
# bunlarla yapılan manüplasyonlar sonucu obje değişmez, aynı türden veya farklı tür-
# den yeni bir obje oluşturulur.

# indeks kullanarak stringi kesmek ve yeni bir string oluşturmak mümkündür. bunun için
# [] içersine iki indeks numarası girmemiz gerekir. indeks numaralarından ilki başlan-
# gıç ikincisi ise bitiş olarak okunacaktır. başlangıç ve bitiş indeksleri ":" ile
# birbirinden ayrılır. oluşturulan yeni stringe başlangıç indeksi dahilken bitiş in-
# deksi dahil değildir. değişken[başlangıç:bitiş] -> "başlangıç....bitiş-1"
ornek = "çekoslovakyalılaştıramadıklarımızdan mısınız?"
print(ornek[0:10]) # 0. indeksten başlayarak 10. indekse kadar yeni bir string oluş-
# turmuş olduk. yani son karakter, 9. indeks.
# negatif ve pozitif indeks farketmeksizin kullanabiliriz. başlangıç indeksinin bitiş
# indeksinden önce gelmesi yeterli aksi halde bir string oluşmayacaktır (hata açığa
# çıkmaz).
print(ornek[12:30])
print(ornek[-33:-15])
print(ornek[12:-15])
print(ornek[-33:30])
# görülebileceği gibi 4 çıktı da birbirinin aynısıdır.
# beklendiği gibi bitiş değeri stringin karakter sayısından daha fazla olduğunda hata
# oluşmaz. python bunu, slicingi son indeksle bitirmek istediğimiz yönünde yorumlar ve
# yeni stringin son karakteri ilk stringin son karakteri olur.
print(ornek[30:200])
# ilk indeksi girmediğimizde python bunu 0. indeksten başlamak istediğimiz yönünde yo-
# rumlar ve kesmeye stringin ilk karakterinden başlar.
print(ornek[:35])
# aynı şekilde bitiş indeksi girmediğimizde de pyhton bunu giriş indeksinden son indek-
# se kadar kesmek istediğimiz yönünde yorumlar.
print(ornek[23:])
# hem başlangıç hem de bitiş indeksi yazılmadığında, aynı stringi kopyalayıp başka bir
# string oluşturmuş olur. bu da bazı durumlarda yararlıdır.
print(ornek[:]) # burada yazdırılan "ornek" değişkeniyle aynı karakterleri aynı sıra
# ile içeren başka bir stringdir, ornek stringi değildir.

# string slicing default olarak stringi birer karakter aralıkla tarar. bunu değiştir-
# mek için [] arasına bir ":" ekleyerek kaç karakter aralıkla taramak istediğimizi ya-
# zabiliriz.
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
print(alfabe[7:26]) # bu şekilde birer indeks ekleyerek 0. indeksten 14. indekse kadar
# stringi kesebiliriz.
print(alfabe[7:26:2]) # bu şekilde yazdığımızda ise kesilecek indeks karakterleri iki-
# şer eklenerek alınır yani 7. 9. 11. 13. ... şeklinde çıkar.
# yine bu kullanımda da ilk karakter için veya son karakter için indeks yazmamıza ge-
# rek yoktur yani şu 4 satır aynı çıktıyı verir.
print(alfabe[0:29:3])
print(alfabe[:29:3])
print(alfabe[0::3])
print(alfabe[::3])
# indeksler negatif yazılabilir.
print(alfabe[-20:-8:4])
# interval negatif de olabilir. bu durumda string tersten yazılır. bu durumda ilk in-
# deks başa son indeks ise sonra yazılır. mesela 5. indeksten 10. indekse 2 intervalle
# tersten düzenlenmiş bir string için [20:5:-2] yazılır.
print(alfabe[20:5:-2])
# bütün stringi terse çevirmek için ilk indeksten son indekse kadar -1 intervalle string
# elde edilmelidir:
print(alfabe[::-1])

# örneğin tersten istiklal marşı yazmak için
istiklal_marsi = """Korkma, sönmez bu şafaklarda yüzen al sancak;
Sönmeden yurdumun üstünde tüten en son ocak.
O benim milletimin yıldızıdır, parlayacak;
O benimdir, o benim milletimindir ancak.
Çatma, kurban olayım, çehreni ey nazlı hilal!
Kahraman ırkıma bir gül! Ne bu şiddet, bu celal?
Sana olmaz dökülen kanlarımız sonra helal
Hakkıdır, hakk'a tapan, milletimin istiklal!"""
print(istiklal_marsi[::-1])