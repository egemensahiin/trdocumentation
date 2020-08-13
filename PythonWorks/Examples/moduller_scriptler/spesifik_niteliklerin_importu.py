# eğer bir yalnızca bir modüldeki spesifik bir veya birkaç niteliği import etmek istiyorsak, from ve import
# keywordlerini birlikte kullanırız. syntaxı şu şekildedir: from <modül> import <attribute>, <attribute> ..
# dikkat edilmesi gereken; faklı modüllerden aynı isimli nitelikleri çağırdığımızda, daha alt satırdaki nite-
# lik import edilir (esasında ikisi de import edilir ama isme karşılık gelen nitelik daha sonra import edi-
# lendir).
from calculator import creator, area
from math import sqrt
# çağrılan niteliklerin public nitelikler olması önemlidir. mesela 'değişken', calculator1 modülünde
# __name__ == __main__ koşulu altında tanımlanmıştır. bulunduğumuz scriptte calculator1 için __name__ bu
# koşulu sağlamaz ve 'değişken'i import etmeye çalıştığımızda ImportError alırız.
# from calculator1 import değişken

# yalnızca spesifik nitelikleri import ettiğimizde artık bunları modül.nitelik şeklinde çağırmamıza gerek
# yoktur, nitelik modülden bağımsız olarak import edilir.
print(creator)
print(area(5))
print(sqrt(3))