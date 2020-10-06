# global keywordünün tamamlayıcısı bir başka keyword de nonlocal keywordüdür. global keywrodü, bir ismi lokal kapsamdan global kapsama taşırken nonlo
# -cal keywordü iç içe fonksiyonlarda kullanılır ve çevrelenen fonksiyondaki yani lokal kapsamdaki bir ismi, çevreleyen fonksiyon kapsamına taşır.
def dış_fonksiyon():
    x = 10
    def iç_fonksiyon():
        x = 20
    iç_fonksiyon()
    return x
print(dış_fonksiyon()) # bu fonksiyonda x değeri olarak 10 değerini alırız çünkü dış_fonksiyon gövdesinde iç_fonksiyonu çalıştırmış olsak da x ismi
# lokal ve çevreleyen fonksiyon kapsamında olmak üzere iki farklı değer alır lokal isim, çevreleyen fonksiyon kapsamında tanınmadığı için dış fonksiyon-
# dan return edilen, çevreleyen fonksiyon kapsamındaki x ismi yani 10 olur.

def dış_fonksiyon():
    x = 10
    def iç_fonksiyon():
        nonlocal x
        x = 20
    iç_fonksiyon()
    return x
print(dış_fonksiyon()) # bu sefer tanımladığımız fonksiyonda ise, 16. satırda kullandığımız nonlocal keywordü, iç fonksiyon içersinde bahsi geçen x is-
# minin lokal kapsamda değil, çevreleyen fonksiyon kapsamında olmasını sağlamaktadır. bu sebeple fonksiyon çalıştırıldığın 17. satır bu sefer lokal
# kapsamda değil, dış_fonksiyonun kapsamında çalışır ve x değişkeni 20 olarak tekrar yazıldıktan sonra return edilir.