# control flow yani akış kontrolü bir programın kalbini oluşturur. tanım olarak: bir
# programın tek tek ifadelerinin, talimatlarının veya işlev çağrılarının yürütülme
# sırasıdır. akış kontrolü sağlanmadığı müddetçe tüm programlar lineer şekilde, line
# 1'den programın sonlandığı satıra kadar ilerler. akış kontrolü ise programa yeni yo-
# llar tanımlamamızı sağlar. akış kontrolü sağlarken kullandığımız en önemli araçlar
# boolean objeleri (bkz. boolean_obj_deneme.py), karşılaştırma operatörleri (bkz 
# boolean_obj_deneme.py) ve ifadeler (statements; if, until, while vb.)dir.
# akış kontrolünde kodun yürümesi bir koşula bağlanır. buna koşulsal mantık (conditi-
# onal logic) denir. "if" ifadesinde eğer koşul doğruysa bu koşula bağlanan kod oku-
# nur aksi takdirde koşula bağlanan ifade yanlış ise okunmaz. koşul ifadelerinin oluş-
# turulması fonksiyon tanımlanmasına benzer. program ifadeyi takip eden satırlarda
# 4 space içerdeki kodu ifadeye bağlı olarak okur.
if True: # :'yı unutma!!
    print("Bu ifade yazılacak, çünkü koşul \"Doğru\"")
if False:
    print("Bu ifade ise yazılmayacak çünkü koşul \"Yanlış\"")
# boolean objesi veren herhangi bir ifade ile if koşulu oluşturulabilir.
if 5 >= 9: # False
    print("Burası yazılmayacak, 5, 9'dan büyük ya da eşit değil")
    print("Burası da yazılmayacak çünkü hala 18. satırdaki if'in bloğundayız")
print("Burası yazılacak çünkü artık bloktan çıktık")

if "Severus" == "Severus": # True
    print("Snape adamdır gerisi madam")

if "Dumbledore" != "dumbledore": # True
    print("Dumbledore'da liderlik vasfı yok kendiyle bile çelişiyor.")

# boolean verilerinin çok çeşitli yollarla elde edilebileceği unutulmamalıdır. mesela:
if type("str") == str:
    print("Bu bir string")
if type(5.99) == int:
    print("Peki bu bir tamsayı mı? HAYIR")

print()

# if koşuluna int, str, float vs tipteki objeler bağlandığında program hata vermez.
# bunun yerine python bu objeleri boolean tipine çeverir ve program bu şekilde çalışır.
# boolean tipine çevrildiğinde doğru olan objelere "truthie" yanlış olanlara ise "falsie"
# denir çünkü bunlar tam anlamıyla True veya False şeklinde değerlendirilemez.
# 0 haricindeki tüm int tipindeki objeler truthie'dir, 0 ise falsie'dir.
# boş string ("") haricinde tüm str'ler truthie'dir. boş string ise falsie'dir.
# 0.00.. haricindeki tüm float'lar truthie'dir. 0.00.. ise falsie'dir.
if 3:
    print("burası yazılacak")
if -3:
    print("burası da yazılacak")
if 0:
    print("ama burası yazılmayacak...")

if "aljskaj":
    print("\nbu string dolu")
if " ":
    print("hatta bu string de dolu")
if "":
    print("ama bu boş :((")

if 3.14:
    print("\nbu doğrumsu bi değer.")
if -3.14:
    print("hatta bu da öyle")
if 0.0:
    print("ama malesef bu değil")
# bir objenin doğru olarak mı yanlış olarak mı değerlendirileceği, "bool" fonksiyonu ile
# bulunur. tıpkı str, int veya float gibi aslında bool fonksiyonu da kendine verilen i-
# fadeyi boolean değerlerine çevirir.
print(bool(1648))
print(bool(-545))
print(bool(0))

print(bool("herhangi bir string"))
print(bool(""))

print(bool(3.6541354))
print(bool(-2.546))
print(bool(0.001))
print(bool(0.0000))