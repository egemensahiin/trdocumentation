import copy
# listeler mutable yani değiştirilebilir objelerdir. bu değiştirilebilirlik, objelerin değişkenlere atanma-
# sında önem kazanmaktadır. immutable bir objeyi mesela bir sayıyı değişkene atayalım:
a = 5
# başka bir değişkeni bu a değişkeni ile tanımladığımızda olan şey, esasında değişkenin tanımladığı objenin
# yeni değişkene atanmasıdır. yani:
b = a # şeklinde atadığımızda, b değişkenine a değişkeni değil, a'nın karşılık geldiği obje olan 5 sayısı
# atanmıştır. yani a ile b birbirine bağlı değildir. bu durumda a değişkenine farklı bir değer atadığımızda
# b değişkeninin değeri değişmez:
a = 3
print(a)
print(b)
# fakat listeler kendileri değişebilen objeler olduğundan birden fazla değişkenle uygulanan kullanımlarda
# dikkatli olunmalıdır.
a = [1, 2, 3]
b = a # burada olan şey, yukarıda olanla aynıdır. a değişkeni söz konusu listeyi refere eder. b değişkeni
# de a'yı değil, yine aynı listeyi refere eder. fakat dediğimiz gibi listeler değiştirilenilir objelerdir.
# yani a'yı, bir metod kullanarak değiştirdiğimizde, aslında a'nın refere ettiği listeyi değiştirmiş olu-
# ruz:
a.append(4)
print(a) # artık elimizdeki liste değişmiştir, a değişkeni değil. bu listeye aynı zamanda b değişkeni de
# referans gösterildiği için a ve b değişkenleri artık [1, 2, 3, 4] listesini refere ederler.
print(b) # aynı durumun tersi de mümkündür. elimizdeki listeyi b değişkeniyle referans edip değiştirebili-
# riz:
b.append(5)
print(a)
print(b)

# python mutable ve immutable objeleri aynı şekilde işlemez. mutable objeler, program içersinde değişe-
# bildiği için birbirine eşit iki mutable obje tanımlasak dahi python bunları iki farklı obje olarak ha-
# zada tutat. öte yandan değişmez objelerde böyle bir önleme gereksinim olmadığı için birbirine eşit bir
# objeden ne kadar tanımlanırsa tanımlansın hafızada tek bir yerde tutulur ve birbirlerine sadece eşit
# değil aynı zamanda da aynıdırlar. bunu kontrol etmek için is keywordü kullanılır:
sayılar = [1, 2, 3]
rakamlar = sayılar 
# eşitliklerini kontrol etmek için == kullanılır:
print(rakamlar == sayılar) # True
# aynı olup olmadıklarını kontrol etmek içinse is keywordu kullanılır:
print(rakamlar is sayılar) # True
# bu iki değişken aynı listeyi refere ederler dolayısıyla is keywordu ile True çıktısı alınır ve aynıdırlar.
aynı_sayılar = [1, 2, 3] # bu liste ise diğerlerine eşit olmakla beraber aynı listeyi refere etmez. birbirine
# eşit fakat farklı listelerdir:
print(aynı_sayılar == sayılar) # True
print(aynı_sayılar is sayılar) # False
# bahsettiğimiz gibi değişmez objeler için hafızada yeni bir birim oluşturmaya gerek görülmez çünkü zaten
# söz konusu objeler değişemeyeceği için birbirlerine eşit iken aynı olmalarının da bir sakıncası yoktur:
a = 3
b = a
print(a == b) # True
print(a is b) # True
# bu sebeple başka bir değişkeni de 3'e refere ettiğimizde, bu üç değişken birbirleriyle eşit olduğu gibi
# aynı zamanda da aynı olacaktır:
c = 3
print(c == a) # True
print(c is a) # True

# listeler bazen değiştirilmeden başka bir değişkene kopyalanmak istenebilir. bunun için iki context söz
# konusudur. bunlardan biri shallow (yüzeysel) kopyalama diğeri ise deep (derin) kopyalamadır.
a = [1, 2, 3]
# yüzeysel kopyalamada geçerli bir kaç syntax vardır. bunlardan ilki slicing metodudur:
b = a[:] # bu şekilde a'nın bir kopyasını b'ye atamış oluruz. a ve b eşittir fakat aynı değildir. progra-
# mın ilerleyen kısımlarında a'yı manüple etsek dahi bir yedeği b değişkeninde mevcuttur. 
print(a == b) # True
print(a is b) # False
# bir diğer syntax da copy metodudur:
b = a.copy()
print(a == b) # True
print(a is b) # False
# copy metoduna benzer şekilde copy fonksiyonuyla da aynı şeyi yapabiliriz. fakat bunun için önce copy mo-
# dülünü import etmemiz gerekir (bkz. line 1)
b = copy.copy(a)
print(a == b) # True
print(a is b) # False
# a listesini değiştirdiğimizde b listesi değişmez:
a.append(4)
print(a)
print(b)

