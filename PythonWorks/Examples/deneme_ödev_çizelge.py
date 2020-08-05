ödevler = []
biten_ödevler = []
verilmemiş_ödevler = []

kontrol = 0

def fon(a, b):
    print(f"{a} ödevler (toplam {len(b)} tane):")
    for i in b:
        print(i)

while kontrol == 0:
    ders = input("Ödev verilmemiş bir ders giriniz (devam etmek için q): ")
    if not ders == "q":
        verilmemiş_ödevler.append(ders)
    else:
        kontrol = 1

kontrol = 0

while kontrol == 0:
    ders = input("Ödev verilmiş bir ders giriniz (devam etmek için q): ")
    if not ders == "q":
        ödevler.append(ders)
    else:
        kontrol = 1

fon("Verilecek", verilmemiş_ödevler)
fon("Yapılacak", ödevler)

kontrol = 0

while kontrol == 0:
    ders = input("Bitmiş ödevleri giriniz (devam etmek için q): ")
    if not ders == "q":
        biten_ödevler.append(ders)
        for ind, drs in enumerate(ödevler):
            if drs == ders:
                ödevler.pop(ind)
    else:
        kontrol = 1

fon("Yapılacak", ödevler)
fon("Bitmiş", biten_ödevler)