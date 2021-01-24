# doctest, docstring'ler içersinde, kendine özgü bir syntaxla yazılan testleri çalıştırmamızı sağlayan bir modüldüt ve doctest stratejisi, test driven de-
# volopment (TDD) konseptinin temelini oluşturur. TDD konseptinde bir birim yazılırken (fonksiyon, sınıf, metod vs.) öncelikle bu birim için bir test se-
# naryosu yazılır, belirli bir yazımda birimden ne çıktı alınacağı hesaplanır ve test kodu olarak yazılır. kod da bu test uyarınca geliştirilir. doctest
# modülü de burada devreye girer. ">>>" syntaxıyla docstring'e yazılmış kodlar, doctest modülündeki testmode fonksiyonu ile çalıştırılır ve sonucun, bek-
# lentiye uygunluğu test edilir. testten beklenen sonuç, test edilecek kodun altına yazılır. eğer test edilen kodlardan beklenen sonuç alınırsa testmode
# fonksiyonu bir çıktı vermez fakat beklentiyi karşılamayan testler için bilgilendirici bir çıktı verir. bu çıktılar oldukça anlaşılırdır.

def sayilar_toplami(sayilar):
    """Bir listedeki sayıların toplamını return eder.
    >>> sayilar_toplami([1, 2, 3])
    6
    >>> sayilar_toplami([4, 5, 6])
    15
    """
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return sayi # mesela burada bir yazım yanlışı yaptık

if __name__ == "__main__": # testleri genellikle dosyanın kendisinde çalıştırmak isteriz, modül olarak her çağrıldığında test uygulamak ve çalıştırmak
    import doctest         # pratik bir yaklaşım değildir.
    doctest.testmod()
    # doctest testleri hata değildir, testlerden sonra yazılan kodlar çalışır.
    print("Çalışır çalışır...")

# çok faydalı ve mantıklı bir yöntem olsa da doctest modülü pek sık kullanılmaz çünkü beklentinin tam anlamıyla karşılanmasını bekler. söz gelimi beklen-
# ti koşulu olarak '' ile bir string aradıysak ama bu stringi "" içersinde elde ettiysek doctest bunların aynı string olmasını umursamaz, yazım farklı
# olduğu için testin başarısız olduğunu söyler. bu sebeple daha mantıksal test yapan unittest daha çok tercih edilir.