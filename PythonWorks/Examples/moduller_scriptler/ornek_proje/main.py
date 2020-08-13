# import keywordü, modülleri olduğu gibi 'paketleri' import etmek için de kullanılır. pythonda paket, modül-
# lerin veya diğer bir deyişle organize python dosyalarının oluşturduğu klasörlere denir:
import initsizozellikler # bu haliyle paketi çağırmış olsak da şu an içersindeki modüllere erişemeyiz. bunun
# için paket içersindeki modülleri paketin bir niteliği farz ederek "." syntaxıyla import etmemiz gerekir:
import initsizozellikler.copyleft
print(initsizozellikler.copyleft.copyleft_tarihi)
print("-----------------------")
# genellikle bir klasörün paket olarak deklare edilmesi için içersinde dundar init (__init__.py) dosyası o-
# luşturulur. bu dosyalar çoğunlukla doğrudan script olarak çalıştırılan dosyalar değillerdir, bunun yeri-
# ne python, söz konusu paketi import ettiğimizde bu dosyayı otomatik olarak çalıştırır.
# görüldüğü üzere oluşturduğumuz örnek proje klasöründe bir özellikler klasörünü, içersine bir __init__.py
# dosyası oluşturarak bir paket haline getirdik. hatta onun da içine bir alt özellikler klasörü oluşturarak
# onu da __init__.py ile bir paket yaptık.
# import keywordü ile bir paketi çağırabiliriz:
# import ozellikler # sağda gördüğümüz üzere, ozellikler paketini çağırdığımızda python klasörde bir __init__
# # dosyası arıyor ve bu dosyayı main.py içerisinde çalıştırıyor.
# # bu şekliyle ozellikler paketini import etmiş oluyoruz fakat copyright modülünü henüz import etmedik. bu
# # modül ozellikler paketinde olduğu için bunu özelliklerin bir niteliği olarak yani "." ile import ediyoruz:
# ---------------------------------------------------
# import ozellikler.copyright # şimdi copyright içersindeki bir niteliği mesela copyright_tarihi değişkenini
# # çağırabiliriz: --->> sağdaki çıktıda gördüğümüz gibi paketi değilde bir niteliğini çağırdığımızda da init
# #                      dosyası çalışıyor.
# print(ozellikler.copyright.copyright_tarihi)
# ---------------------------------------------------
# # şimdi bir seviye daha derine inip bu sefer altozellikler paketini import edelim. altozellikler paketi, o-
# # zellikler paketi içinde yer alır, yani ozellikler paketinin bir niteliğidir. bu sebeple tıpkı copyright mo-
# # dülünde olduğu gibi altozellikler paketi de "." syntaxıyla çağrılır:
# import ozellikler.altozellikler # yine bu satır alt özellikler paketini çağırmak için yeterlidir ve bunu,
# # sağdaki çıktıdan doğrulayabiliriz. paketten modül import ederken olduğu gibi paket içindeki bir paketi im-
# # port ettiğimizde de, önce üst paket (ozellikler) içersindeki init dosyası çalışır. ardından yine init dos-
# # yası bulunan bir paket import ettiğimiz için bu paketin de init dosyası çalışır. bu sebeple sağda, iki dos-
# # yaya ait çıktıları da görmek mümkündür.
# ---------------------------------------------------
# # aynı şekilde "." syntaxını kullanarak altpaketten de modül import edebiliriz:
# import ozellikler.altozellikler.calculator
# print(ozellikler.altozellikler.calculator.add(3, 5))
# ---------------------------------------------------
# # fakat from keywordünü de işin içine katarak daha temiz bir kod elde edebiliriz. from keywordüyle paketten
# # alt paket veya doğrudan alt paketten nitelik import edebiliriz fakat dikkat etmemiz gereken bir husus;
# # from paket import altpaket.modül syntaxı geçersizdir. bunun yerine from paket.altpaket import modül syn-
# # taxı kullanılmalıdır.
# from ozellikler.altozellikler import calculator
# # yine from keywordü kullandığımızda da her iki init dosyası da çalışacaktır.
# # bu durumda mesela copyright modülünü de import edersek, ozellikler paketindeki init dosyası iki defa çalış-
# # maz. bir scriptte bir pakete kaç defa atıf yapılırsa yapılsın, söz konusu paketin init dosyası yalnız bir
# # defa çalışır.
# import ozellikler.copyright
# print(calculator.add(3, 5))
# print(ozellikler.copyright.copyright_tarihi)
# ---------------------------------------------------
# programımızın özelliklerine göre istediğimiz gibi from ve import keywordlerini kullanabiliriz. mesela yal-
# nızca alt paketteki bir modül içersinden bir fonksiyonu da import edebiliriz:
from ozellikler.altozellikler.calculator import subtract
print(subtract(3, 5))