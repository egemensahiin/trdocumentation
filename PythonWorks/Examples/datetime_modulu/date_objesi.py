# datetime modülü, pythonda zaman ile ilgili sınıfları, objeleri içeren builtin bir kütüphanedir. date objesi, timedate modülü içersindeki bir sınıftır.
# bir date objesi, yıl, ay ve gün niteliklerinden oluşmaktadır.
import datetime
doğumGünü = datetime.date(1995, 11, 9)
print(doğumGünü)
# date objesi yalnızca bir string değil, kendisi bir sınıftır:
print(type(doğumGünü))

print()

# nitelikleri keyword argüman olarak da yazmak mümkündür.
ayaİniş = datetime.date(year = 1969, month = 7, day = 20)
# bu niteliklere nokta syntaxıyla erişmek mümkündür.
print(ayaİniş.year)
print(ayaİniş.month)
print(ayaİniş.day)

print()

# date objesinin çıktı olarak bugünün tarihini veren bir sınıf metodu mevcuttur. hatırlanacağı üzere sınıf metodları, sınıfın örneklemi üzerinde
# değil kendisi üzerinde çalıştırılırlar:
bugün = datetime.date.today()
print(bugün)
# bugün değişkeni de bir date objesini refere eder yani today metodu çıktı olarak date sınıfının bir örneklemini verir ki o da bugünün tarihidir:
print(type(bugün))
print(f"Bugün {bugün.month}. ayın {bugün.day}. günü ve sene {bugün.year}")

print()

# year niteliği 0den küçük ve 9999dan büyük olduğunda ValueError alınır.
try:
    tarih = datetime.date(0, 1, 1)
    print(tarih)
except ValueError as e:
    print(f"Yıl, aralık dışında olduğu için hata alındı: {e}\n")

# tabii ki aynı durum aylar için de geçerli. month niteliği 12den büyük 1den küçük olduğunda da ValueError alınır.
try:
    tarih = datetime.date(2021, 13, 1)
    print(tarih)
except ValueError as e:
    print(f"Ay niteliği aralık dışında verildiği için hata alındı: {e}\n")

# günler için ise durum hangi ay verildiğine göre değişir. eğer 
try:
    tarih = datetime.date(2021, 2, 30) # şubat ayında 30 gün hata verir
    print(tarih)
except ValueError as e:
    print(f"Şubat ayında 30 gün olmaz, hata alındı: {e}\n")

# ama mesela temmuzda sıkıntı yok:
try:
    tarih = datetime.date(2021, 7, 30)
    print(tarih)
except:
    print("hata yok burası yazılmayacak")