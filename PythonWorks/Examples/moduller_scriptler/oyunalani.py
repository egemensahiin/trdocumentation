# pythonun her dosyaya atadığı dundar name denilen bir değişken vardır ve __name__ ile çağırılır (dundar gali-
# ba __'ye deniyor). eğer import edilen bir modülün __name__ niteliği çağırılırsa, modülün adı çıktı olarak a-
# lınır:
import math
import calculator1
# import math, calculator1 da mümkündür ama tercih edilmez.
print(math.__name__)
print(calculator1.__name__)
# fakat mevcut script için __name__ değişkenini çağırdığımızda çıktının scriptin adı değil dundar main denilen
# __main__ olduğunu görürüz:
print(__name__)

# her dosyanın __name__ çıktısı kendi içinde __main__, fakat başka dosyalarda dosya adıdır. örneğin calculator1
# modülünde __name__'i yazdıralım. görüldüğü üzere calculator1.py ln 19'da çağırılan __name__, orada __main__
# çıktısını verirken burada (ilk çıktı importtan gelen) calculator1 çıktısını verdi.
# __name__ değişkeni sayesinde bir programın çalıştığı esnada modül olarak mı script olarak mı çalıştığını
# test edebilir ve koşullu ifadelerle program yalnızca script veya yalnızca modül olarak çalıştığında işle-
# yecek bloklar yazabiliriz. örnek için goto calculator1.py ln 20-23:
# görüldüğü gibi 21deki koşul, oyunalani.py içersinde sağlanmadığı için 22 ve 23. satırlardaki print'ler yal-
# nızca calculator1.py içersinde yazılmıştır.