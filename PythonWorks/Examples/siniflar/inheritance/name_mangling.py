# name_mangling, ismin karışıklaştırılması gibi bir anlama gelir ve özellikle kütüphane geliştiricileri tarafından, sınıfların nitelik
# ve metodlarında oluşabilecek isim karışıklıklarını önlemek için sıklıkla kullanılan bir syntaxtır. pythonda bazen diğer programcıların
# yazdıkları kütüphaneler üzerinden kodlama yaparız ve bu esnada onları yazdıkları sınıflara alt sınıflar yazarız. name mangling, bu
# alt sınıfların yazımı sırasında, üst sınıftan doğrudan alt sınıfa miras edilmeyen nitelikler oluşturmak için kullanılır. esasında
# olan şey, niteliğin miras edilmemesi değil, niteliğin adının kasti olarak karışıklaştırılmasıdır. bu sayede özel nitelikler oluştu-
# rulur.
class Sınıf():
    def __init__(self):
        # name mangling için niteliğin ismi, başında "__" ile tanımlanır.
        self.__nitelik = "Merhabaa"
    def __metod(self):
        print("Bu metod, özel bi metod.")
    def özele_eriş(self):
        print(self.__nitelik)
        self.__metod()

class AltSınıf(Sınıf):
    pass

sınıf = Sınıf()
altsınıf = AltSınıf()

# hem superclass hem de subclass'ta __nitelik ve __metod'a erişmeye çalışırsak AttributeError alırız:
# print(sınıf.__nitelik)
# print(sınıf.nitelik)
# print(altsınıf.__nitelik)
# print(altsınıf.nitelik)
# altsınıf.__metod()
# altsınıf.metod()
# sınıf.__metod()
# sınıf.metod()
# gerek "__" ile gerekse "__" olmadan hem metodun hem ne niteliğin çağrımları AttributeError verir. ama bu, bunlara erişilemeyeceği
# anlamına gelmez. pythonun nitelikleri özel hale getirme metodu javadaki gibi onları erişilmez kılmak değil, isini karıştırmak. ö-
# zel bir niteliğe erişmek için nitelik; _TanımlandığıSınıf__nitelik_ismi şeklinde çağrılmalıdır:
print(sınıf._Sınıf__nitelik)
print(altsınıf._Sınıf__nitelik)
sınıf._Sınıf__metod()
altsınıf._Sınıf__metod()
# ayrıca tanımlandığı sınıf içersindeki başka metodlar tarafından da söz konusu nitelik kullanılabilir:
sınıf.özele_eriş()
# özele_eriş metodu korumalı olmadığı için alt sınıflara da miras olur:
altsınıf.özele_eriş()
