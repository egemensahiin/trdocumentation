import random
import time
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

print()

# recursionun güzel bir örneği binary search konseptidir. pythonda sıralı bir listede bir elemanın varlığını
# aradığımızı farzedelim. bunu iki şekilde uygulamak mümkündür. ilki normal arama yani tüm elemanların tek tek
# sorgulanmaası diğeri ise binary search yani "böl ve fethet" mantığı. binary search algoritmasında, hedefin
# önce listenin ortasındaki elemana eşit olup olmadığı kontrol edilir. eğer eşit ise hedefe ulaşılmıştır.
# eşit olmaması durumunda ise hedefin, ortadaki sayıdan büyük olup olmadığı kontrol edilir. eğer büyükse bu
# sefer listenin sağındaki elemanların ortasında aranır, küçükse sağdaki elemanların ortasında aranır ve böyle
# devam eder. anlatırken de yazarken de normal aramadan uzun sürse de binary search, arama hızını arttıran
# bir algoritmadır.
def normal_arama(liste, hedef):
    for i in range(len(liste)):
        if liste[i] == hedef:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    
    if high < low:
        return -1
    
    mid = (low + high) // 2

    if l[mid] == target:
        return mid
    elif target > l[mid]:
        return binary_search(l, target, mid + 1, high)  # return etmeyi unutma fonksiyon çağırımlarını. yoksa None çıktısı alınır.
    else:
        return binary_search(l, target, low, mid - 1)

liste = [1, 3, 5, 7, 9, 11, 12, 30]
print(normal_arama(liste, 3))
print(binary_search(liste, 3))

# şimdi bunların ortalama ne kadar sürdüğüne bakalım:
if __name__ == '__main__':
    uzunluk = 10000
    sıralı_liste = set()
    while len(sıralı_liste) < uzunluk:
        sıralı_liste.add(random.randint(-3 * uzunluk, 3 * uzunluk))
        # while döngüsünde, -30000 ile +30000 arasındaki rastgele sayılardan oluşan bir set oluşturduk.
    sıralı_liste = sorted(list(sıralı_liste))
    # şimdi de bu seti sıralı bir liste haline getirdi.
    # listedeki her hedef için arama yapalım ve ortalamasını alalım:
    başlangıç = time.time()
    for hedef in sıralı_liste:
        normal_arama(sıralı_liste, hedef)
    bitiş = time.time()
    print(f'Normal arama yaptığımızda bir elemanın aranıp bulunması ortalama {(bitiş - başlangıç) / uzunluk} saniye sürdü.')
    # listedeki her hedef için bu sefer binary search yapalım ve ortalamasını alalım:
    başlangıç = time.time()
    for hedef in sıralı_liste:
        binary_search(sıralı_liste, hedef)
    bitiş = time.time()
    print(f'Binary search yaptığımızda bir elemanın aranıp bulunması ortalama {(bitiş - başlangıç) / uzunluk} saniye sürdü.')