# hatırlanacağı üzere keyword argümanlar, bir fonksiyon çalıştırırken parametreyi ismiyle belirttiğimiz ar-
# gümanlardır. bir örnekle hatırlayalım:
def uzunluk_toplamı(a, b):
    print(len(a) + len(b))
uzunluk_toplamı("Merhaba", "Dünya") # bu şekilde çalıştırdığımızda fonksiyon parametreleri pozisyonel argü-
# manlar olarak çağrılmıştır (shell scripting'te olduğu gibi esasında)
uzunluk_toplamı(a = "Merhaba", b = "Dünya") # fakat fonksyionu böyle çağırdığımızda fonksiyon parametreleri,
# keyword argümanlar olarak çağrılmıştır. eğer fonksiyona, tanımında belirtilenden farklı bir keyword argü-
# manı verilirse veya beklenen argümanlardan biri verilmezse TypeError alınır.

print()

# fonksiyonlarda keyword argümanların kullanımıyla ilgili önemli bir konu da daha önce tuple'larda gördüğü-
# müz bir operatör olan *'tir. hatırlanacağı üzere bir fonksiyonda verilen pozisyonal argümanları bir tu-
# ple'da depolamak için *değişken syntaxını kullanıyorduk. python programcıları genellikle bu amaçla args
# değişkenini kullanmaktadır:
def pozisyonel_argümanlar(*args):
    return args
print(pozisyonel_argümanlar(5, "string", 3.14))
print(type(pozisyonel_argümanlar(5, "string", 3.14)))

print()

# benzer şekilde; bir fonksiyon tanımlanırken, ** operatörüyle bir argüman tanımladığımızda (ki python top-
# luluğunda genel kullanım olarak **kwargs kullanılır.) fonksiyonu çalıştırırken verdiğimiz keyword argü-
# manlar, bir sözlük şeklinde depolanır.
def keywordleri_toparla(**kwargs):
    return kwargs
print(keywordleri_toparla(kw1 = "ilk kwarg", kw2 = 3.14)) # görüldüğü gibi fonksiyondan çıkan kw-
# args değişkeni, fonksiyona verilen argümanların oluşturduğu bir sözlüktür:
print(type(keywordleri_toparla(kw1 = "ilk kwarg", kw2 = 3.14))) # <class 'dict'>
# fonksiyon içinde elbette normal sözlüklerde yaptığımız her şeyi yapabiliriz. mesela iterasyon:
def keywordleri_yazdır(**kwargs):
    for key, value in kwargs.items():
        print(f"Bu elemanda key '{key}', value ise '{value}'")

keywordleri_yazdır(a = "İlk", b = "ikinci", c = "Bu da üçüncü")

print()

# yine daha önce tuple'larda pozisyonel argümanları depolarken gördüğümüz gibi, **kwargs da başka argüman-
# larla birlikte kullanlılabilir ama farklı olarak, pozisyonel argümanların arasında veya öncesinde tanım-
# lanamaz, pozisyonel argümanlardan sonra tanımlanır:
def func(a, **kwargs):
    print(f"{a}'nın veri tipi {type(a)}")
    print(f"Kalan argumanlar ise bir sözlüktür: {kwargs}")
func("adald", b = "aldkad", c = 13213, d = 545, e = 48745, f = 3.14)

def bir_func_daha(a, b, **kwargs):
    print(f"{a}'nın veri tipi {type(a)}")
    print(f"{b}'nın veri tipi {type(b)}")
    print(f"Kalan argumanlar ise bir sözlüktür: {kwargs}")
bir_func_daha("adald", b = "aldkad", c = 13213, d = 545, e = 48745, f = 3.14)
# aynı şekilde pozisyonal argümanları, kwargs ile bir araya getirmek de mümkündür:
def args_ve_kwargs(a, b, *args, **kwargs):
    print(f"'{a}' ve '{b}' normal argümanlardır.")
    print(f"Kalan pozisyonel argümanlar {args} tupleında depolanmıştır.")
    print(f"Kalan keyword argümanlar ise {kwargs} sözlüğünde tutulmuştur.")
args_ve_kwargs(5, 3, 6, "asds", "string", 3.14, kw1 = 512, kw2 = "bu da string")

# mesela normal argümanları, pozisyonel argümanları ve keyword argümanları ayrı ayrı toplayan bir fonksiyon
# yazıp hepsini bir daha görelim:
def toplamlar(a, b, *args, **kwargs):
    print(f"Normal argümanların toplamı {a + b}")
    print(f"args tuple'ındaki pozisyonel argümanların toplamı {sum(args)}")
    dict_top = 0
    for sayı in kwargs.values():
        dict_top += sayı
    print(f"kwargs sözlüğündeki sayıların toplamı {dict_top}")
toplamlar(1, 2, 3, 5, 6, x = 7, y = 8, z = 9)

print()

# bununla alakalı bir başka syntaxta tuple veya listelerde olduğu gibi unpacking syntaxıdır. bunun için **
# kullanılır. keyword argümanlarla tanımlı bir fonksiyonu çalıştırırken bu syntaxtan faydalanılır ve fonk-
# siyon uygun bir **sözlük girdisiyle çalıştırıldığında, sözlükteki her bir eleman kwarg olarak okunur.
# sözlüğün key'lerinin, kwarg'larla aynı olması, (eğer fonksiyonda **kwarg tanımlı değilse) fazladan eleman
# olmaması önemlidir.
def feet_to_meter(feet, inch):
    tot_inch = (feet * 12) + inch
    meter    = tot_inch * 0.0254
    return meter
# mesela bu fonksiyonu doğrudan şu şekilde çalıştırabiliriz:
print(feet_to_meter(5, 11))
# veya fonksiyonun ihtiyaç duyduğu argümanların tanımlandığı bir sözlüğü unpack edebiliriz. bu duruma özel-
# likle dinamik olarak programda bir sözlüğün oluşturulduğu ve bu sözlükteki key-value çiftleri üzerinde bir
# fonksiyon çalıştırılmak istendiğinde başvurulur.
değerler = {
    "feet": 5,
    "inch": 11
}
print(feet_to_meter(**değerler)) # sözlük boşaltıldığında çıktısı ' "feet" = 5, "inch" = 11 ' olur. dola-
# yısıyla burada çalışan feet_to_meter(feet = 5, inch = 11)'dir.