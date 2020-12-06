print(4 + 2)
print(4 - 2)
print(4 * 2)
# 4 işlem normal şekilde oluyor zaten. pythonda tamsayılar ve ondalıklı sayılar iki fark-
# veri türü olmasına karşın bu iki verinin bir işlemde operant olarak kullanılması pyth-
# onda geçerli bir işlemdir ve tam sayı da ondalıklı bir sayıya çevrilerek işlem gerçek-
# leştirilir.
print(4 + 6) # burada obje "tamsayı"dır
print(4.5 + 6.2) # burada ise obje "ondalıklı sayı"dır
print(5 + 2.6) # burada objelerden biri tam diğeri ondalıklı sayı olmasında karşın çıktı,
# ondalıklı sayıdır. 10. ve 9. satırdakiler gibi işlermlerde sonuç tamsayı olsa dahi çık-
# tı ondalıklı sayı olarak (x.0) verilir.

print(5 / 2) # aynı kurallar bölme işlemi için de geçerli olmasına karşın, bölme işlemi-
print(4 / 2) # nin çıktısı her zaman ondalıklıdır.

print(14 / 3) # bölme işleminin bir başka şekli de "//" operatörüdür. bu operatör kulla-
print(14 // 3) # nıldığında "/" operatöründeki gibi ondalıklı bir çıktı alınmaz, çıktı
# tamsayı olarak alınır. tamsayı olarak alınan çıktı gerçek sonucun yuvarlanması ile el-
# de edilen tamsayı değil, gerçek sonucun ondalığının çıkarılmasıyla elde edilen tam sa-
# dır. bu işleme "floor division" (kat bölme) denir.
print(-13 / 4) # sonuç negatif olduğunda floor division çıktısı aşağı "yuvarlanmış" şe-
print(-13 // 4) # kilde verildiği için her zaman tam kısmın bir eksiği ("/" ile sonuç
# -x.y ise floor division ile sonuç -(x+1) olmaktadır.
print(13 % 4) # bölme ile ilgili başka bir operasyon da "modulo" (reminder, mod) operas-
print(-13 % 4) # yonudur. "%" operatörü kullanıldığında ilk sayının ikinci sayıya bölün
# mesiyle kalan sayıyı verir. modulo'su alınan sayı negatif alındığında sonuç, ikinci
# sayıya tamamlayan sayıyı verir. söz gelimi a=(k*b)+m olsun. bu durumda (a % b)=m olur.
# a sayısının nefatifi için (-a % b)=(b-m) olur.

print(5 ** 3) # üstel işlemler genellikle hesap makinelerinde kullanılanın aksine ^ ope-
# ratörü ile değil ** operatörüyle gerçekleştirilir.

print("lol" + "o") # matematiksel operasyonlardan bazıları (toplama ve çarpma) string ti-
print("lo" * 10) # pindeki veriler ile de işlem yapabilmektedir. "+" operatörü iki strin-
# gi birbirine bağlarken "*" operatörü, beraberindeki stringi verilen sayı kadar tekrar
# ederek birbirine bağlar
# iki stingi birbirine bağlamak için "+" operatörü elzem değildir fakat anlaşılabilirlik
# açısından daha çok tercih edilir.
print("lol" "o") # print("lol", "o") ile aynı şey değil!!
print("lol", "o")

# ----
print()
# format fonksiyonu, stringlerdeki format metodundan farklı olarak kendisine verilen bir
# numerik objeyi, belirtilen formatta bir string haline getiren bir fonksiyondur ve sayı-
# ların belli formatta çıktısını elde etmek için kullanılır, elde edilen çıktılar string
# olduklarından matematiksel operasyonlara tabii tutulamazlar. format fonksiyonu iki ar-
# güman kabul eder. bunlardan ilki, formata uydurulacak sayı, ikincisi ise istenilen for-
# mattır. python pek çok farklı format seçeneği sunmaktadır ve bunlar pythonun dökümantas-
# yonunda sunulmuştur. bir kaç örneği inceleyelim:

sayı = 0.123456789
# ondalıklı bir sayı olarak çıktı almak için "f" kullanılır.
print(format(sayı, "f")) # default olarak virgülden sonra 7 basamağı alır fakat f opsiyonu
# değiştirilerek bunu değiştirmek mümkündür. seçeneklerin önüne getirilen .sayı ifadeleri
# ondalıklı basamak sayısını belirtmek için kullanılır:
print(format(sayı, ".2f"))
print(type(format(sayı, ".2f"))) # format fonksiyonunda unutulmaması gereken, elde edilen 
# çıktının bir string olduğudur.

# bir sayıyı yüzde şeklinde yazmak için de % seçeneğinden faydalanılır:
print(format(0.35, "%"))
print(format(0.65, ".2%"))

# uzun sayıları virgül ile bindeliklerinden ayırmak için (1,234,567 şeklinde) "," opsiyonu
# kullanılır
print(format(12345678, ","))