# tek katmanlı listelerde her üç yöntem de etkindir. fakat işin içine iç içe listeler girdiğinde aynı şeyi
# söyleyemeyiz. üç yöntemde de listenin elemanları, yeni bir değişkene tekrar refere edilir. yani ilk liste
# içersinde eleman olarak başka bir liste varsa, bu liste olduğu gibi refere edilir, her iki değişken içinde
# de eşit olmanın yanı sıra aynıdır ve manüple edildiğinde kopya da etkilenir:
arası = [2, 3, 4]
baş_son = [1, arası, 5]
yedek = baş_son[:]
print(baş_son == yedek) # True
print(baş_son is yedek) # False
# görüldüğü gibi iki liste eşit ve farklıdır. fakat listelerin ilk indekslerini kıyaslarsak:
print(baş_son[1] == yedek[1]) # True
print(baş_son[1] is yedek[1]) # True
# hem eşit hem de aynı olduklarını görürüz. bu sebeple baş_son'un 1. indeksini manuple ettiğimzde, yedeğin
# de 1. indeksi manuple edilmiş olur.
baş_son[1].append(6)
print(baş_son)
print(yedek)
# bunun için deep copy fonksiyonu kullanılır ve bu da copy fonksiyonu gibi copy modülünde tanımlıdır:
arası = [2, 3, 4]
baş_son = [1, arası, 5]
yedek = copy.deepcopy(baş_son)
# deep copy fonksiyonu, değişebilen bir objeyi recursif yani tekrarlı olarak kopyalar.
print(baş_son == yedek) # True
print(baş_son is yedek) # False
# ilk indeksler de tıpkı baş_son ve yedek gibi eşit fakat farklıdır:
print(baş_son[1] == yedek[1]) # True
print(baş_son[1] is yedek[1]) # False
# iki obje birbirinin değişimlerinden de etkilenmez:
baş_son[1].append(6)
print(baş_son)
print(yedek)

print()

#-----------------------------------------------------------------------------------------------------------
# LİSTLERDE ELEMENT DEĞİŞTİRME

# tanımda da bahsettiğimiz gibi listeler mutable objelerdir yani değiştirilebilirler
almira_tayfa = ["Egemen", "Gökhan", "Oğuz", "Yavuz"]
print(almira_tayfa)
# şimdi bu objede bir elemanı başka bir stringle değiştirelim. bunun için uyguladığımız syntax şu şekildedir:
# list[indeks] = yeni obje
# mesela almiraya gelmeyi bırakan yavuzun yerine üzülerek mertcanı koyalım:
almira_tayfa[3] = "Mertcan"
print(almira_tayfa)
# şunu unutmamak gerekir; bu oluşan yeni bir obje değildir, almira_tayfa değişkeni hala aynı objeyi tanımla-
# maktadır ama bu obje değiştirilmiştir. bunu syntax'tan anlayabiliriz. imutable objelerde manüplasyon için
# değişkenin karşılık geldiği objeyi değiştiriyoruz. fakat burada listeyi değil liste içinde bir elemanı de-
# ğiştiriyoruz yani listeyi değişirmeden manüple ediyoruz. mesela "String" stringinin ilk karakterini değiş-
# tirmek için "String"[0] = "X" şeklinde bir syntax kullanamayız, kullanırsak TypeError alırız.
# negatif bir indeks değeri ile de listeyi manüple edebiliriz.
almira_tayfa[-2] = "Berkcan"
print(almira_tayfa)
# bu syntaxı listeye eleman eklemek için uygulayamayız. mesela almira_tayfa[4] = "Sefa" şeklinde 4. indekse
# Sefayı atamaya çalışırsak IndexError alırız çünkü Sefa bizi oyalayıp almiraya gelmeyecektir.
# bu syntax int veya float tipinde objelerle de uygulanabilir.
almira_tayfa[-1] = 5
print(almira_tayfa)

print()

