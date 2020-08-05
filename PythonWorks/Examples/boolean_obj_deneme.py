# boolean baska bir veri turu, objedir ve "dogruluk" durumunu ifade eder. iki deger
# alabilmesi soz konusudur ki bunlar True ve False (buyuk kucuk harf duyarli) dur.
# cikti stringlere benzer olsa da string gibi cift tirnak icinde yazilmaz. cift tirnak
# icine yazilan tum ifadeler stringdir, "True" veya "False" dogruluk yanlislik belirt-
# mez. boolean buyuk kucuk harf duyarlidir!! false veya true, boolean degildir
print(True)
print(False)
print("True")
print("False")

# esitlik ve esit olmama (karsilastirma) operasyonlari, cikti olarak boolean 
# turunde veriler verir. pythonda esitlik operatoru "==", esit olmama operatoru
# ise "!=" dir.
print(5 == 5) #True# # esitlik ifadesi dogru oldugunda cikti olarak "True" alinir.
print(5 == 3) #False# # esitlik ifadesi yanlis oldugunda ise "False" verir.
print(5 != 5) #False# # esit degildir ifadesi de ayni mantikla sonuc verir. icerideki
print(5 != 3) #True# # ifade esit oldugunda esit degildir ifadesi yanlis; icerideki ifa-
print(5.3 == 3.2) #False# # de esit olmadiginda ise esit degildir ifadesi dogrudur.
print(6.1 == 6.1) #True#
print(8.0 == 8) #True# # "==" ve "!=" operasyonlari tam sayilari ve ondalik sayilari ki-
# yaslarken tam sayilari da ondalik sekle cevirerek calisir.

# "==" ve "!=" operasyonlari ile stringlerin de karsilastirilmasi mumkundur. string-
# lerde ayni karakterler ayni sirayla bulundugunda == ile "True", != ile False ciktisi
# alinir. buyuk harflerle kucuk harflerin farkli karakterler oldugu unutulmamalidir.
print("lo" == "lo") #True#
print("ol" == "lo") #False#
print("Lo" == "lo") #False#

print("lo" != "lo") #False# cunku karsilastirilan ifadeler esit
print("Lo" == "lo") #True# cunku karlisaltirilan ifadeler esit degil 

# "" icersindeki sayilarin string turunde veriler oldugu unutulmamalidir
print("5" == 5) #False# # ifadesi elbetteki yanlistir.

# iki boolean degeri de birbiriyle karsilastirilabilir. ciktilar yine boolean tipindeki
# verilerdir.
print(True == True) #True#
print(False == False) #True#
print(True == False) #False#

# esittir ve esit degildir disinda 4 tane daha karsilastirma ifadesi vardir:
# karsilastirma operator
#   kucuktur        <
#   kucuk esit      <=
#   buyuktur        >
#   buyuk esit      >=
# bu operatorler de tipki "==" ve "!=" gibi boolean tipindeki ciktilar verirler
print(5 < 8) #True#
print(5 > 8) #False#
print(8 < 5) #False#
print(8 > 5) #True#

print(5 <= 6 < 8) #True# burada iki karsilastirma operatoru kullanilarak bir sayinin (6)
# diger iki sayiya gore durumu degerlendirilir. bu ifadenin dogru (True) olmasi icin her
# iki durumun da (5<=6 ve 6<8) dogru olmasi gerekir ki bu ornekte iki durum da dogrudur.
print(5 <= 8 <=7) #False# (8<=7) # ifadesi yanlis oldugu icin cikti False olur.
print(8 > 5 < 6) #True# # karsilastirma ifadeleri yalnizca sagindaki ve solundaki iki
# sayiyi karsilastirir yani bu ifade degerlendirilirken 8 ve 6'nin birbirlerine gore
# durumlari degil 5'in 8 ve 6'ya gore durumu onemlidir ki hem 8>5 hem de 5<6 ifadeleri
# dogru oldugu icin print ciktisi True olur

# bu tarz bir onerme "==" ve "!=" operasyonlari icin de olusturulabilir
print(5 == 5 != 6) #True#
print(3 < 7 != 2) #True#