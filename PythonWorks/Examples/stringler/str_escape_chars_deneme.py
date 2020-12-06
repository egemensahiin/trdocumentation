# escape karakterler, "\" (backslash, ters slash) ile yazılan karakterlerdir.
# \n, kendisinden sonra gelen kısmı bir alt satıra yazar.
print("Bu stringin bir \nkısmı alt satırda \nyazılacak")
# \t ise kendisinden önce bir "tab" yani 4 space boşluk bırakır.
print("\tBir tab boşluk bıraktık.")
# sting içersinde çift tırnak kullanmak istediğimizde pyhton bu çift tırnağı, stringi
# bitirmek için kullandığımızı düşünür ve istediğimiz şekilde bir string oluşturamayız.
# bu sebeple string içersinde tırnak işaretinden önce \ koyarak karakter olarak elde e-
# debiliriz.
print("Ne demiş atalarımız, \"sakla samanı, gelir zamanı\"")
# aslında bunu, tırnak işaretlerini değiştirerek de yapabiliriz. mesela string içersin-
# de çift tırnak kullanılacaksa stringi tek tırnak içinde tanımlayabiliriz.
print('Ne demişler, "damlaya damlaya göl olur"')
# veya
print("Sonra o da demiş ki, 'sana ne lan hoşaf'")
# eğer string içersinde karakter olarak \ kullanmak istiyorsak \'tan önce de \ koya-
# rak kullanabiliriz.
print("Bu bir backslash'tır: \\")
# veya mesela windows dosya adresleri gibi pek çok backslash içeren metinleri yazarken
# string önüne r harfi (yani raw manasında) konarak (r"string\") string içersindeki
# escape karakterler görmezden gelinebilir.
print("C:\new_folder\types\escape_characters") # yazıldığında \n ve \t escape karakter
# olarak alınır. bu stringi istenen şekilde yazdırmak için
print(r"C:\new_folder\types\escape_characters")
# eğer line'ı iki sıraya yazmak istersek de backslash kullanabiliriz. mesela uzun isim-
# li değişkenler tanımlayalım ve bunları görünür şekilde bir sıra halinde yazalım
bu_bir_degisken = 5
bu_daha_uzun_isimli_bir_degisken = 10
bu_da_bayagi_uzun_isimli_bir_degisken = 25
toplam = bu_bir_degisken + \
         bu_daha_uzun_isimli_bir_degisken + \
         bu_da_bayagi_uzun_isimli_bir_degisken
print(toplam)
# fakat fonksiyonlar içersinde böyle bir şey yapmaya gerek yoktur. fonksiyonun başlan-
# gıcı ve bitişi zaten parantezlerle belirlenmiştir.
print(bu_bir_degisken + 
      bu_daha_uzun_isimli_bir_degisken + 
      bu_da_bayagi_uzun_isimli_bir_degisken)
print(bu_bir_degisken, 
      bu_daha_uzun_isimli_bir_degisken, 
      bu_da_bayagi_uzun_isimli_bir_degisken)