# ekleme yapmak için tek bir indeks numarası seçmek zorunda değiliz. list slicing metoduyla aldığımız liste-
# nin bir parçasını başka bir listeyle değiştirebiliriz. yalnız dikkat; burada "=" in sağına herhangi bir ob-
# je değil yeni bir liste yazmalıyız. yeni liste, kesilen listeyle aynı uzunlukta olmak zorunda değil. daha
# kısa veya uzun da olabilir.
liste = ["Bu", "bir", "liste", "ve", "şimdi", "biz", "bunu", "değiştireceğiz."]
print(liste)
print(len(liste))
# syntax şu şekilde; liste[ilk ind:son ind] = [yeni liste] son indeks yine dahil değil. ayrıca indeks numa-
# raları negatif de verilebilir.
liste[1:3] = ["öylesine", "bir şeyler"]
print(liste)
print(len(liste))
liste[-3:-2] = ["daha", "uzun", "liste"]
print(liste)
print(len(liste))
liste[2:] = ["daha kısa", "liste"]
print(liste)
print(len(liste))

print()

# LİSTELERE ELEMAN EKLENMESİ

# listelere eleman eklemek için kullanılabilecek yöntemlerden biri "append" metodudur. normal metod syntaxı
# ile (obje.metod() şeklinde) kullanılır ve argüman olarak bir eleman kabul eder (string, integer, başka bir
# list vs.). append metodu uygulandığında listenin sonuna, argüman olarak verilen elemanı ekler. fakat dik-
# kat; stringlerdeki metodlarda olduğu gibi yeni bir list oluşmaz, hali hazırda var olan list değişmiş olur.
# bu sebeple list = list.appent(eleman) gibi bir syntax gereksizdir ve yanlış sonuç verir; metodlar obje ti-
# pi olarak None olduğu için böyle bir syntaxın sonucu list = None olur. append metodu yalnız bir tane obje
# kabul eder. aynı anda listeye iki obje eklemez. yeni obje sadece liste sonuna eklenir.

nordic_ülkeler = ["Norveç", "İsveç", "Danimarka", "Finlandiya"]
print(nordic_ülkeler)
print(len(nordic_ülkeler))
# şimdi append metoduyla bu listeye İzlandayı da ekleyelim
nordic_ülkeler.append("İzlanda")
print(nordic_ülkeler) # nordic_ülkeler listesi artık izlandayı da içeren 5 elemanlı bir objedir.
print(len(nordic_ülkeler))
# nordic_ulkeler listedinde bir daha append metodu uyguladığımızda 6 elemanlı bir liste oluşur:
nordic_ülkeler.append("Rusya")
print(nordic_ülkeler)
print(len(nordic_ülkeler))

# ufak bir örnek; bir stringdeki tüm elemanlarla liste oluşturan bir fonksiyon yazalım
def ornek_fonks(orn):
    ls = []
    for karakter in orn:
        ls.append(karakter)
    return ls
print(ornek_fonks("Bu örnek bir stringdir"))

print()

# listelere uygulanan metodlardan biri de "extend" metodudur. extend metodu, append metoduna benzer yalnız
# extend metodunda eleman sayısı sınırlı değildir. listin sonuna boş bir liste, tek bir eleman veya iste-
# nen sayıda eleman içeren bir liste eklenebilir. boş liste eklendiğinde elbette listede bir değişiklik ol-
# maz. yine append metodundaki gibi listenin kendisi değişmektedir, yeni bir liste oluşmamaktadır.

nordic_ülkeler = ["Norveç", "İsveç", "Danimarka", "Finlandiya"]
print(nordic_ülkeler)
print(len(nordic_ülkeler))
nordic_ülkeler.extend(["İzlanda", "Grönland"])
print(nordic_ülkeler)
print(len(nordic_ülkeler))
# eklenecek listeyi bir değişkene de atayabiliriz:
baltık_ülkeleri = ["Estonya", "Letonya", "Litvanya"]
nordic_ülkeler.extend(baltık_ülkeleri)
print(nordic_ülkeler)
print(len(nordic_ülkeler))
# tek bir eleman da olsa argüman liste olarak girilmeli:
nordic_ülkeler.extend(["Polonya"])
print(nordic_ülkeler)
# extend içersine str tipinde bir veri girildiğinde bu veriyi karakterlerine ayırıp listeleyerek ekler.
nordic_ülkeler.extend("dfdsfsd")
print(nordic_ülkeler)

print()

