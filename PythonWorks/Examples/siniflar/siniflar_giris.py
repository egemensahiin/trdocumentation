# programlar karmaşıklaştıkça, program mantığı genişledikçe kullanılan dilin yerel objeleriyle çalışmak zorlaşır. bu sebeple kendi python objelerimizi,
# kendi veri yapılarımızı oluşturma gerekliliği doğar. obje odaklı programlama, bir yazılım programını birbiriyle etkileşen ve birbiriyle konuşan obje-
# lerin bir koleksiyonu olarak gören kod organizasyonu ve tasarımı için kullanılan paradigmadır. bu da objenin ne olduğu sorusunu doğurur. obje, veri
# ve "davranış"ın konteynırıdır ve bu davranış, söz konusu veri ile etkileşmektedir.
#
# objelerle ilgili bilmemiz gereken en temel şey, nitelikler (attributes) ve metodlardır. bahsettiğimiz üzere objeler veri konteynırlarıdır ve nitelik-
# lerle metodları içerirler. nitelikler, internal veriyi ve/veya objenin durumunu tanımlarlar ve temelde objeye ait değişkenler olarak düşünülebilirler.
# objelerin birbiriyle iletişimini sağlayansa metodlardır ve objeye ait fonksiyonlar gibi düşünülebilirler; objeye gönderilen bir komut, yönlendirme ve-
# ya mesajdır. bir metod, objenin nitelikleriyle etkileşebilir ve modifiye edebilir, dolayısıyla da objenin durumunu değiştirebilir.
# 
# sınıflar (classes) ise pythonda yeni bir obje tipi tanımlamak için kullanılan taslaklardır. bir sınıf, objeyi meydana getiren tüm nitelikleri ve me-
# todları tanımlar. örnek (instance), bir sınıftan oluşturulan objedir. bir sınıftan obje oluşması olayı ise örnekleme (instantiation) olarak bilinir.
# aynı sınıftan oluşturulan objeler birbirinden bağımsızdırlar. aynı şemadan oluşturulurlar, aynı düzendedirler, aynı özelliklere ve işlevlere sahip-
# tirler fakat farklı değerlerde, farklı durumlardadırlar ve birbirlerinden bağımsızdırlar. 
#
# sınıf oluşturmak için "class" keywordü kullanılır. syntaxı şu şekildedir: class SınıfAdı(): ve ardından fonksiyon bloklarına benzer bir blok yazılır
# ki bu blok, sınıfın kendisine ait bir isim alanı oluşturur ve burada bu sınıfa tanımlanan metod ve nitelikler, sınıfın kapsamındadır. sınıfların i-
# simlendrimesinde bir kısıtlama olmamasına karşın python topluluğunda genel kullanımda sınıflar camel case veya pascal case denilen şekilde isimlen-
# dirilir. bu isimlendirmede boşluk veya karakter harici semboller kullanılmaz ve her kelimenin ilk harfi büyük harfle yazılır. ayrıca sınıfların her
# çağırımı, bağımsız tek bir objeyi temsil ettiği için çoğunlukla tekil isimlendirilirler.
class Kişi(): # python2'de bu parantezler içine "object" yazılıyordu fakat python3te böyle bir syntax yok. eski kodlarda karşılaşılabilir.
    pass # pass sadece boş sınıftan hata almayalım diye
class VeriBağlantısı():
    pass
egemen = Kişi() # sınıflar, fonksiyonlara benzer şekilde, parantezlerle çağırılırlar. parantezlerin içine daha sonra geleceğiz.
gülzeynep = Kişi()
print(egemen)
print(gülzeynep) # bu çıktılarda gördüğümüz gibi objelerimiz aynı sınıfa ait hatta bu örnekte teorik olarak da aynı olmalarına karşın, hafızada farklı
# noktalarda tutulan bağımsız objelerdir.
dc = VeriBağlantısı()
print(dc)