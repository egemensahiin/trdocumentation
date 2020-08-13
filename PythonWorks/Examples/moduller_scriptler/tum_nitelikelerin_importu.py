# bir modüldeki tüm nitelikleri import etmek için * kullanılır. örneğin calculator modülü yerine calculatorde
# bulununan tüm nitelikleri import etmek için:
from calculator import * # kullanılır. fakat bu syntax, tercih edilen bir kullanım değildir çünkü isim ça-
# tışmalarına yol açabilir. uzun ve çok isim bulunduran modüllerdeki tüm isimleri bu şekilde import ettiği-
# mizde karışıklıklara yol açması muhtemeldir çünkü bu durumda calculator içersindeki isimleri, calculator
# modülüne atıf yapmaksızın kullanırız:
print(creator)
print(add(3, 5))
# bir istisnası şudur; bu şekilde modüldeki tüm nitelikler import edilir fakat başında bir '_' ile tanım-
# lanmış nitelikler import edilmez. calculator.py'da ln 19'daki _sene değişkenini çağırıdığımızda, NameError
# alırız. fakar calculator.py'daki 20-21. satırların çıktısında gördüğümüz üzere _sene, modül içersinde
# tanımlı ve geçerli bir değişkendir.
# print(_sene) # çalıştırıldığında NameError
# fonksiyonlar için de aynı durum söz konusudur.
# print(_multiply(3, 5)) # çalıştırıldığında NameError