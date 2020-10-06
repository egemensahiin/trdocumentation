# dosyalara yazmak için kullandığımız syntax, okumak için kullandığımız syntaxla aynıdır. eğer open fonksiyonuna ikinci bir argüman vermeden ça-
# lıştırırsak python dosyayı okumaya çalışır ve eğer dosya mevcut değilse FileNotFoundError alınır. fakat ikinci bir argüman olarak "w" verilir-
# se python dosyayı yazar. yani eğer dosya bulunamazsa oluşturur; eğer dosya hali hazırda varsa üstüne yazar.
dosya_adı = "yenidosya.txt"
with open(dosya_adı, "w") as dosya:
    # dosyaya yazmak istediğimiz stringleri write() metoduyla yazabiliriz. write metodu tek bir argüman kabul eder ve bu stringi dosyaya yazar.
    dosya.write("İlk dosya, ilk satır!")
    # dosyaya bir satır daha yazdığımızda 
    dosya.write("İkinci satır değil, ilk satır..")
    # alt satıra eklemek için write metoduyla yazılan stringin sonuna bir satır sonu (\n) eklenmelidir.
    dosya.write("Burası ilk satır.\n")
    dosya.write("Burası da ikinci satır.")
    # görüldüğü gibi bu durumda dosyamız iki satırdan oluşmaktadır.

# aynı blok içersinde write metodunu tekrar çağırdığımızda doyanın üzerine yazılmaz çünkü dosya hali hazırda açıktır fakat mevcut bir dosyayı
# "w" opsiyonuyla açıp write metodunu çalıştırdığımızda dosyaya bir string eklenmez, write metoduyla verilen string, dosyanın üstüne yazılır.
with open(dosya_adı, "w") as dosya:
    dosya.write("Üstüne yazıldı.")
    # görüldüğü üzere yukardaki string, dosyaya eklenmedi; dosyanın üzerine yazıldı.