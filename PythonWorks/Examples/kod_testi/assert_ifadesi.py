# assert, test kodlarının yazımı için mantıksal temel oluşturan bir bir kavramdır. en basit tabiriyle "assertion", bir doğrulama veya bir şeyin doğru, isa-
# betli, beklendiği gibi olduğuna dair bir beklentidir. assert keywordünü takip eden ilk argüman boolean doğrusu olduğunda, assert keywordü None çıktısı
# verir ve basitçe hiçbir şey yapmaz. fakat ilk argüman doğru değilse yani belirtilen beklenti karşılanmamışsa AssertionError yükselir ve eğer verilmişse
# virgülden sonraki ikinci argüman hata mesajı olarak terminalde okunur.
def ekle(x, y):
    assert isinstance(x, int) and isinstance(y, int), "Her iki argüman da tamsayı olmalıdır."
        # |---- burası ilk argüman virgüle kadar ---|
    return x + y

print(ekle(3, 4)) # burada bir sıkıntı yok. assert koşulu karşılandığı için None veriyor ve olduğu gibi devam ediyor.
print(ekle(3, "4")) # burada ise assert koşulu karşılanmıyor. normalde ValueError alınacakken AssertError alınıyor. bunun sebebi ise AssertError'un,
# ValueError'dan daha önce gelmesi. assert koşulu karşılanmadığı ve hata yükseldiği için program hiçbir zaman 3 sayısını ve "4" stringini toplamaya ça-
# lışmıyor ve ValueError alınmıyor. yani bu satırda "return x + y" ifadesine ulaşılmıyor.