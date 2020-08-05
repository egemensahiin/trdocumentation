# input fonksiyonu çalıştırıldığında program, kullanıcıdan
# bir "girdi" yazmasını bekler ve girdi yazılıp enter'a
# basıldığı zaman devam eder. bunu anlamak için input fon-
# ksiyonundan sonra bir print fonksiyonu eklenebilir.
# input fonksiyonu sonlandırılmadan print fonksiyonunun
# çalışmadığı görülecektir çünkü program, kullanıcının ob-
# je girmesini bekleyecektir.
# input fonksiyonuna verilen veri, string tipindedir. eğer
# int veya float gibi başka şekillerde kullanılacaksa ge-
# rekli fonksiyonlarla çevrilmesi gerekir. input fonksi-
# yonuna eklenen string, input'a veri girilmeden hemen
# önce yazılır.
# girilen obje bir değişkene atabanilir. bunu yapmak i-
# çin değişken = input("string ") şeklinde yazılmalıdır.
# bu değişken kullanılarak girilen input programda kul-
# lanılabilir.
# örnek olarak isminizi girdiğinizde memnun olduğunu
# söyleyen bir program yazabiliriz:
isim = input("Isminiz nedir? ")
print("Tanıştığıma memnun oldum,", isim)