# standart kütüphane, geliştirme ve üretkenliği arttırırmak ve hızlandırmak için bir dilde yerleşik bulu-
# araç koleksiyonudur. pythonun hem python dilinde hem c dilinde yazılmış 250den fazla standart kütüphane-
# si bulunmaktadır ve bunlar matematik, istatistik, rastgelelik, işletim sistemine erişim gibi pek çok
# aracı hazır halde sunmaktadır. kendi modüllerimiz gibi standart modüller de gerektiğinde geliştirici ta-
# rafından import edilirler.
# kendi modüllerimizin aksine standart modülleri import ederken aynı klasörde olması gerekmez. import key-
# wordü ile bir modülü çağırdığımızda python modülü önce local konumda arar. eğer mevcut klasörde veya ve-
# rilen yolda modülü bulamazsa, pythonda tanımlı global konumlarda arar ve standart kütüphanedeki modül-
# leri bu yolla bulup import eder.
# örnek olarak, ASCII karakterlerle ilgili name'ler içeren bir standart modül olan string modülünü import
# edip bir kaç niteliğini görelim:
import string
import math

# mesela string metodundaki niteliklerden bir kaçı ingilizce alfabedeki tüm karakterleri bir stringde de-
# polayan ascii_letters değişkenidir.
print(string.ascii_letters)
# yalnızca büyük veya küçük harflerin olduğu değişkenler de vardır.
print(string.ascii_lowercase)
print(string.ascii_uppercase)
# sayılar için digit niteliği:
print(string.digits)
# hatta string modülünde, title metoduna benzer şekilde baş harfleri büyük yeni bir string veren capwords
# fonksiyonu da vardır.
print(string.capwords("selam bebek ben mayk bebek"))
# pythonun resmi github reposundan, standart library'deki modüllere kolaylıkla erişmek mümkündür.

print()

# bir başka örnek de math modülüdür.
# mesela calculator.py da tanımladığımız pi değişkeni esasında math modülünde mevcuttur:
print(math.pi)
# sayıyı üste yuvarlayan ceil, alta yuvarlayan floor veya kare kökünü (square root) alan sqrt gibi pek çok
# fonksiyonu da sunar:
print(math.ceil(4.5))
print(math.floor(4.8))
print(math.sqrt(9))
print(math.sqrt(32))