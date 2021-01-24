import random
import copy

# shuffle fonksiyonu teorik olarak sıralı, iterable ve değiştirilebilir objelerin elemanlarını karıştırır fakat bu koşullara uyan tek python objesi liste-
# ler olduğu için shuffle fonksiyonu da yalnızca listeler üzerinde çalıştırılır. shuffle fonksiyonu, listenin karıştırılmış bir halini return etmez, None
# return eder ve listenin kendisini değiştirir.
oyuncular = ["Egemen", "Gökhan", "Oğuz", "Berkcan"]
print(oyuncular)
# şimdi listemizi shuffle'layalım
print(random.shuffle(oyuncular)) # görüldüğü gibi çıktı None
print(oyuncular) # görüldüğü gibi doğrudan oyuncular listesini yazdırıyoruz ve karşımıza öncekinden farklı sırada bir liste çıkıyor.

print()

# shuffle fonksiyonu listenin kendisini değiştirir. bu sebeple listenin orijinal halini korumamız gereken durumlarda listenin klonlanması gerekir.
# bunun için daha önce bahsettiğimiz bir kaç yöntem vardı, bunları hatırlamakta fayda var:
sayılar = [1, 2, 3, 4, 5]
# 1- ilk yöntemimiz indeks yöntemi. bir listeyi başından sonuna indeklesiğimizde listenin klonunu elde ederiz;
klon = sayılar[:]
# 2- ikinci metodumuz ise "copy" metodu. copy metodu da üzerinde çalıştırdığı objenin aynısını return eder;
klon = sayılar.copy()
# 3- bir diğer yöntem de copy modülü içersindeki copy fonksiyonudur. copy fonksiyonu da argüman olarak verilen objebin klonunu oluşturur;
klon = copy.copy(sayılar)
# 3.5- bu 3 yöntemin de listeleri yüzeysel olarak klonladığını unutmamalıyız. iç içe listeler gibi daha karmaşık veri yapılarını sadece bir basamak de-
# ğiştirirler yani liste içinde listeler içeren bir objenin tam kopyasını oluşturmazlar dolayısıyla istenmeyen verilerin manüple olmasına sebep olabilir-
# ler. bu gibi durumlarda, iç içe objelerin kopyalanmasında, copy modülündeki deepcopy fonksiyonundan faydalanılır. deepcopy, objeleri kopyalarken
# objelerin elemanlarını da ayrı olarak kopyalar.
klon = copy.deepcopy(sayılar)

random.shuffle(klon)
print(sayılar)
print(klon)