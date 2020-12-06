# tıpkı listelerde olduğu gibi sözlüklerde de comprehension, iterable bir objeden sözlük oluşturmak için ku-
# llanılır. sözlük oluştururken key-value çiftleri için kural normal bir sözlükteki gibi ":" ile tanımlanır.
# ardından for döngüsü tanımlanır ve gerekirse for döngüsünden sonra da koşul ifadesi konulur.
# örnek olarak bir listedeki elemanları, karakter sayılarıyla bir sözlük haline getirelim.
# öncelikle fonksiyon anlayışını inceleyelim:
programlama_dilleri = ["Python", "JavaScript", "Bash", "Ruby", "C++"]
def len_dict(liste):
    sonuç = {}
    for eleman in liste:
        sonuç[eleman] = len(eleman)
    return sonuç
print(len_dict(programlama_dilleri))
# bu kadar uzun bir syntax yerine tek satırda bu sözlüğü tanımlamak mümkündür:
uzunluklar = { dil: len(dil) for dil in programlama_dilleri }
print(uzunluklar)
# hatta aynı satırda bu sözlüğü, bir koşula bağlı da oluşturabiliriz. mesela içinde sadece "t" olanlar:
uzunluklar = { dil: len(dil) for dil in programlama_dilleri if "t" in dil }
print(uzunluklar)

print()

# listeler dışındaki iterable objelerle de comprehension uygulanabilir. mesela bir kelimedeki harflerin
# sayılarıyla eşleşmesiyle bir sözlük oluşturalım. önce fonksiyon ile bunu ele alalım:
kelime = "çekoslovakyalılaştıramadıklarımızdan mısınız"
def harf_sayıları(string):
    sonuç = {}
    for harf in string:
        sonuç[harf] = string.count(harf)
    return sonuç
print(harf_sayıları(kelime))
# bunu da yine comprehension anlayışıyla tek satırda tanımlamamız mümkündür.
sayılar = { harf: kelime.count(harf) for harf in kelime }
print(sayılar)
# bu durumda da yine koşulları kullanabiliriz. mesela harfler arasında da karşılaştırma yapmamıza olanak ta-
# nıyan > veya < operatörleriyle yalnızca belli bir harften sonrakileri test edebiliriz:
sayılar = { harf: kelime.count(harf) for harf in kelime if harf > "l" }
print(sayılar)

print()

# bir örnek de sözlükten başka bir sözlük oluşturma durumu için uygulayalım. tanımladığımız sözlüğün key-va-
# lue çiftlerinin yerlerini değiştirelim:
ülkeler_ve_başkentler = {
    "Almanya"   : "Berlin",
    "Norveç"    : "Oslo",
    "Lüksemburg": "Lüksemburg" 
}
print(ülkeler_ve_başkentler)
başkentler_ve_ülkeler = { başkent: ülke for ülke, başkent in ülkeler_ve_başkentler.items() }
print(başkentler_ve_ülkeler)
# yine koşullu ifadelerin uygulanması mümkündür:
mantıklı_başkentler = { başkent: ülke for ülke, başkent in ülkeler_ve_başkentler.items() if ülke != başkent }
print(mantıklı_başkentler)