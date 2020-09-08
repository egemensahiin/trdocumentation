# bir dosyadan veri okumak için sıklıkla kullanılan bir yöntem, open fonksiyonudur. open fonksiyonu, çok ter-
# cih edilen iki pozisyonel argüman kabul eder: ilk argüman dosya ismidir ve python, mevcut klasörde bu dos-
# yayı arar, ikinci argüman ise dosyanın hangi modda açılacağını belirleyen mode argümanıdır ve ekleme yapmak
# için "a", üstüne yazmak için "w", okumak için "r" stringlerini kabul eder.
# open fonksiyonu çıktı olarak input-output tipinde bir obje verir ve bu obje bir değişkene atanarak daha
# sonra dosyayı çağırmak için kullanılabilir:
diller = open("diller.txt", "r")
print(diller)
# type fonksiyonuyla çıktı aldığımızda bu objenin sınıfının '_io.TextIOWrapper' olduğunu görürüz.
print(type(diller))
# dosyanın içeriği read metoduyla okunabilir:
print(diller.read())
# bu syntaxla dosyayı kapatmayı unutmamalıyız. aksi takdirde dosya açık kalır ve RAM'de yer tutmaya devam e-
# der. bunun için close metodu kullanılır:
diller.close()
# dosya kapansa da diller değişkeni halen bir IO objesidir.
print(type(diller))

print()

# open-close syntaxında en önemli problem, open fonksiyonu ve close metodunun kullanımı kısıtlıdır. bunun
# sebebi, bu arada mesela 12. satırda meydana gelecek bir hata sonucu program sona erse de close metodu ça-
# lışmayacağı için dosyanın açık kalmasıdır. bu durumda açık kalan dosya RAM ve CPUda yer tutmaya devam e-
# derek performans düşüşüne yol açar. bu sebeple with keywordu kullanılır. with keywordu bir blok oluşturur
# ve blok içersinde hata olsun ya da olmasın blok sonlandığında doyayı kapatır.
with open("diller.txt", "r") as diller_dosyası:
    içerik = diller_dosyası.read()
    print(içerik)
# with bloğu bittikten sonra da içersindeki değişkenler geçerlidir:
print(diller_dosyası)
print(içerik)
