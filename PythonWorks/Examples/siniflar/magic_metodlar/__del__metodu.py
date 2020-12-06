# hatırlanacağı üzere pythonda programlar sonlanırken "çöp toplama" olarak adlandırabileceğimiz (garbage collection) bir süreç gerçekleşir. __del__
# metodu, OBJEMİZ sonlandığında otomatik olarak çalışır. pythonda bir objenin çöp toplama sürecine girmesi için ya program sonlanır ve progeamdaki
# her şey ile beraber objemiz de hafızadan silinir ya da objemiz artık refere edilmez. pythonda refere edilmeyen objeler de çöp toplama sürecine
# girer yani objemizi atadığımız değişken artık o objeyi refere etmiyorsa, obje hafızadan silinir.
import time
class Garbage():
    def __del__(self):
        print("Bu benim son nefesim :/")

çöp = Garbage()
# bu aşamada kodumuzu çalıştırdığımızda, "Bu benim son nefesim :/" çıktısını görürüz. objemiz refere edilir, program sonlanmadan önce silinir ve
# silinmeden hemen önce __del__ metodu çalışır.
# bu konsepti daha iyi anlamak için time modülü içersindeki sleep fonksiyonundan faydalanabiliriz. bash scriptingde kullandığımız sleep programı
# ile aynı mantıkta çalışır.
# objemizin çöp olarak toplanması için referansını ortadan kaldıralım. bu amaçla çöp değişkenine başka bir obje atayalım:
çöp = ""
# şimdi programı 5 saniye uyutalım:
time.sleep(5)
# program uyandıktan sonra da bir çıktı versin ki programın bittiği yeri anlayalım:
print("Program sonlandı.")
# terminalde programı çalıştırdığımızda görebileceğimiz gibi; Garbage() objesi referansı ortadan kalktığı an yani 16. satır okunduğu an __del__
# metodu çalışıyor. ardından 18. satır çalışıyor ve program 5 saniye uyuyor. son olarak 20. satır çalışıyor ve program sonlanıyor.
# mesela yazdığımız sınıflar, geçici dosyalar oluşturduğunda ve program sonlanırken bunları silmek istediğimizde veya bir veritabanı bağlantısını
# program sonlanırken kesmek istediğimizde yani program veya sınıfımızın referansı sonlandığında bir şeyleri temizlemek istediğimizde __del__ me-
# todu oldukça kullanışlıdır.
