# raise keywordünü kullanarak kendi tanımladığımız hataları da kullanabileceğimizden bahsetmiştik. pythonda tekrar tekrar söylediğimiz gibi her şey objedir.
# bunda hatalar da dahil. pythondaki tüm hatalar, Exception üst sınıfından miras alan alt sınıflardır. biz de Exception üst sınıfına bir alt sınıf tanımla-
# yıp kendi hatalarımızı oluşturabiliriz.
class NegativeNumberError(Exception): # hatalarımızı daha spesifik kılmak adına mesela ValueError, AttributeError gibi sınıfların alt sınıfı olarak da ta-
    # nımlayabiliriz. teknik olarak pek bi şey değiştirmese Exceptiondan miras alan hatalar daha yaygın kullanılır, daha stabildir.
    """Bir veya daha fazla sayı negatif verilmiş""" # genellikle hatalarda bir açıklama verilir ardından blok sonlandırılır. hata mesajı ise hata koşulu ile
    # beraber raise keywordü ile tanımlanır.
    pass

def pozitifse_ekle(a, b):
    try:
        if a <= 0 or b <= 0:
            raise NegativeNumberError # hata mesajını boş bırakmak istediğimizde böyle bırakıyoruz, boş parantez kullanmıyoruz
        return a + b
    except NegativeNumberError:
        return "Utan be adam pozitif dedik amk!!"
    
# deneyelim bakalım
print(pozitifse_ekle(5, 6))
print(pozitifse_ekle(-5, 6))
print(pozitifse_ekle(5, -6))

# raise keywordünü mesajla kullanmak daha iyi olur tabii:
class PositiveNumberError(Exception):
    """Bir veya daha fazla sayı negatif verilmiş."""
    pass

def negatifse_topla(a, b):
    try:
        if a >= 0 or b >= 0:
            raise PositiveNumberError("Sayılardan en az biri pozitif.")
        return a + b
    except PositiveNumberError as err:
        return f"Okuman yazman yok değil mi? Hata var: {err}"
    
print(negatifse_topla(-5, -6))
print(negatifse_topla(5, -6))
print(negatifse_topla(-5, 6))

print()
# Kullanıcı tanımlı hatalarda inheritance
# --------------------------------------
# pyhthonda kendi tanımladığımız hataları bir modül içersinde toplamak genellikle iyi bir pratiktir. bazı programlarda, programcılar benzer
# hataları, aynı mantıkla yükselen hataları bir hata sınıfının alt sınıfları olarak tanımlarlar. yalnız hendi hatalar hiyerarşimizi oluştururken
# her miras alımın en üstünde, pythonun built-in hata sınıflarından birinin miras alındığına dikkat etmemiz lazım:
class Hatalar(Exception):
    pass

class SaçmaHata(Hatalar):
    pass

class MantıksızHata(Hatalar):
    pass

# bu durumda SaçmaHata ile MantıksızHata, kardeş sınıflardır çünkü aynı parenttan köken alırlar.
try:
    raise SaçmaHata("Saçma sapan hareketler yapmasan mı..")
except SaçmaHata as e:
    print(f"Bir hata buldum: {e}")

try:
    raise MantıksızHata("Mantık arıyorum bulamıyorum.")
except MantıksızHata as e:
    print(f"Bir hata buldum: {e}")

# gördüğümüz gibi iki hata da başarılı şekilde çalışıyor. fakat unutmamız gereken şu, kardeş objeler aynı objeler değildir. yani:
# try:
#     raise SaçmaHata("Saçma sapan hareketler yapmasan mı..")
# except MantıksızHata as e:
#     print(f"Bir hata buldum: {e}")
# bu bloklar çalıştığında SaçmaHata alırız ama except bloğu MantıksızHata beklediği için program 68. satırda sonlanır ve TraceBack verir.

# fakat her iki hata da Hatalar objesinin altında olduğu için Hatalar, her ikisini de yakalar:
try:
    raise SaçmaHata("Saçma sapan hareketler yapmasan mı..")
except Hatalar as e:
    print(f"Bir hata buldum: {e}")

try:
    raise MantıksızHata("Mantık arıyorum bulamıyorum.")
except Hatalar as e:
    print(f"Bir hata buldum: {e}")

# bu şekildeki bir pratik her program için uygun olmayabilir. sonuçta hataları spesifik durumları test etmek için yazdığımızı düşünürsek
# tek bir üst sınıfın iki farklı hatayı yakalamasını istemeyebiliriz. fakat bunların hepsi pratiğe göre. bilmekte fayda var.