import unittest
from unittest.mock import MagicMock

# şimdi bir örnekle mocking ve testing konseptlerini birleştirelim:
class Aktor():

    def helikopterden_atla(self):
        return "Hayatta olmaz kafayi mi yediniz aga."

    def atese_atla(self):
        return "Ne diyosun abi? Menajerimi bi çağırsana."

class Film():

    def __init__(self, aktor):
        self.aktor = aktor

    def cekimlere_basla(self):
        self.aktor.helikopterden_atla()
        self.aktor.atese_atla()

class FilmTesti(unittest.TestCase):
    # burada test etmek istediğimiz obje Film objesi. fakat Film objesi bir Aktor objesine ihtiyaç duyuyor.
    # hatırlayacağımız üzere unit testler tek bir "unit" yani birimi test etmeli ve olabildiğince izole
    # olmalıdır. bu sebeple Film objesini test etmek için bir Aktor objesi oluşturmak doğru bir yaklaşım
    # olmaz. Aktor objesini taklit eden bir mock oluşturmak, test mentalitesine daha uygun olur.
    def test_cekimlere_basla(self):
        dublor = MagicMock()
        # aktorumuzun yerini alacak bir dublor olusturduk. simdi bu aktorle bir Film objesi oluşturalım:
        film = Film(dublor)
        # bu dublor uzerinde cekimlere_basla metodunu çalıştırdığımızda, dublor objesi üzerinde helikopterden_atla
        # ve atese_atla metodları çalışacak. test ettiğimiz durum bu metodların çalışması durumu bunun için gerçek
        # bir Aktor'e ihtiyacımız yok. mock'ların esnekliği işte burada işimize yarıyor.
        film.cekimlere_basla()
        # cekimlere_basla çağırıldığında çalışması gereken metodları da assert_called sayesinde kontrol edebiliriz:
        dublor.helikopterden_atla.assert_called()
        dublor.atese_atla.assert_called()

if __name__ == "__main__":
    unittest.main()
