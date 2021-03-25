from random import randint
# mock, test içersinde bir objenin yerini alan başka bir objedir. mockların kullanılmasındaki amaç unit testler
# arasında gerçek bir ayrım yapmaktır. hatırlanacağı üzere unit testler, ideal olarak programın tek bir parçasını
# test etmelidir. unit testlerimizin bu açıdan izole olmasını isteriz fakat gerçekte, test edilen sınıflar başka
# sınıfları içerir, fonksiyonlar başka fonksiyonları çağırır yani programlarımız genellikle testleri izole etmek
# için fazla karmaşıktır. bu sebeple unit testleri gerçek manada izole etmek için mockları kullanarak diğer objelere
# bağlı olan objelerimiz arasında bir ayrım sağlarız. 

# mock modülü, unittest içersinde bulunan bir modüldür ve unittest içersinden çağrılır. şimdilik Mock objelerini
# programımıza dahil edelim:
from unittest.mock import Mock

# şimdi bir mock örneklemi oluşturalım:
pizza = Mock()
print(pizza) # mock objelerinin kendilerine özgü ID'leri vardır.
print(type(pizza))

# mock objeleri oldukça esnektir. istediğimiz kadar değişkeni nokta syntaxıyla ekleyebiliriz.
pizza.boyut = "Buyuk"
pizza.fiyat = 19.90
print(pizza.boyut)
print(pizza.fiyat)

# mock'ların esnekliği bununla da kalmaz; herhangi bir nitelik, herhangi bir metod, pythonda müsait olan herhangi
# bir isim mock objesinde tanımlıdır.
print(pizza.herhangiBirNitelik)
print(pizza.sacmaBiNitelik)
# görülebileceği gibi bir mock objesinden herhangi bir nitelik çağrıldığında o obje içersinde farklı bir mock objesi
# oluşur. bu objelerin hepsinin kendi ID'si vardır ve bu ID'ler de mock'un kendisine özgüdür. aynı mock tekrar çağrıldığında
# ID'si aynı olur:
print(pizza.herhangiBirNitelik)

# bununla da kalmaz, mock objeleri içinde birden fazla seviyede obje de çağırabiliriz:
print(pizza.herhangiBirNitelik.icersinde.baska.bir.nitelik)
# aynı şekilde metodları da çağırmak mümkündür:
print(pizza.issizMetodlar())

# bir mock objesi içine belli değerler atamak için pratikte nokta syntaxı kullanılmaz. bunun yerine mock objeleri üzerindeki
# özel bir örneklem metodu olan configure_mock kullanılır ve değerler bu metoda kw argüman (veya sözlük) şeklinde verilir.
pizza.configure_mock(
    malzemeler = ["Sucuk", "Mozarella", "Mısır"],
    marka = "PizzaHut"
)
print(pizza.marka)
print(pizza.malzemeler)

print()

# özellikle de fonksiyonlar veya metodlar gibi davranmasını istediğimizde mock'lara return değerleri atamamız da mümkündür.
# normalde mock'lar kendi başlarına örneklendiğinde (fonksiyon veya sınıflar gibir) başka bir mock objesi verirler.
mockOrnegi = Mock()
print(mockOrnegi) # örneklediğimiz mock objesi
print(mockOrnegi()) # örneklediğimiz mock objesinin bir sınıf veya fonksiyon gibi örneklenmesi/çağırılması
# bir mock objesinin default return_value niteliği kendisinin örneklemidir (ln. 52'deki gibi yani):
print(mockOrnegi.return_value) # bu niteliğe başka bir değer atadığımızda ise mock objesi örneklendiğinde yeni atanan değeri return eder.
mockOrnegi.return_value = 30
print(mockOrnegi())

# bu değeri mock objesini tanımlarken atamak da mümkündür:
baskaMockOrnegi = Mock(return_value = "Return ediyor..")
print(baskaMockOrnegi())

# mock'ları sınıfların replasmanı için kullandığımızda metodları taklit etmek için de bu nitelikten faydalanırız. burada hatırlamamız
# gereken, mocklar üzerinde çağrılan herhangi bir metodun veya niteliğin de mock objesi olduğu ve bunların da kendi return_value
# nitelikleri olduğudur.
dublor = Mock()
dublor.yuksekten_atla.return_value = "Kolum kirildi amk..."
dublor.atesle_yanma.return_value = "Yandım anammm..."
print(dublor.yuksekten_atla())
print(dublor.atesle_yanma())

print()

# mock objelerindeki bir diğer özel nitelik de side_effect niteliğidir. diğer özel niteliklerden farklı olarak side_effect niteliği dinamiktir.
# return_value'ya benzer şekilde side_effect tanımlanmış bir mock, bir değer return eder fakat return_value niteliği gibi statik değildir.

# mesela side_effect olarak bir fonksiyon verildiğinde, mock'un her bir örneklemi/çağırımı return value olarak bu fonksiyonun çıktısını verir.
# söz konusu dinamizmi göstermek adına random modülünden faydalanarak görelim:
def rastgele_sayi():
    return randint(1, 10)

cagir_beni = Mock()
# tanimlanmadığında side_effect başka bir mock objesi vermez, None verir:
print(cagir_beni.side_effect)
cagir_beni.side_effect = rastgele_sayi # fonksiyonun çağırımını değil kendini atıyoruz buna dikkat.
# şimdi cagir_beni mock'u her çalıştığında farklı bir çıktı alacağız:
print(cagir_beni())
print(cagir_beni())
print(cagir_beni())
print(cagir_beni())

# eğer side_effect'i bir liste olarak tanımlarsak 0'dan -1. indekse kadar mock her çağrıldığında side_effect sıradaki değişkeni return eder.
# mesela listedeki elemanları baştan sona silen ve elemanlar bitince IndexError veren pop metodunu simüle etmek için son elemanı IndexError olan
# 4 elemanı bir listeyi side_effect olarak atayabiliriz:
pop_simulasyonu = Mock(side_effect = [3, 2, 1, IndexError("pop from empty list.")])
# şimdi pop_simulasyonu'nu her cagirdigimizda bir sonraki eleman return edilecek.
print(pop_simulasyonu())
print(pop_simulasyonu())
print(pop_simulasyonu())
# print(pop_simulasyonu()) # bu satır çalışınca IndexError alınır.

# eğer aynı mock için hem return_value hem de side_effect tanımlanmış ise side_effect kazanır:
kim_kazanir = Mock(return_value = "kaybettik..", side_effect = NameError("Hataliydik ama kazandik.."))
# print(kim_kazanir()) # çalışınca NameError verir çünkü side_effect kazanır

# side_effecti sıfırlamak için None'a eşitlemek yeterlidir. bu durumda eğer bir return value tanımlanmadıysa mock'ın örneklemi yine bir mock
# objesi return eder.
mock = Mock()
print(mock())
mock.side_effect = "Yan Etki"
print(mock())
mock.side_effect = None
print(mock()) # return edilen mock objesi, side_effect tanımlanmadan önce return edilenle aynıdır.