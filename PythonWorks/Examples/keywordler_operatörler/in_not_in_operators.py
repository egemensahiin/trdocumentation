# in ve not in operatörleri, bir obje içersinde (genellikle string) istenilen bir ifa-
# denin varlığı (in) veya yokluğu (not in) ile ilgili boolean objesi türünde bir bil-
# gi verir. kullanılışı "aranan obje" in (veya not in) "içerisinde arama yapılan ob-
# je" şeklindedir. aranan obje eğer ki varsa "in" operatörüyle "True", "not in" ope-
# ratörüyle ise "False" çıktısı alınır. aksi durumda "in" operatörü "False", "not in"
# operatörü ise "True" bilgisini verir.
a = "Kimya" in "Kimyasal çalışmalarda bilgisayar bilimleri oldukça önemlidir."
print(a) # True
ornek = "Kimyasal çalışmalarda bilgisayar bilimleri oldukça önemlidir."
print("fizik" in ornek) # False
# aranan string için büyük küçük harfin önemli olduğu unutulmamalıdır.
print("kimya" in ornek) # False
print("fizik" not in ornek) # True
# in veya not in operasyonlarıyla her hangi bir string aranabilir.
print(" " not in "Bu örnek bir stringdir.") # False