from datetime import datetime, timedelta
# timedelta objesi, zamanda bir noktayı değil bir "büyüklüğü" ifade eder. bir kaç farklı noktada karşımıza çıkar ve kullanılabilir. zaman uzunluğunu
# gün, saat, dakika, saniye ve microsaniye olarak ifade eder; ay ve yıl birimleri, güne dönüştürülür. timedelta objelerinin kendileri tanımlanırken de
# bu nitelikler kullanılır, yıl ve ay programcı tarafından güne çevrilmelidir.

# timedeltanın ilk kullanımı, timedelta objelerinin yani zaman farkı objelerinin oluşturulmasıdır:
bes_yuz_gun = timedelta(days = 500, hours = 12)
print(bes_yuz_gun)
print(type(bes_yuz_gun))

print()

# bir başka kullanım ise timedelta objelerinin birbirlerine veya datetime objelerine eklenmesi veya çıkarılmasıdır:
bugun = datetime.now()
print(bes_yuz_gun + bes_yuz_gun)
print(bugun + bes_yuz_gun)
print(bugun - bes_yuz_gun)

print()

# iki datetime objesi arasındaki fark da bir timedelta objesidir. mesela doğduğumuz günden bugüne kadar geçen zaman, bir timedeltadır:
dogum = datetime(1995, 11, 9, 6)
harcadigim_zaman = bugun - dogum
print(harcadigim_zaman)
print(type(harcadigim_zaman))
# timedelta objelerinde çalıştırılabilen bir örneklem metodu total_seconds, söz konusu zaman aralığının tamamını saniyeye çevirir ve float tipinde
# return eder.
print(harcadigim_zaman.total_seconds())
print(type(harcadigim_zaman.total_seconds()))