#!/usr/bin/env python3.7

import npyscreen
import random

class OldurmeUygulamasi(npyscreen.NPSApp):
    def main(self):
        appFormu1 = npyscreen.Form(name = "Olum odasina hosgeldin!!")
        aciklama1 = appFormu1.add(npyscreen.MultiLineEdit, editable = False,
                                 value = "\nUzandigin yerden yavasca kalkiyorsun...\
                                  \nIcınde bulundugun oda karanlik ve nerede olduguna dair hicbir fikrin yok....\
                                  \nGozlerin karanlıga yavasca alistiktan sonra, duvardaki isik anahtarini, masadaki silahi ve kapi kolunu goruyorsun...")
        appFormu1.edit()

        appFormu2 = npyscreen.Form(name = "Olum odasina hosgeldin!!")
        aciklama2 = appFormu2.add(npyscreen.FixedText,
                                  value="\nNe yapmak istersin?..")
        secenekler = appFormu2.add(npyscreen.TitleSelectOne, max_height = 5, value = [0,], name = "Seceneklerin sunlar: ",
                                   values = ["Isik anahtarina gidip isigi ac.","Ayaga kalkip masadaki silahi aliyorsun.","Kapiyi acmaya calisiyorsun."])
        appFormu2.edit()

        self.sectigimiz = secenekler.value[0]

        if self.sectigimiz == 0:
#            self.anahtari_ac()
            self.mesaj_taslak(mesaj = "\nZorla yerinden kalkıp anahtara ulasiyorsun.\
                              \nAnahtari actiginda oda kuvvetli bir beyaz isikla doluyor.\
                              \nIcınde bulundugun odanın duvarinda bir cam goruyorsun ve camin arkasinda sandalyeye bagli uc kisi...\
                              \nKisilerin yuzlerine baktiginda Yavuzalp Korkmaz, Anil Aksu ve Oguzhan Sahin olduklarini goruyorsun...\
                              \n\nSimdi ne yapacaksin?..")
            self.anahtarSectigimiz1 = self.secenek_taslak(secenekler = ["Camin arkasindakilere seslen.", "Arkanda duran silahi al ve cama ates et.", "Cebinden telefonu cikar ve hemen Yan Camanın basrollugundeki Pasha Fencer reklamlarini izle."])
#                                aciklama = "Ne yapmak istedigine karar ver...")

            if self.anahtarSectigimiz1 == 0:
                self.mesaj_taslak(mesaj = "\nArkadaslarina seslendin: Neler oluyor burada? Ne yapıyorsunuz??\
                                  \nOguzhan: 8k Yasuo var kardesim bende.\
                                  \nYavuzalp: Falcao gitsin bence.\
                                  \nAnil: Kolsuz musun abi ya?")
                self.mesaj_taslak(mesaj = "\nSaskinlikla arkadaslarinin yuzune baktin. Iyi olup olmadiklarini sordun ama sana cevap veren olmadı..\
                                  \nHenüz durumu anlayamamisken, daha once orada oldugunu bile farketmedigin hoparlorden cizirtili bir ses duydun...")
