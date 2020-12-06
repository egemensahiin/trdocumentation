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