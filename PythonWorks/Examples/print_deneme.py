# print zaten ne olduğu mağlum. "" veya '' içersinde yazılan ifade ne olursa olsun
# "string" olarak kabul edilir. tırnak içerisinde olmayan sayılar (operasyon sonuçları
# da dahil olmak üzere) kendi değerlerinde okunur, string olarak okunmazlar.
print("Hello World!") # "" içersindeki ifade string olarak alınır ve olduğu gibi okunur
print("3")
print("3 + 1") # aynısı sayılar, operasyonlar ve klavyeyle yazılan tüm işlemler için
# geçerlidir. eğer "" veya '' içersindeyse ifade "string"dir.

print(3) # sayılar da tek başlarına iken olduğu gibi okunur
print(3 + 1) # print altındaki operasyonların sonucu da sayılarda olduğu gibi okunur,
# string olarak okunmaz. 6. ve 10. satırlardaki komutların farkı kolayca görülmektedir.

print("")

print("A", "B", "C", 5, 5+3) # birden fazla objeyi aynı fonksiyon altında print edebil-
# mek de mümkündür. bunu yaparken iki objeyi birbirinden ayırmak için virgül (,) kulla-
# nılır (boşluk opsiyoneldir). default olarak çıktıda iki obje arasında bir karakter
# boşluk bulunur.

# print fonksiyonu 4 parametre ile konfigüre edilir. bu parametreler "sep" (seperation),
# "end", "file" ve "flush"tır ve default olarak print fonksiyonunun ifadesi
# print(*object, sep=' ', end='\n', file=sys.stdout, flush=False)
# şeklindedir. (*, istenilen sayıda demek)

print("A", 5, 2+1, sep='!') # sep parametresi, print fonksiyonu altında birbirinden ay
# rılan objelerin arasına yerleştirilen string'i belirler ve default olarak ' ' yani
# boşluktur. bunu ünlem ile değiştirdiğimizde outputun farklı olduğu görülmektedir.

print("A", "B", end='...') # end parametresi ise print fonksiyonundan sonra eklenen stri
print("C", "D") # ngi yani fonksiyonun bitişini belirler. default olarak '\n' yani sa-
# tır sonudur (alt satıra geçer). örnekte boşluk olarak değiştirdiğimizde alttaki print
# komutunun diğerinden bir boşluk sonra okunduğu görülmektedir.

print("çoq qomiq", "baya güldüm", sep=' xdxd ', end=' xde') # bu da bi örnek
# önemli bir nokta, sep ve end parametreleri herhangi bir obje olamaz, ikisi de string
# olmak zorundadır!!
print("")

# yan yana üç tane çift tırnak (""") içersine alınan ifade, birden farklı satırda yazı-
# labilir. iki satırda yazılacak bir metni, iki farklı string olarak alt alta print fon-
# siyonuyla yazmak yerine tek bir string şeklinde (""") içersine yazılabilir.
print("""bakalım
nasıl
olacak""")