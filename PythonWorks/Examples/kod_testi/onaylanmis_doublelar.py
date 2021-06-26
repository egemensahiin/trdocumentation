# onaylanmış double'lar (verifying double) mocklarla ilgili oldukça önemli bir konsepttir. daha önce de gördüğümüz gibi mock objeleri oldukça dinamik
# yapıdadır fakat bu dinamizm her zaman istenen bir durum değildir. mesela mock kullanarak hazırladığımız bir testte yazım hatalarını veya atamayı unuttuğumuz
# değişkenleri farkedemeyiz çünkü mocklar, bu objeleri çağırdığımızda başka bir mock objesi oluştururlar. magic mocklar bu gibi durumlar için özel bir nitelik
# taşırlar: spec. spec niteliğine bir sınıfın kendisi veya örneklemi verildiğinde, mock bu sınıfın veya örneklemin nitelikleri ve metodlarından başka bir
# nitelik/metod çağırılmasında hata verirler yani söz konusu objeyi gerçeğe çok daha yakın taklit ederler.
from unittest.mock import MagicMock

class DonerDurum():
    restoran = "Acıktım 2 Alpay Abi"

    @classmethod
    def spesyel(cls):
        return cls(protein = "et", patates = True, porsiyon = 1.5)
    
    def __init__(self, protein, patates, porsiyon):
        self.protein = protein 
        self.patates = patates
        self.porsiyon = porsiyon
    
    def porsiyon_arttır(self):
        self.porsiyon += 0.5

# bu dürüm döner sınıfını klasik mock objesiyle taklit etmeye çalıştığımızda, her türlü niteliği kopyalayalayabiliriz fakat yanlış yazım, olmayan bir niteliğin
# çağrımı vb durumlarda hata almayız:
klasik_mock = MagicMock()
print(klasik_mock.protein)
print(klasik_mock.patates)
print(klasik_mock.porsiyon)

print(klasik_mock.yesillik) # aslinda taklit etmek istedigimiz objede boyle bir nitelik yok ama mock bunu da varmış gibi kabul eder.

# fakat spec ile kullanımda, objeyi daha iyi taklit edebiliriz. bunu hem sınıf hem de örneklem düzeyinde yapmamız mümkün:
sinif_mock = MagicMock(spec = DonerDurum)
print(sinif_mock.spesyel())
print(sinif_mock.restoran)
orneklem_mock = MagicMock(spec = DonerDurum("et", True, 1))
print(orneklem_mock.protein)
# bunlarda sıkıntı yok mesela ama aşağıdaki satır çalışınca hata verir:
# print(orneklem_mock.yesillik)

# bunun da daha özel bir hali spec_set'tir. normal spec kullanmamız durumunda, objenin sahip olmadığı nitelikler mock edilmez fakat en nihayetinde bu da bir mock
# objesi olduğu için yeni nitelikleri nokta syntaxı ile kabul eder. spec_set ile bir mockun objeye bağlanması ile ise bu mocka yeni bir nitelik tanımlanamaz.
orneklem_mock.sos = True
print(orneklem_mock.sos)

orneklem_set_mock = MagicMock(spec_set = DonerDurum("et", True, 1))
print(orneklem_set_mock.protein)
# orneklem_set_mock.sos = True # bu satır çalıştığında hata alınır.