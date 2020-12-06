# recursion, bir fonksiyonun kendi kendini çağırmasıdır. mesela bir geri sayım fonksiyonu yazalım ve kendi-
# sine verdiğimiz sayıdan 0'a kadar olan sayıları sırayla yazdırsın. bunun iki yolu vardır.

# # ilki tabii ki de while döngüsü oluşturmak:
# def gerisayım(sayı):
#     while sayı >= 0:
#         print(sayı)
#         sayı -= 1
# gerisayım(10)
# # bu programın mantığı basittir: sayı değişkeni 0'dan büyük veya 0'a eşit olduğu sürece sayı değişkenini yaz-
# # dır ve sayı değişkenini, bir eksiğiyle değiştir.

# print()

# şimdi de recursion ile aynı fonksiyonu yazalım:
def gerisayım(sayı):
    if sayı < 0:
        return # öncelikle koşulu belirtiyoruz. return, fonksiyonu bitiriyor. ifade yanlış olunca line 19
    print(sayı) # çalışıyor. doğru olduğunda ise fonksiyon bitiyor.
    gerisayım(sayı - 1) # olayın asıl kısmı bu. sayıyı yazdırdık ve line 20'ye geldik line 20'de aynı fonk-
    # siyonu bu sefer sayı - 1 için çalıştırdık. bunu yapınca öncelikle if satırı devreye girdi ve sayı - 1
    # in 0'dan küçük olup olmadığını kontrol etti. eğer küçük değilse ifade yanlış olduğu için if bloğu ça-
    # lışmadan devam etti ve sayı - 1 print edildi. ardından gerisayım fonksiyonu yine mevcut sayının bir
    # eksiği yani sayı - 2 için çalıştı. ta ki if koşulu sağlanıp return komutu çalışana kadar çünkü fonksi-
    # yonlarda return komutundan sonrası okunmaz.
gerisayım(10)