#                self.hoparlor_secenekleri()
                self.hoparlorSecimi = self.secenek_taslak(secenekler = ["Hoparlore yaklaş ve soylenenleri duymaya calis.","Silahı al ve hoparlore ates et."])
                if self.hoparlorSecimi == 0:
                    pass
                    # hoparlore yaklas
                    self.mesaj_taslak(mesaj = "\nHoparlore yaklastiginda tanidik bir ses duymaya basliyorsun:\
                                      \n- Hahaha Hayrettin hoca seni burada bulabilecegimi soylemisti...\
                                      \nBi sikinti olmazsa, onumuzdeki Ocak ayinda mezunum... Hahahaha!\
                                      \nNeyse, konumuza donelim.")
                    self.mesaj_taslak(mesaj = "\nBirazdan bu cami indirecegim. Elindeki silahta iki kurşun var..\
                                      \nYani burdan sadece iki kişinin sag kurtulmasını istiyorum...\
                                      \nEger bir kahramanlik yapmaya kalkarsan uc arkadasin da sandalyenin altinda bulunan kaziklarla aci icinde olumu tadar. Hahahaha\
                                      \nZamanin kisitli. Kararini hemen vermen lazim.")
                    self.mesaj_taslak(mesaj = "\nArkadaşlarının seslerini duydun:\
                                      \n\nYavuzalp: Ben senin Kim Milyoner Olmak Isterdeki telefon jokerinim, beni olduremezsin. Futbol sorusu gelse yapabilcek misin?\
                                      \nOguzhan: Kanka ben kedisi medisi olan adamim yapma bak. Chester var mi kanka?? Yoksa baska beyaz filtre de olur.\
                                      \nAnil: Sacmalama abi tabii ki de beni seciceksin. Bi de dusunuyo musun bunu gercekten. Silahi ver abi ba...")

                    self.hoparlor0Secim = self.secenek_taslak(secenekler = ["Lafını bitirmesini beklemeden Anil Aksu'yu iki kez vur ve infaz et.",
                                                                            "42 dakika boyunca neden Anil Aksu'yu vurmaman gerektigini dinle."])
                else:
                    # hoparlore ates et
                    pass
            if self.anahtarSectigimiz1 == 1:
                self.mesaj_taslak(mesaj = "\nSilahi aldin ve arkadaslarini kurtarmak umuduyla cama ates ettin...\
                                  \nFakat bilmedigin bir sey vardi...\
                                  \n\nCam kursun gecirmezdi ve seken kursun kasiklarina isabet etti..\
                                  \nCinsel organindan vurulmus halde kan kaybindan oldun...")
                self.oyun_sonu()

            if self.anahtarSectigimiz1 == 2:
                self.mesaj_taslak(mesaj = "\nOmrunun sonuna kadar sarji bir turlu bitmeyen telefonunda Yan Caman videolari izleyerek olumu bekledin...\
                                  \nSon duydugun sey Yan Caman'in su sozleri oldu:\
                                  \n\"Cok eglenceli oyun yha, muthis zaman geciriyorum...\"")
                self.oyun_sonu()

    def anahtari_ac(self):
        appAnahtarForm = npyscreen.Form(name = "Olum odasina hosgeldin!!")
        anahtarAciklama = appAnahtarForm.add(npyscreen.MultiLineEdit, editable = False,
                                             value = "\nZorla yerinden kalkıp anahtara ulasiyorsun.\
                                             \nAnahtari actiginda oda kuvvetli bir beyaz isikla doluyor.\
                                             \nIcınde bulundugun odanın duvarinda bir cam goruyorsun ve camin arkasinda sandalyeye bagli uc kisi...\
                                             \nKisilerin yuzlerine baktiginda Yavuzalp Korkmaz, Anil Aksu ve Oguzhan Sahin olduklarini goruyorsun...\
                                             \n\nSimdi ne yapacaksin?..")
        appAnahtarForm.edit()

        appAnahtarForm2 = npyscreen.Form(name = "Olum odasina hosgeldin!!")
#        anahtarAciklama2 = appAnahtarForm2.add(npyscreen.MultiLineEdit, editable = False,
#                                               value = "Ne yapmak istedigine karar ver...")
        anahtarSecenekler = appAnahtarForm2.add(npyscreen.TitleSelectOne, value = [0,], name = "Seceneklerin sunlar: ",
                                                values = ["Camin arkasindakilere seslen.",
                                                          "Arkanda duran silahi al ve cama ates et.",
                                                          "Cebinden telefonu cikar ve hemen Yan Camanın basrollugundeki Pasha Fencer reklamlarini izle.",])
        appAnahtarForm2.edit()

        self.anahtarSectigimiz1 = anahtarSecenekler.value[0]

#    def hoparlor_secenekleri(self):
#        appHoparlorForm = npyscreen.Form(name = "Olum odasina hosgeldin!!")
#        hoparlorAciklama = appHoparlorForm.add(npyscreen.MultiLineEdit, editable = False,
#                                           value = "Hizlica kararini ver...")
#        hoparlorSecenekler = appHoparlorForm.add(npyscreen.TitleSelectOne, value = [0,], name = "Seceneklerin sunlar: ",
#                             values = ["Hoparlore yaklaş ve soylenenleri duymaya calis.","Silahı al ve hoparlore ates et."])
#        appHoparlorForm.edit()
#
#        self.hoparlorSecimi = hoparlorSecenekler.value[0]

    def mesaj_taslak(self, mesaj):
        appTaslak = npyscreen.Form(name = "Olum odasina hosgeldin!!")
        silahYanlisAciklama = appTaslak.add(npyscreen.MultiLineEdit, editable = False, value = mesaj)
        appTaslak.edit()

    def secenek_taslak(self, secenekler):
        appTaslak = npyscreen.Form(name = "Olum odasina hosgeldin!!")
#        secenekAciklama = appTaslak.add(npyscreen.MultiLineEdit, editable = False,
#                                        value = aciklama)
        taslakSecenekler = appTaslak.add(npyscreen.TitleSelectOne, value = [0,], name = "Seceneklerin sunlar: ",
                             values = secenekler)
        appTaslak.edit()

        return taslakSecenekler.value[0]

    def oyun_sonu(self):
        appOyunBitti = npyscreen.Form(name = "Olum odasina hosgeldin!!")
        oyunSonuAciklama = appOyunBitti.add(npyscreen.MultiLineEdit, editable = False,
                                           value = "\nOynadiginiz icin tesekkurler.")
        appOyunBitti.edit()


if __name__ == '__main__':
    App = OldurmeUygulamasi()
    App.run()
