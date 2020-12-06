# comprehension, bir iterable objeden, başka bir iterable obje oluşturulmasıdır.
# pythonda liste comprehensionı ve iterasyonu diğer dillerden farklıdır. bunun en önemli faydası, pythonda
# bir iterable objeden liste oluştururken tek satırlık bir syntax sunuyor olmasıdır. mesela elimizde bir
# takım numaralardan oluşan bir liste olsun ve bu listeden hareketle sayıların karesinden oluşan başka bir
# liste oluşturulım:

sayılar = [2, 4, 5, 7, 8]

# klasik syntax ile bunu yapmak için önce boş bir liste tanımlamayız
kareler = [] # ardından sayıları for döngüsüyle tek tek çağıracağız
for sayı in sayılar: # her bir sayının karesini kareler listesine append metoduyla ekleyeceğiz
    kareler.append(sayı ** 2)

print(kareler)
# bu syntaxın önemli problemlerinden biri alternatifine göre uzun sürmesi. bir diğeri de for döngüsünde o-
# luşturulan "sayı" değişkenine değer atanması. eğer programın öncesinde bir sayı değişkeni atanmışsa, daha
# sonra bu değişken tekrar kullanıldığında for döngüsünde bu değişkenin değitiği unutulabilir.
print(sayı)

# pythonun listelerden veya herhangi bir iterable objeden yeni liste oluşturmak için farklı bir mantığı var-
# dır. bu syntax şu şekildedir: [X ile yapılan işlemler for X in ITER] burada normal bir for döngüsünden
# farklı olarak boş bir liste oluşturmuyoruz ve işlemleri, for ifadesinden önce tanımlıyoruz. ayrıca burada
# x bir değişken olarak oluşturulmuyor, yalnızca [] arasında oluşturulup bunun dışına çıkmıyor. aynı işi
# bu syntaxla yapalım:
kareler = [sayıı ** 2 for sayıı in sayılar]
print(kareler)
# burada sayıı değişkenini yazdırmak istediğimizde yukarıdaki gibi en son aldığı değeri almayız, NameError
# alırız çünkü sayıı değişkeni bu liste dışında tanımlı değildir.
# print(sayıı) # yorum kaldırıldığında NameError alınır.
# mesela bir stringdeki tüm karakterleri bir liste haline getirirken de kullanabiliriz mesela çünkü string-
# ler de iterable'dır.
string = "asdalskdjlajd"
print(string)
print([karakter for karakter in string])

# bir stringdeki karakterlerin alfabedeki yerlerinden oluşan bir liste oluşturalım mesela
print([" abcçdefgğhıijklmnoöprsştuüvyz".index(char) for char in "egemen şahin"])

# veya mesela ondalık sayılardan oluşan bir listeden, tamsayılardan oluşan bir liste yapalım
ondalıklar = [1.2, 2.3, 3.4, 4.5, 5.6]
print([int(ondalık) for ondalık in ondalıklar])

# veya generator objeler de kullanılabilir mesela bir listeti tersten oluşturmak için şunu yapabiliriz:
liste = [1, 2, 3, 4, 5]
print([el for el in reversed(liste)])

# koşul ifadesi vererek belirli elemanları seçmek de mümkündür. mesela dersler arasından adında Farmasötik
# olanları seçerek yeni bir liste oluşturalım:
dersler = [
    "Farmasötik Botanik",
    "Farmasötik Teknoloji",
    "Analitik Kimya",
    "Biyokimya",
    "Farmasötik Kimya"
]
# alışılageldik syntax ile
farmasötikler = []
for ders in dersler:
    if "Farmasötik" in ders:
        farmasötikler.append(ders)

print(farmasötikler)

# pythonun liste comprehensionıyla bu şekilde koşullu ifadeler ile listeyi filtrelemek mümkündür. bunun
# için geçerli syntax; [X ile işlemler for X in İTER if X ile ilgili koşul] şeklindedir.
print([ders for ders in dersler if "Farmasötik" in ders])
# mesela dersi yazdırırken farmasötik yazdırmayalım
print([ders.split(" ")[1] for ders in dersler if "Farmasötik" in ders]) # split metoduyla veya;
print([ders[11:] for ders in dersler if "Farmasötik" in ders]) # indeks slicing ile yapabiliriz.

# veya mesela 0'dan 20'ye kadar olan sadece çift sayıların yarısını yazdıralım
print([sayı / 2 for sayı in range(21) if sayı % 2 == 0])
# hatta bi de bunları tam sayı olarak yazdıralım
print([int(sayı / 2) for sayı in range(21) if sayı % 2 == 0])