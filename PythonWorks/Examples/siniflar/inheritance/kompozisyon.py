# pythonda alt-üst sınıf ilişkisi, daha önce de bahsettiğimiz gibi kullanımı tartışmalı bir pratik. buna alternatif olarak kullanılan fikir ise kompozisyon 
# konsepti. inheritance, bir alt-üst sınıf ilişkisini modellemede kullanılırken kompozisyon ilişkilerin varlığını modellemektedir. yani birbirinin alt-üst 
# sınıfları olan objeler değil de birbirini içeren ayrı objelerden oluşan bir kod modellemesi olarak düşünmek yanlış olmaz. özellikle çoklu inheritance ya-
# zımlarında gördüğümüz gibi, miras almaya dayalı sınıf tanımlamaları, kodun okunurluğunu azaltmakla kalmıyor, koda yapılacak eklemelerde-çıkarmalarda-gün-
# cellemelerde programın istendiği gibi çalışmama olasılığını da arttırıyor. öte yandan kompozisyon yaklaşımı, oluşturacağımız sınıfların kendi başına izo-
# le edilebilecek özelliklerinin ayrı sınıflar olarak kodlanmasına ve daha sonra başka sınıfların gövdesinde refere edilmesine dayandığından hem kodun oku-
# nabilirliği iyileşiyor hem de bir sınıf için yapacağımız güncellemeler programın stabilitesini etkilememiş oluyor.
# kağıt-çanta-avukat örneği oluşturup kompozisyon mantığını irdeleyelim. miras alma-verme ilişkisindeki alt-üst ilişkisinin aksine kompozisyonda oluşturaca-
# ğımız sınıflar birbirlerinin "tip"indeki sınıflar değil, birbirlerinin içinde bulunabilen sınıflar. sözgelimi çanta içersindeki kağıtlar veya avukatın ta-
# şıdığı çanta gibi. en dipten kodumuza başlayalım:
class Kağıt():
    def __init__(self, yazı, dosya_no):
        self.yazı = yazı
        self.dosya_no = dosya_no

class Çanta():
    def __init__(self, fiyat):
        self.fiyat = fiyat
        self.kağıtlar = []
    def kağıt_ekle(self, kağıt):
        self.kağıtlar.append(kağıt)
    def notlara_bak(self):
        return [kağıt.yazı for kağıt in self.kağıtlar]

class Avukat():
    def __init__(self, isim, çanta):
        self.isim = isim
        self.çanta = çanta
    def not_yaz(self, yazı, dosya_no):
        self.çanta.kağıtlar.append(Kağıt(yazı, dosya_no))
    def notlara_bak(self):
        return self.çanta.notlara_bak()

# görüldüğü gibi kod gayet temiz, karmaşık hiyerarşiler yok, birbirinin içine geçmiş sınıflar yok. olayın mantığına uygun şekilde; çanta, çantayı taşıyan bir
# avukat ve çanta içersindeki kağıtlar var. mesela kağıtları bir liste değil de bir sözlük şeklinde not etmek istersek hiç problem değil, notlara bak fonksi-
# yonunu değiştirsek yeter.
ucuz_çanta = Çanta(55.95)
fatih = Avukat(
    isim = "Fatih",
    çanta = ucuz_çanta
    )
fatih.not_yaz("Hakim Bey müvekkilim suçsuzdur.", "AB-2341")
fatih.not_yaz("Nası şahit var ya??", "AB-2341")
print(fatih.notlara_bak())
# not yazma, notlara bakma işi Kağıt objesini gerektirir fakat işleri yapan Çanta objesidir. bizim çanta objesini kullanmak için eriştiğimiz arayüz ise Avu-
# kat objesidir. bu da kompozisyona güzel bir örnek. tek bir obje altında yapabileceğimiz işleri, farklı işlevselliklere bölüp işi kolaylaştırmış olduk.
