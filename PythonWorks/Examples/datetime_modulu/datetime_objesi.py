# datetime objesi, aynı isimli modülde yer alan bir sınıftır ve tam bir zamanı yanı belirli bir tarih ve saati temsil eder.
from datetime import datetime as dt
# datetime objesi 7 argüman kabul eder fakat objenin örneklenmesi için gerekli olanlar yıl, ay ve gündür; saat nitelikleri için değer verilmediğinde
# default olarak 0 atanır.
print(dt(1963, 7, 12))
print(dt(1981, 10, 3, 18, 23))
print(dt(year = 1981, month = 10, day = 3, hour = 18, minute = 23))

# datetime objesinin iki adet kullanışlı sınıf metodu vardır: today ve now. her iki metod da mikrosaniye hassasiyetinde tam olarak bulunulan anı çıktı
# olarak verir.
print(dt.today())
print(dt.now())

# diğer objelerde de olduğu gibi tüm niteliklere tek tek erişmek mümkündür fakat diğerlerinde de olduğu gibi bu nitelikler yazılamaz.
şimdi = dt.now()
print(şimdi.year)
print(şimdi.month)
print(şimdi.day)
print(şimdi.hour)
print(şimdi.minute)
print(şimdi.second)
print(şimdi.microsecond)

# bir başka kullanışlı metod da datetime objeleri üzerinde kullanılan bir örneklem metodu weekday'dir. 0'ı ilk indeks alarak ve pazartesiden başlayarak
# datetime objesinin haftanın hangi günü olduğunu verir.
print(şimdi.weekday())

# datetime objeleri değiştirilebilen objeler değildir bu sebeple bir tarihi değiştirmek istediğimizde bunu nokta syntaxıyla yapamayız. bunun için replace
# metodunu kullanırız. replace metodu, objeyi değiştirmek yerine verilen niteliğin yeni değeriyle başka bir obje oluşturur. bunu da bir değişkene
# atayarak başka bir zaman, mesela 5 dakika sonrasını oluşturabiliriz:
beş_dk_sonra = şimdi.replace(minute = şimdi.minute + 5)
print(beş_dk_sonra)

print()

# datetime objelerinde sıklıkla kullanılan bir başka metod da strftime örneklem metodudur. strftime metodu isminden (string from time) de anlaşılacağı
# üzere söz konusu datetime objesinden bir string oluşturur. argüman olarak kendisi de bir string kabul eder fakat bu string normal bir string değil
# çıktı olarak almak istediğimiz tarihin formatını ifade eden bir stringdir. bu string içersinde "%" işareti ile verilen ifadeler, datetime objesinin
# farklı niteliklerini refere eder. bu referanslar, standarttır ve GNU kapsamındaki date programı ile aynı formattadır.
print(şimdi.strftime("%Y")) # yazımı, çıktı olarak yılı verir
# çıktı olarak alınan objenin string tipinde bir obje olduğunu type fonksiyonu ile teyit edebiliriz:
print(type(şimdi.strftime("%Y")))
# iki dijit yıl için "y", ay için "m", gün için "d" kullanarak türkçeye göre formatlanmış ve / ile ayrılmış bir tarih yazımı elde edebiliriz:
print(şimdi.strftime("%d/%m/%y"))
# seperatör olarak istediğimiz karakterleri kullanabilir hatta ek olarak başka yazımlar da ekleyebiliriz:
print(şimdi.strftime("Bugün tarih %d-%m-%Y"))
# saat için H, dakika için M ve saniye için S:
print(şimdi.strftime("Şu an saat tam olarak %H:%M:%S"))
# hatta istersek bu değerleri integer de yapabiliriz:
saat = int(şimdi.strftime("%H"))
print(f"{saat} {type(saat)}")
# datetime stringlerini formatlamak için kullanılan pek çok ifade mevcuttur. sık kullanılanlardan bazıları haftanın günü ve mevcut ayı yazı ile ifade
# etmemize olanak tanıyan A (uzun gün), B (uzun ay), a (3 digit gün) ve b (3 digit ay) ifadeleridir:
print(şimdi.strftime("This month is %B or %b and it is %A or %a today."))