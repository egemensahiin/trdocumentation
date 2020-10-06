# bir dosyadan veri okumak için sıklıkla kullanılan bir yöntem, open fonksiyonudur. open fonksiyonu, çok ter-
# cih edilen iki pozisyonel argüman kabul eder: ilk argüman dosya ismidir ve python, mevcut klasörde bu dos-
# yayı arar, ikinci argüman ise dosyanın hangi modda açılacağını belirleyen mode argümanıdır ve ekleme yapmak
# için "a", üstüne yazmak için "w", okumak için "r" stringlerini kabul eder.
# open fonksiyonu çıktı olarak input-output tipinde bir obje verir ve bu obje bir değişkene atanarak daha
# sonra dosyayı çağırmak için kullanılabilir:
sozler = open("sozler.txt", "r")
print(sozler)
# type fonksiyonuyla çıktı aldığımızda bu objenin sınıfının '_io.TextIOWrapper' olduğunu görürüz.
print(type(sozler))
# dosyanın içeriği read metoduyla okunabilir:
print(sozler.read())
# bu syntaxla dosyayı kapatmayı unutmamalıyız. aksi takdirde dosya açık kalır ve RAM'de yer tutmaya devam e-
# der. bunun için close metodu kullanılır:
sozler.close()
# dosya kapansa da sozler değişkeni halen bir IO objesidir.
print(type(sozler))

print()

# open-close syntaxında en önemli problem, open fonksiyonu ve close metodunun kullanımı kısıtlıdır. bunun
# sebebi, bu arada mesela 12. satırda meydana gelecek bir hata sonucu program sona erse de close metodu ça-
# lışmayacağı için dosyanın açık kalmasıdır. bu durumda açık kalan dosya RAM ve CPUda yer tutmaya devam e-
# derek performans düşüşüne yol açar. bu sebeple with keywordu kullanılır. with keywordu bir blok oluşturur
# ve blok içersinde hata olsun ya da olmasın blok sonlandığında doyayı kapatır.
with open("sozler.txt", "r") as sozler_dosyası:
    içerik = sozler_dosyası.read()
    print(içerik)
# with bloğu bittikten sonra da içersindeki değişkenler geçerlidir:
print(sozler_dosyası)
print(içerik)

print()

# open fonksiyonuyla oluşturduğumuz obje, bir iterable objedir. dolayısıyla bir dosyayı okumanın en etkin yolu
# dosyayı for döngüsüyle satır satır okumaktır. bu sayede istediğimiz satırı okumamız mümkündür, diğer satır-
# ları okumayarak performanstan tasarruf edebiliriz.
with open("sozler.txt", "r") as sozler:
    for satır in sozler:
        print(satır)
print()
# çıktıda gördüğümüz üzere satır arası boşluklar, normalde olduğundan daha fazla. bunun sebebi print fonksiyo-
# nunun her yazımdan sonra bir satır sonu eklemesidir. dosyada da her satır, bir satır sonuyla bittiği için
# iki satır sonu birlikte yazdırılır. bunu önlemek için her satır, strip metodundan geçirilebilir. en nihaye-
# tinde her satır birer string olduğu için mesela rstrip metoduyla sağdaki fazla satır sonu silinebilir:
with open("sozler.txt", "r") as sozler:
    for satır in sozler:
        print(satır.rstrip())
