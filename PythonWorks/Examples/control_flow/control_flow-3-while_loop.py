# # while döngüleri, belirli bir koşul doğru olduğu müddetçe çalışacak bir blok şeklindedir.
# degisken = 0

# while degisken <= 5: # olsun
#     print(degisken)
#     # bu şekilde program çalışırsa sonsuz bir döngü oluşur çünkü 0 her zaman 5ten küçüktür.
#     degisken += 1
#     # while bloğu içersinde değişkeni değiştirerek yani 1 artırarak değişkeni değiştirebirilir. blok bitti-
#     # ğinde değişken, değişken + 1 olur ve tekrar 5 le karşılaştırılır. döngü degisken <= 5 koşulu yanlış
#     # olduğu müddetçe yani degisken = 6 olana kadar sürer.

# # degisken, bu döngü bittiğinde "6"dır. degiskeni yazdırarak bunu görebiliriz. degisken 6 olarak döngüye gi-
# # rer, koşul yanlış olduğu için döngü bloğu okunmaz ve döngüden sonraki kodlar okunur (line 14).
# print()
# print(degisken)

# # şimdi yukarıyı yorumlayalım ve istediğimiz koşula uygun bir değer girene kadar değer girmemizi isteyen bir
# # döngü yazalım:
# kontrol = True
# # kontrol değişkeni, döngünün bitişini kontrol etmemizi sağlayacak:
# while kontrol == True:
#     deger = int(input("Bir değer gir ki 10'dan büyük olsun..: ")) # input'un her zaman str verdiğini unutma!
#     if deger > 10:
#         print(f"Tebrikler, {deger} gerçekten de 10'dan büyük.")
#         kontrol = False # döngüyü bitiriyoruz.
#     else:
#         print(f"{deger} maalesef 10'dan büyük bir sayı değil. Tekrar dene!")
#         # burada kontrol ifadesini değiştirmiyoruz ki if koşulu yanlışsa bunu yazdıktan sonra döngü başa dön-
#         # sün.

# şimdi yukarıyı da yorumlayıp kullanıcı adı olarak hem harf hem de sayı içeren kullanıcı isimlerini geçerli sa-
# yan bir program yazalım
kontrol = True
while kontrol == True:
    isim = input("Kullanıcı adı giriniz (Harf ve sayı içermelidir.): ")
    if isim.isalnum() == True and isim.isalpha() == False and isim.isnumeric() == False:
        print(f"Tebrikler! Girdiğiniz kullanıcı adı {isim} geçerlidir!")
        kontrol = False
    else:
        print(f"Girdiğiniz kullanıcı adı {isim} geçersizdir. Tekrar deneyiniz.")