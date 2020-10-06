# fonksiyonlar listeler, tuplelar gibi iç içe (nested) olabilirler. yani bir fonksiyon, başka bir fonksiyonun gövdesinde bulunabilir. iç içe fonksiyon-
# lar sayesinde uzun gövdeli fonksiyonları, daha kısa parçalara bölebilir ve kodumuzu organize edebiliriz.
def litreden_bardak(litre):
    # şimdi bu fonksiyon içersinde başka bir fonksiyon tanımlayalım:
    def litreden_mililitre(lt):
        print(f"{lt} litre, mililitreye çevriliyor...")
        return lt * 1000
    # şimdi de mililitreden bardağa çevirelim
    def militreden_bardak(ml):
        print(f"{ml} mililitre, bardağa çevriliyor...")
        return ml / 200
    ml = litreden_mililitre(litre)
    bardak = militreden_bardak(ml)
    return bardak
print(litreden_bardak(5))
print(litreden_bardak(1))
# iç içe fonksiyonlarla ilgili göz önünde bulundurulması gereken önemli br detay, bir fonksiyon içinde tanımlanan diğer fonksiyon ve değişkenlerin o fon-
# ksiyonun isim alanı içinde enkapsüle olduğudur. yani "litreden_militreye()" fonksiyonu veya ml değişkeni, return edilmedikleri sürece fonksiyon dışın-
# da tanımsızdır.
# mililitreden_bardak(5)
# print(ml) # 20 veya 21. satırlar çalıştırıldığında NameError alınır.