# iterable bir objeden indeks syntaxıyla bir elemana ulaşmak istediğimizde arka planda olan __getitem__ metodunun çalışmasıdır. bunu pythonun
# buitlin objelerinde gözlemleyebiliriz:
notlar = {
    "F. Kimya": 82.53,
    "F. Teknoloji": 71.24
}
# yukarıdaki notlar sözlüğünden bir indeksi çağıralım:
print(notlar["F. Kimya"])
# aslında bu esnada olan şudur:
print(notlar.__getitem__("F. Kimya"))

# __getitem__ ile sınıflarımızı indekslenebilir hale getiriyoruz fakat yalnızca getitem kullanıdğımızda elimizde stringler gibi indekslenebilir
# ama immutable objeler oluyor. objelerimizin indeks değerlerinin değiştirilebilir olması içinse __setitem__ metodunu kullanıyoruz. pythonda
# obje[i] yazımı, obje üzerinde __getitem__ metodunu tetiklerken obje[i] = değer yazımı da __setitem__ metodunu tetikler ve bu şekilde mutable
# objeler oluşturabiliriz. yani:
notlar["F. Kimya"] = 90.25
print(notlar["F. Kimya"])
# aslında:
notlar.__setitem__("F. Kimya", 95.12)
print(notlar["F. Kimya"])
# ile aynıdır.

print()

# aynı şekilde listeleri de inceleyebiliriz:
dersler = ["F. Kimya", "F. Teknoloji", "F. Toksikoloji"]
print(dersler[1]) # aslında:
print(dersler.__getitem__(1)) # ile aynı şeydir
dersler[0] = "Farmakoloji" # yazımı da,
print(dersler[0])
dersler.__setitem__(0, "Klinik Eczacılık") # yazımıyla aynıdır
print(dersler[0])

print()

# şimdi kendi oluşturduğumuz sınıfların nasıl indekslenebilirhale getirilebileceğine bakalık:
class DersListesi():
    def __init__(self):
        self.dersler = []
    def ders_ekle(self, ders):
        self.dersler.append(ders)
    # eğer __getitem__ metodu tanımlamazsak, DersListesi sınıfının örneklemlerini indekslediğimizde TypeError alırız ve açıklamasında, objenin
    # subscriptable yani takip edilebilir olmadığını görürüz. tek liste içeren bir sınıfta indekslemenin önemi anlaşılmayabilir fakat birden
    # fazla indekslenebilir nitelikten oluşan bir sınıfımız olduğunu düşündüğümüzde, __getitem__ metodu ile hangi niteliğin daha önemli oldu-
    # ğunu başka bir deyişle sınıfımızın indeksini hangi niteliğin daha iyi yansıttığını belirleyebiliriz.
    def __getitem__(self, index): # indeks yerine istediğimiz ismi kullanabiliriz. mesela sınıfımız bir sözlük üzerinden indeksleniyorsa key
        # de diyebiliriz.
        return self.dersler[index]
    # bir de __setitem__ tanımlayarak objemizi mutable hale getirelim buradaki mentalite de esasında getitem ile aynı. tek bir liste olduğunda
    # külfet gibi görünüyor (öyle de zaten) ama komplex bir sınıfta, sınıfın indeksini değiştirdiğimizde ne olması gerektiğini tam olarak be-
    # lirleyebilmemizi sağlıyor.
    def __setitem__(self, index, değer):
        self.dersler[index] = değer

dokuzuncu_yarıyıl = DersListesi()
dokuzuncu_yarıyıl.ders_ekle("İşlem Mühendisliği")
dokuzuncu_yarıyıl.ders_ekle("Kontrollü Salım")
dokuzuncu_yarıyıl.ders_ekle("Serbest Radikaller")
# objemizi indeksleyelim:
print(dokuzuncu_yarıyıl[1])

# şimdi de indeksimizi değiştirelim:
dokuzuncu_yarıyıl[1] = "Medisinal Kimyada Bilgisayar"
print(dokuzuncu_yarıyıl[1])

print()

# indekslenebilirlik, objeye iterasyon özelliği de kazandırır. yani getitem metodu ile nasıl indekslendiğini belirlediğimiz bir objeyi,
# itere ettiğimizde, obje getitemda belitrilen kurala göre itere olur.
for ders in dokuzuncu_yarıyıl:
    print(ders)
