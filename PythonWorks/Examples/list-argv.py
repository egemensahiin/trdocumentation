# aslında argv, sys modulünü import ederek kullanabileceğimiz bir ifade ve modüller daha sonra işlenecek bir
# konu fakar argv, bir liste olması açısından önemli. ilk önce sys modülünü import edelim
import sys

# argv, python programları bash'e yazılan argümanlarla besler. argv listesi komut satırına yazılan her şeyi
# listeler ve bu listenin elemanları, komut satırına yazılmış ve boşlukla ayrılmış yazınlardan oluşur. ya-
# zılanların hepsi listeye string olarak kaydedilir. mesela sys.argv ile komut satırından liste oluşturalım
# ve bunu yazdıralım.

# print(sys.argv) # programı açmak için yalnızca python list-argv.py yazıldığında tek elemanlı bir liste ola-
# # rak ['list-argv.py'] yazdırılır. bu tip bir objenin (sys.argv) liste olduğunu, tipini yazdırarak ispatla-
# # yabiliriz.
# print(type(sys.argv)) # aşağıdaki döngü için burayı bi commentleyelim

print()

# mesela bir for döngüsünde sys.argv listesi çağıralım ve bu liste komut satırına girilen tüm stringleri u-
# zunluğuyla beraber yazdırsın. yalnız şuna dikkat; sys.argv listeleri her zaman programın adıyla başlıyor
# çünkü yazdığımız ilk string hep programın adı. bu yüzden list slicing ile stringi 1. indeksten itibaren al-
# malıyız (yani sys.argv[1:])
for string in sys.argv[1:]:
    print(f"{string} stringi, tam olarak {len(string)} adet karakterden oluşmaktadır.")