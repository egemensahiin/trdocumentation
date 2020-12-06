# __bool__ metodu, kendi oluşturduğumuz objelerin rölatif doğruluğunu (doğrumsuluk, truthieness) tanımlamak yani bir boolean contextindeki (mesela if
# veya while ifadelerinde) davranışlarını belirlemek için kullanılır.
class DuyguDurum():
    def __init__(self, optimizm, pesimizm):
        self.optimizm = optimizm
        self.pesimizm = pesimizm
    def __bool__(self):
        return self.optimizm > self.pesimizm # yani optimizm pesimizmden büyük olduğunda true çıktısı verecek. bu da bizim rölatif doğruluğumuz oluyor.

duygu_durumum = DuyguDurum(optimizm = 60, pesimizm = 75)
print(bool(duygu_durumum))
# bunu koşullu ifadelerde de kullanabiliriz:
if duygu_durumum:
    print("Böyle devam")
else:
    print("Üzülme knk niye üzülüyon :(")