# '+' syntaxıyla da listeleri tıpkı stringlerde olduğu gibi birleştirmek mümkündür. fakat bu sefer liste de-
# ğişmez, yeni bir liste oluşur. istersek bu listeyi += operatörüyle ilk listenin üzerine yazabiliriz.

dersler = ["Kimya", "Tekno", "Kognozi"]
print(dersler)
seçmeli_dersler = ["BİHAD", "EM Tasarımı"]
tüm_dersler = dersler + seçmeli_dersler
print(tüm_dersler)
# dersler ve seçmeli dersler objeleri hala aynıdır.
print(dersler)
print(seçmeli_dersler)
# dersler objesinin üzerine de yazabiliriz:
dersler += seçmeli_dersler
print(dersler) # listeyi değiştirmedik ama yeni listeyi eski listenin değişkeni üzerine yazdık.

print()

# 'insert' metodu da listelere eleman eklemek için kullanılan bir metoddur. append metodu gibi tek bir obje
# kabul eder fakat farklı olarak objeden önce bir indeks numarasını argüman olarak alır. obje bu indeks nu-
# marasına yerleştirilir. diğer indeks numaralarındaki elemanlar kaldırılmaz, sadece sonraki indekslerdeki
# karakterler birer indeks kayar. son indeksten daha büyük bir indeks girildiğinde hata alınmaz, python yeni
# objeyi listenin sonuna ekler.

plays = ["Hamlet", "Macbeth", "King Lear"]

plays.insert(1, "Julius Caesar")
print(plays)
plays.insert(0, "Romeo & Juliet")
print(plays)
plays.insert(10, "A Midsummer Night's Dream")
print(plays)

print()

# LİSTELERDE ELEMENT ÇIKARMA - SİLME

# pop metodu listelerden belirli bir indeksteki elemanı çıkarmak için kullanılır. Eğer bir argüman veril-
# mezse default olarak listenin sonundaki eleman yani -1 nolu indeks silinir. pop metodunun syntaxı bildi-
# ğimiz metod syntaxıdır; obje.pop(indeks) şeklinde çalışır ve listeyi değiştirir. diğer metodların aksine
# pop metodu listeyi değiştirirken return olarak None çıktısı vermez, silinen objeyi verir. yani:
# degisken = liste.pop() şeklinde bir syntax yazıldığında degisken, liste[-1] olur yani listenin son elemanı-
# dır; liste ise liste[:-1] yani son elemanı çıkmış şekilde olur. liste = liste.pop() şeklindeki bir syn-
# tax sonucu liste değişkeni, listenin son elemanına eşitlenir ve artık bir liste değildir! indeks negatif
# de olabilir.

ödevler = ["Kimya", "Kolagog", "Tekno", "Bakım", "BİHAD"]
print(ödevler)
# pop metoduyla BİHADı silelim mesela
ödevler.pop() # default olarak son eleman
print(ödevler)
# mesela şimdi de Kolagog u 
ödevler.pop(1)
print(ödevler)
print()
# silinenler depolayarak devam edelim mesela
ödevler = ["Kimya", "Kolagog", "Tekno", "Bakım", "BİHAD"]
biten_ödevler = ödevler.pop() # önce eşitliğin sağı çalışır. önce ödevler.pop() çalışarak ödevler listesini
# değiştirir. bu metod çıktı olarak silinen elemanı vereceğinden = in sağındaki değişkene de bu eleman tanı-
# mlanır.
print(ödevler)
print(biten_ödevler)
print(type(biten_ödevler))
print()
# şimdi biten ödevlerle de bir liste oluşturalım:
ödevler = ["Kimya", "Kolagog", "Tekno", "Bakım", "BİHAD"]
biten = []
biten.append(ödevler.pop())
print(ödevler)
print(biten)
biten.append(ödevler.pop(-3)) # ödevler listesinin son halinde kolagog -4 değil -3. indeks
print(ödevler)
print(biten)

print()

# listelerden eleman çıkarmanın bir başka yolu da "del" keywordüdür. syntaxı del obje[indeks] şeklindedir.
# pop metodunun aksine del ifadesi ile silinen elemanı çıktı olarak alamayız, yalnızca listeyi manüple ede-
# biliriz. del ifadesinin avantajı ise slicing syntaxını kullanarak [ilk ind:son ind] birden fazla
# elemanı silmek mümkündür. elbette ki ilk indeks dahil, son indeks ise dahil değildir.
örnek_liste = ["artık", "liste", "yapacak", "bi şey", "bulamadım"]
print(örnek_liste)

