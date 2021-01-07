# else bloğu, try bloğundan sonra gelir ve yalnızca, eğer try bloğunda bir hata yakalanmazsa çalışır. her try bloğundan sonra yalnızca bir else
# bloğu yazılabilir. mantıken hatasız bir try bloğunda bir kod yürütmek için doğrudan try bloğuna yazabiliriz. fakat bu şekilde kodumuzu daha temiz
# yazabiliriz. genel olarak, özellikle de büyük projelerde, hata yakalamak için kullandığımız try bloklarının çok uzun olması istenmez, try bloğunda
# yalnızca hatanın yakalanmasını istediğimiz kodu bulundurmak iyi bir pratiktir. hata alınmayan durumlarda çalıştırılacak diğer kodlar bu sebeple
# else bloğunda yazılır. böylece kodumuza geri dönüp baktığımızda alınan bir hatanın nereden aldığını daha rahat okuyabiliriz.
try:
    print(x + 5)
except NameError:
    print("Kullanılan değişken bulunamadı.")
else:
    print("Kullanılan değişken bulundu ve başarıyla kullanıldı.")

# görüldüğü gibi x değişkeni tanımlanmadığı için kodumuz NameError yakaladı ve except bloğu çalıştı. try bloğundan hata yakalandığı için else bloğu
# çalışmadı. 

print()
 
# şimdi x değişkeni tanımlayıp aynı kodu çalıştıralım:
x = 10
try:
    print(x + 5)
except NameError:
    print("Kullanılan değişken bulunamadı.")
else:
    print("Kullanılan değişken bulundu ve başarıyla kullanıldı.")

# görüldüğü üzere try bloğu başarıyla çalıştı ve except bloğu çalışmadığı için else bloğu da çalıştı ve çıktıda iki bloğun da çıktısını gördük.

print()

# sonraki bloğun pratiği için x değişkenini silelim
del x

# finally bloğu ise kodda hata yakalansa da yakalanmasa da çalışır. sınıflarda gördüğümüz __del__ metoduna benzer şekilde, her ne olursa olsun ça-
# lışmasını istediğimiz bir kodu çalıştırmak için kullanılabilir. mesela try bloğunda bir dosya açtık ve else bloğunda dosyayı kapattık. eğer
# try bloğunda bir hata yükseklir ve except bloğuna geçilirse, else bloğu çalışmayacaktır ve dosya kapanmayacaktır. bu da gereksiz ram kullanımına ve
# veri kayıplarına yol açabilir. bu sebeple dosyayı finally bloğunda kapatmak daha iyi bir pratiktir. finally bloğu kodda hata yükselip except bloğuna
# geçilse de (veya geçilmese de), kod çalışıp else bloğuna geçilse de her halükarda çalışacaktır.

# try:
#     print(x + 10)
# finally:
#     print("Hata da olsa burası yazıldı...")

# çıktıda görülebileceği üzere hata çıktısının hemen öncesinde finally bloğundaki kod çalıştı. fakat devam eden kısmı engellememesi için burayı yorumlayalım.
# kod çalışınca da finally bloğu çalışıyor:
try:
    print("Burda ne hata olacak??")
finally:
    print("Sonunda....")

print()

# except ve else bloklarıyla da finally keywordü çalışır:
try:
    print(x + 10)
except NameError:
    print("Kullanılan değişken bulunamadı.")
else:
    print("Kullanılan değişken bulundu ve başarıyla kullanıldı.")
finally:
    print("Sonunda....")

print()

# else bloğu da çalışsa finally bloğu gene çalışacak:
x = 10
try:
    print(x + 10)
except NameError:
    print("Kullanılan değişken bulunamadı.")
else:
    print("Kullanılan değişken bulundu ve başarıyla kullanıldı.")
finally:
    print("Sonunda....")