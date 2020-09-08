# paketleri ve __init__.py dosyasını, ornek_proje'de gördük fakat elbette __init__.py dosyalarını paketleri
# import ederken print fonksiyonu çalıştırmak için kullanmıyoruz. örneğin eğer calculator.py modulunden sub-
# tract fonksiyonunu çağırmak istersek şu satırları yazmamız gerekir:
# import ozellikler.altozellikler.calculator
# print(ozellikler.altozellikler.calculator.subtract(5, 3))
# ama görüldüğü üzere bu şekilde bir syntax kullanımı oldukça uzun isimler içermektedir. bu sebeple __init__
# dosyalarından faydalanılarak rölatif import dediğimiz yöntem kullanılır. rölatif import, mevcut pakette ya-
# pılan importtur. (gerisi /ozellikler/altozellikler/__init__.py içersinde)

# ../altozellikler/__init__.py dosyasına yazdığımız 3. satır sayesinde artık calculator.py modulunu import
# etmeden altozellikler paketi içersinde subtract fonksiyonunu çalıştırabiliriz.
import ozellikler.altozellikler
print(ozellikler.altozellikler.subtract(5, 3))