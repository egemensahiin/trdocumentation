# stringler immutable yani değişmez yapıda objelerdir. fakat format metodunu kul-
# lanarak bunları dinamik hale getirmemiz mümkündür. format metodunu kullanabilmek
# için stringe dinamik kısımlar tanımlamamız gerekir. bunun için {} kullanılır.
# format metoduyla, stringde tanımladığımız {} içersine substring'ler atayarak
# stringi dinamik hale getiririz.
# degisken = "{} ornek {} string {}" şeklinde bir string tanımlayıp bunu format
# metoduyla degisken.formak("substr1", "substr2", "substr3") şeklinde çağırdığı-
# mızda elde ettiğimiz çıktı "substr1 ornek substr2 string substr3" olur.
sonuc = "{} isimli etken madde {} için kullanılmakta olup en önemli yan etkisi,\
 {} olarak görülmüştür." 
# şeklinde tanımladığımız bir stringi
print(sonuc) # olduğu gibi çağırırsak {}'ler karakter olarak okunur.
print(sonuc.format("Empagliflozin", "diyabet", "sistit")) # şeklinde değişkeni çağır-
# dığımızda, metod içersine yazdığımız sırayla substringleri atayarak yeni bir
# string oluşturur.
print(sonuc.format("Empagliflozin", "diyabet", "sistit", "saçma bi şey")) # şeklinde
# değişkene tanımlanandan daha fazla substring girilirse program basitçe fazla o-
# lanları okumaz.
#print(sonuc.format("Empagliflozin", "diyabet")) # fakat bu şekilde eksik değer gi-
# rildiği takdirde IndexError ile karşılaşılır.

# stringi tanımlarken {} içersine indeks numaraları yazabiliriz. default olarak
# format metodu içersine yazdığımız substringler de aynı sıradadır. 0, 1, 2 vs.
# indeks numaralarıyla ilerler. stringi tanımlarken bu sıralama default olarak
# metoddakiyle aynıdır (0, 1, 2..)
sonuc = "{0} isimli etken madde {1} için kullanılmakta olup en\
 önemli yan etkisi, {2} olarak görülmüştür." 
print(sonuc.format("Empagliflozin", "diyabet", "sistit"))
# fakat {} içersine özel olarak indeks numaralarını belirterek bunu değiştire
# biliriz.
sonuc = "{1} isimli etken madde {2} için kullanılmakta olup en\
 önemli yan etkisi, {0} olarak görülmüştür." 
print(sonuc.format("Empagliflozin", "diyabet", "sistit"))
# indeks numarasının 0dan başladığı unutulmamalıdır. aşağıdaki gibi bir değişken
# ve string tanımladığımızda ve format metoduyla çalıştırdığımızda 0 indeks numa-
# ralı ilk substring okunmaz, 3 indeks numaralı 4. substring okunur.
sonuc = "{1} isimli etken madde {2} için kullanılmakta olup en\
 önemli yan etkisi, {3} olarak görülmüştür." 
print(sonuc.format("Empagliflozin", "diyabet", "sistit", "akjfhajdf"))

# daha uzun programlarda okunabilirlik ve anlaşılabilirlik açısından string tanım-
# lanırken {} içersine isim de yazılabilir. bu durumda substringler tanımlanırken
# bu isimlerle (isim = "substr") tanımlanır.
sonuc = "{ilaç} isimli etken madde {endikasyon} için kullanılmakta olup en\
 önemli yan etkisi, {yan_etki} olarak görülmüştür."
print(sonuc.format(ilaç = "Empagliflozin", endikasyon = "diyabet", 
yan_etki = "sistit"))

# # bu şekilde mesela eczacılıkla ilgili veri girip çıktı alabildiğimiz bir program
# # yazabiliriz.
# bilgi = "{ilaç} isimli etken madde {endikasyon} için kullanılmakta olup en\
#  önemli yan etkisi, {yan_etki} olarak görülmüştür."
# ilaç = input("İlaç adı giriniz: ")
# endikasyon = input("Endikasyonunu giriniz: ")
# yan_etki = input("En önemli yan ekisini yazınız: ")
# print(bilgi.format(ilaç = ilaç, endikasyon = endikasyon, yan_etki = yan_etki))
# # bundan öncekileri çalıştırmak için öncekilere meta+u, buraya meta+c yap!

print()

# format metodu yerine daha az kod yazarak değişkenleri stringler içersine yine {} kul-
# lanarak tanımlanabilir. bunun için stringi tanımlarken başına "f" veya "F" ibaresi
# kullanarak stringi "formatted string"e çevirebiliriz. yalnızca değişken değil, forma-
# tted stringlerde {} arasına yazılan matematiksel ifadelerin sonuçları, fonksiyonların
# çıktıları vs. de string olarak çıkar. yani formatted olarak tanımlanmış bir string i-
# çersindeki {}, içeriyi normal bir python programı gibi işler, çıktısını ise substing
# olarak stringe katar.
ilaç = "Empagliflozin"
endikasyon = "diyabet"
yan_etki = "sistit"
# "{ilaç} isimli etken madde {endikasyon} için kullanılmakta olup en önemli yan etkisi, 
# {yan_etki} olarak görülmüştür." stringini yukarıdaki değişkenlerle yazarken format 
# metodunu kullanırsak
# print("{ilaç} isimli etken madde {endikasyon} için kullanılmakta olup en önemli yan 
# etkisi, {yan_etki} olarak görülmüştür.".format(ilaç = ilaç, endikasyon = endikasyon
# yan_etki = yan_etki)) şeklinde uzunca bir print fonksiyonu kullanmamız gerekir. Bunun
# yerine formatted string yöntemini kullandığımızda string içersindeki {}lere doğrudan
# değişkenleri tanımlayabiliriz.
sonuc = f"{ilaç} isimli etken madde {endikasyon} için kullanılmakta olup en önemli yan \
etkisi, {yan_etki} olarak görülmüştür."
print(sonuc)
# {} içersinde matematiksel işlemler gibi operasyonlar ve hatta fonksiyonlar da olabi-
# lir.
print(F"5 ve 4'ün toplamı {5 + 4} yapar.")

def eşit_mi(a, b):
    return a == b
print(f"6 ve 7 birbirine eşit mi? {eşit_mi(6, 7)}")