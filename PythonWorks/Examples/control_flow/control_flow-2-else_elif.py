# else ifadesi, if ila birlikte kullanılır ve if ifadesi yanlış olduğunda program için alternatif bir yol o-
# luşturur. eğer if ifadesi yanlış ise if bloğu okunmaz. sonrasında eğer bir else bloğu varsa else bloğu o-
# kunur, eğer if ifadesi doğruysa if bloğu okunur ve bu sefer else bloğu okunmadan program devam eder.
if 5 > 3:
    print("Bu ifade doğru") # burası okunur çünkü if ifadesi doğrudur.
else:
    print("Bu ifade yanlış")

if 5 > 10:
    print("Bu ifade doğru")
else:
    print("Bu ifade yanlış") # burası okunur çünkü if ifadesi yanlış.

# daha anlaşılır olması için bunu bir input fonksiyonuyla birleştirebiliriz. o yüzden yukarıyı yorumlayalım.
# programımız kendisine verilen inputun tamamen alfabetik olmasını istesin aksi taktirde uyarı versin mesela:
# degisken = input("Bir şeyler yaz! Ama alfabetik mümkünse: ")

# if degisken.isalpha() == True:
#     print("Evet bu string hakikaten alfabetik!")
# else:
#     print("O kadar yazdık oraya neresini anlamadın?")

print()

# tek bir if ve else ifadesinin birlikte kullanımı için alternatif bir şablon mevcuttur:
# degisken = "doğru ise" if ifade else "yanlış ise"
# anlaması biraz zor, örneğe bak
tel_no = "5115115151"
if len(tel_no) == 10:
    kontrol = "Geçerli"
else:
    kontrol = "Geçersiz!"

# bu şekilde 4 satırda yazmak yerine tek satırda aynı ifadeyi yazabiliriz.
kontrol = "Geçerli!" if len(tel_no) == 10 else "Geçersiz!"
print(kontrol)
# hatta hadi bunu fonksiyon yapalım:
def tel_kontrol(a):
    a = str(a)
    kontrol = "Geçerli" if len(a) == 10 else "Geçersiz!"
    return kontrol
print(tel_kontrol(52365978526))
print(tel_kontrol(5115115151))

print()

# elif ifadesi de else e benzer (zaten else if in kısaltması) ama else'in aksine elif, koşul belirtir. else,
# bağlı olduğu if koşulu yanlış olduğu müddetçe okunur fakar elif'in okunması için hem if koşulunun yanlış
# olması hem de elif koşulunun doğru olması gerekir. örneğin her halükarda bir çıktı elde etmemiz gerektiği-
# nde else ifadesini kullanmamız daha doğrudur çünkü else ifadesi yukarısındaki if ve elifler yanlış olduğu
# müddetçe okunur, başka bir koşula beğlı değildir fakat belli koşullar dışında ifadelerden çıktı almak is-
# temiyorsak elif kullanmamız gerekir çünkü elif de tıpkı if gibi belli koşullara bağlıdır fakat üzerindeki
# if doğru olduğunda okunmaz.

def pozitif_negatif(a):
    if a > 0:
        return "sayı pozitif."
    elif a < 0:
        return "sayı negatif."
    else:
        return "sayı pozitif veya negatif değil! sayı 0."
# bu şekliyle bu fonksiyonu çalıştırdığımızda:
    # a>0 ise sayı pozitif çıktısı verir.
    # a<0 ise sayı negatif çıktısı verir.
    # a>0 veya a<0 değilse sayı 0 çıktısı verir
print(pozitif_negatif(5))
print(pozitif_negatif(-3))
print(pozitif_negatif(0))
# bu fonksiyonu şu şekilde de yazmak mümkündür.
def pozitif_negatif(a):
    if a > 0:
        return "sayı pozitif."
    elif a < 0:
        return "sayı negatif."
    elif a == 0:
        return "sayı pozitif veya negatif değil! sayı 0."
print(pozitif_negatif(5))
print(pozitif_negatif(-3))
print(pozitif_negatif(0))

# başka bir örnek:
def hesap(işlem, a, b):
    if işlem == "topla":
        return a + b
    elif işlem == "çıkar":
        return a - b
    elif işlem == "çarp":
        return a * b
    elif işlem == "böl":
        return a / b
    else:
        return "Ne yapayım anlamadım!!"

print(hesap("topla", 5, 2))
print(hesap("çıkar", 5, 2))
print(hesap("çarp", 5, 2))
print(hesap("böl", 5, 2))
print(hesap("logaritma", 5, 2))