del örnek_liste[1]
print(örnek_liste)
örnek_liste = ["artık", "liste", "yapacak", "bi şey", "bulamadım"]
del örnek_liste[-1]
print(örnek_liste)
örnek_liste = ["artık", "liste", "yapacak", "bi şey", "bulamadım"]
del örnek_liste[0:3]
print(örnek_liste)

print()

# remove metodu listelerden eleman kaldırmanın başka bir yoludur. remove metodu argüman olarak tek bir eleman
# kabul eder ve bu elemanı listeden kaldırır. eğer aynı elemandan iki tane varsa remove metodu indeks numa-
# rası en küçük olanı siler.
komşu_ülkeler = ["Yunanistan", "Bulgaristan", "Gürcistan", "İran", "Yunanistan"]
print(komşu_ülkeler)
komşu_ülkeler.remove("Yunanistan") # sadece 0. indeksteki yunanistan stringi silinecek
print(komşu_ülkeler)
# listede olmayan bir string girildiğinde ise ValueError alınır
# komşu_ülkeler("İsviçre") # satırının yorumu kalktığında hata alınır.
# hatayı önlemek için remove metodu bir if koşuluna bağlanabilir:
if "İsviçre" in komşu_ülkeler:
    komşu_ülkeler.remove("İsviçre")
# bu durumda hata alınmaz, listeyi yazdırdığımızda aynı şekilde yazılır.

print()

# clear metodu, uygulandığı listenin uzunluğunu 0 yapar. yani basitçe listeyi boşaltır. syntax her metodda
# olduğu gibi liste.clear() şeklindedir ama parantez içine hiçbir argüman kabul etmez. listeyi manüple eder
# yani liste hala mevcuttur fakat artık boş bir listedir yani print ile çıktısı [] şeklindedir.
citrus_fruits = ["Lemon", "Orange", "Lime"]
print(citrus_fruits)
citrus_fruits.clear()
print(citrus_fruits)

print()

# LİSTELERİN BAŞKA TÜRLÜ DEĞİŞTİRİLMESİ
#--Listenin tersine değişmesi

# reversed fonksiyonu, farklı türde bir obje oluşturur ve bu obje listeyi ters sırayla iterate edebilmemizi
# sağlar. reverse metodu ise metod syntaxıyla (liste.reverse()) çalışır ve bir argüman kabul etmez. metodun
# kendisi None tipinde çıktı verir. metod uygulanmış liste ise ters sıradadır.
yağda_çözünen_vitaminler = ["A", "D", "E", "K"]
print(yağda_çözünen_vitaminler)
yağda_çözünen_vitaminler.reverse() # bu satır type fonksiyonuna alınıp print edilirse None çıktısı alınır.
print(yağda_çözünen_vitaminler)

print()

#--Listelerin sıralanması

# sort metodu numerik listelerin küçükte büyüğe, alfabetik listeleri ise alfabetik sırayla sıralanmış şek-
# line dönüştürür. metod syntaxında yazılır ve argüman kabul etmez.
temperatures = [40, 28, 52, 66, 35, -1]
print(temperatures)
temperatures.sort()
print(temperatures)
# büyükten küçüğe sıralama yapmak için basitçe sort edilmiş liste reverse metoduyla tekrar değiştirilir.
temperatures.reverse()
print(temperatures)

coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
print(coffees)
coffees.sort()
print(coffees)
# yine tersine sıralama reverse metoduyla yapılabilir
coffees.reverse()
print(coffees)

# eğer listede hem büyük harfle hem küçük harfle başlayan stringler söz konusuysa önce büyük harfle başla-
# yan stringler sıralanır sonra küçük harfle başlayan stringler sıralanır çünkü pythonun sıralama algorit-
# masında büyük harfler küçük harflerden daha önce gelmektedir.
coffees = ["Latte", "espresso", "macchiato", "Frappucino"]
coffees.sort()
print(coffees)

# sorted fonksiyonu da çıktı olarak listenin sıralanmış halini yeni bir liste olarak verir, söz konusu lis-
# teyi değiştirmez.
coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
print(sorted(coffees))
# listeyi tekrar yazdığımızda değişmediğini görürüz.
print(coffees)

öylesine = [1, 5, "abc", 3, 2, "gfhfg", "bgds", -1] # önemli bir nokta şudur; sorted fonksiyonu ve sort meto-
# du yalnızca homojen listelerde çalışmaktadır. heterojen listelerde ikisi de TypeError verir.