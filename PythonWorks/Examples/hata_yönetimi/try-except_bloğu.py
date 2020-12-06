# normalde python, bir hata ile (exception/istisna) karşılaştığında bir hata mesajı verip programı sonlandırır. bu hata mesajı, dosya yolu, hatanın
# ortata çıktığı konum (satır) ve hataya özel isimden (AttributeError, NameError vs.) oluşan bir mesajdır. fakat pythonda, hata durumunu kontrol e-
# debilir, programın hatadan alması durumundaki davranışını yönetebiliriz.
def beşi_böl(n):
    return 5 / n
print(beşi_böl(10))
# yukarıdaki fonksiyonu, n = 0 şeklinde çalıştırdığımızda python 0'a bölüm hatası (ZeroDivisionError) verir:
# print(beşi_böl(0))

# mesela programımızın bundan sonra hiçbi şey yokmuş gibi devam etmesini isteyebiliriz veya bir hata mesajı verip yaptığı işi yapmaya devam etmesini
# isteyebiliriz. bunun için try ve except keywordlerini kullanırız. try ve except keywordleri birer blok oluşturur. try bloğu içerisine yazdığımız
# kodun (kaç satır olduğu ne olduğu önemli değil blok dahilindeki her şeyin) çalışıp çalışmadığını kontrol eder. eğer içerdeki kod hata veriyorsa
# except bloğu içersindeki kod çalışır. eğer try bloğundan hata alınmazsa, except bloğu çalışmaz:
def dördü_böl(n):
    try:
        hesaplama = 4 / n
    except:
        hesaplama = 0

    return hesaplama

# dördü_böl fonksiyonuna 0 değeri verildiğinde artık hata almak yerine 0 çıktısını alacağız:
print(dördü_böl(0))
# diğer sayılarla normal şekilde çalışmaya devam eder:
print(dördü_böl(3))

# bunun yerine daha iyi bir pratik, return keywordünü try bloğunda çalıştırmaktır. hata vermeyen ve çalışmaya devam eden bir bölme fonksiyonu için:
def üçü_böl(n):
    try:
        return 3 / n
    except:
        pass

print(üçü_böl(0)) # görüldüğü gibi None çıktısı alınıyor.
print(üçü_böl(7)) # hata vermeyen değerlerle normal çalışmaya devem ediyor.
# bu çerçevede except keywordü tüm hatalar için aynı şeyi yapar:
print(üçü_böl("Bölünür mü aq??")) # TypeError için de aynı şekilde davranıyor.
# normalde bu çok iyi bir pratik değildir farklı hata türleri farklı davranışlar gerektirir. bunun için except keywordünden sonra hangi istisna için
# bloğun çalışacağı belirtilmelidir.
def altıyıböl(n):
    try:
        return 6 / n
    except ZeroDivisionError:
        return "Hiçbir sayıyı sıfıra bölemezsiniz!"

print(altıyıböl(12))
print(altıyıböl(0))
# bu sefer başka bir hata durumunda normal hata davranışı gözlenir:
# print(altıyıböl("Bölünür mü aq??"))

# birden fazla hatanın yönetimi için iki farklı except bloğu oluşturmak da mümkündür:
def onu_böl(n):
    try:
        return 10 / n
    except ZeroDivisionError:
        return "Hiçbir sayıyı sıfıra bölemezsiniz!"
    # eğer hata mesajını, except bloğunda refere etmek istersek, as keywordünü kullanabiliriz.
    except TypeError as e:
        return f"Geçersiz objelere bölüm yapılamıyor! {e}"

print(onu_böl(0))
print(onu_böl("askdak"))
print(onu_böl(9))

# aynı anda birden fazla hatanın ayıklanması için hatalar, tuple'lar içersine alınır:
def yediyi_böl():
    try:
        return 7 / n
    except (ZeroDivisionError, TypeError) as e:
        return f"Bir hata oluştu! {e}"

print(yediyi_böl(0))
print(yediyi_böl(7))
print(yediyi_böl(""))
