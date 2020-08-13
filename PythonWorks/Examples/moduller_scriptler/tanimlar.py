# -- Modüller ve Scriptler: teknik olarak modül, .py uzantısıyla biten herhangi bir python dosyasıdır. fakat
# python programcıları arasında modül ve script arasında nüans farklılıkları bulunmaktadır; script, direkt o-
# larak çalıştırılan bir pyhton dosyasını tanımlarken modül, diğer python dosyaları veya scriptlerde kullanı-
# python dosyalarını tanımlar. modüllerin kullanılmasının en önemli avantajı, mantığın spesifik bir dosyaya
# izole edilmesidir; böylece programcıya, daha sonra bu mantığı programın farklı yerlerinde kullanma imkanı
# sunar.
# her modül, deklare edilen isimler (names) için bir isim alanı (namespace) yaratır. bir isim alanı, dosyada-
# ki isimlerin kaçmasını önleyen bir konteyner veya ismi çevreleyen bir duvar gibi düşünülebilir. burada i-
# sim olarak atfedilen, dosyada tanımlanan her türlü tanımlayıcıdır; değişkenler, sabitler, fonksiyonlar vs.
# isim alanları da bunları yalnızca bu dosya içersinde izole eden duvarlar gibidir. isim alanlarına örnek
# olarak fonksiyon gövdeleri de verilebilir. fonksiyon gövdeleri, içersinde tanımlanan lokal değişkenleri vs
# içersinde barındırır ve bunların fonksiyon dışarsına çıkmasını önler.
# diğer her şey gibi modüller de birer objedir ve aynı isim alanını paylaşan (yani aynı dosya içersinde ta-
# nımlı) isimlerin bir koleksiyonunu temsil ederler.
# modül içersindeki isimlere nitelik (attribute) denmektedir. bir modülün başka bir dosyaya çağrılması için
# import keywordü kullanılır.
# örnek olarak ilk dosyalar, calculator.py ve my_program.py