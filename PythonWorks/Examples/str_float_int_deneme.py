# int, float ve str, input olarak verilen objenin type'ını değiştirmek için (type con-
# version) kullanılan fonksiyonlardır.
print(int(3.14)) # çıktı olarak 3 alınır çünkü int fonksiyonu, içersindeki objeyi int
# tipinde bir objeye çevirir. bunu yaparken sayıyı yuvarlamaz, ondalık kısmı atar.
print(int(3.75)) # 3
print(int("3")) #int fonksiyonu kullanarak string türünde bir veri integer türüne çev-
# rilmek istendiğinde girdi olarak sadece sayısal stringler kullanılmalıdır aksi hal-
# valueerror verilir. çıktıya bakıldığında bir değişim görülmemesi normaldir. değişimi
# gözlemlemek için kıyaslama operasyonlarıyla inceleyelim:
print(int("3") == "3") # False olarak çıkar çünkü int("3"), kıyaslandığı "3" gibi bir
# string değil bir integer'dir.
print(int("3") == 3) # True
# veya type fonksiyonu ile de değişim gözlenebilir
print(type("3")) # <class 'str'>
print(type(int("3"))) # <class 'int'>
print(int(True)) # boolean tipindeki verilerin de integer tipte karşılıkları vardır.
print(int(False)) # int(True) 1 değerini verirken int(False) ise 0'a eşittir.

# float fonksiyonu ise kendisine verilen tamsayıyı ondalıklı hale getirir. bunun için
# a sayısını a.0 şekline çevirir. aslında bu işlemi python, bir tam bir ondalıklı sa-
# yıyı topladığımızda kendisi yapmaktadır. mesela 5 + 6.1 işlemini gerçekleştirirken
# önce 5'i ondalıklı hale getirir ardından 5.0 ile 6.1'i toplar.
print(float(5)) # 5.0
print(float("5"))
print(float("3.14")) # ayrıca string tipindeki ondalıklı sayılar da float fonksiyonu
# ile float tipine çevrilir. yine değişim çıktıda farkedilmese de type fonksiyonu ile
# kontrol edilebilir.
print(float(True)) # boolean tipindeki objeler float fonksiyonu için de valid'dir ve
print(float(False)) # 1.0 ile 0.0 sayılarını verirler.

# str fonksiyonu ise float ve int gibi obje türünü değiştirerek sting yapar.
print(str(5))
print(str(10.2))
# değişimi gözlemek için type fonksiyonu kullanılabileceği gibi "+" operasyonundan da
# faydalanılabilir. int ve float tipindeki objeler "+" işlemi altında toplanırken str
# tipindeki veriler bağlanır.
print(str(5) + str(10))
# eğer str fonksiyonu altında bir operasyon varsa önce operasyon işlenir ardından str
# fonksiyonu bu operasyonun sonucuna uygulanır
print(str(5 + 10)) # çıktısı "5 + 10" değil "15" tir.
# str fonksiyonu içersine boolean tipindeki objeler de alınabilir
print(str(True)) # bir boolean değildir, doğruluk yanlışlık belirtmez, bir stringdir
# "True"
print(type(str(True))) # <class 'str'>
print(str(True) == True) # False