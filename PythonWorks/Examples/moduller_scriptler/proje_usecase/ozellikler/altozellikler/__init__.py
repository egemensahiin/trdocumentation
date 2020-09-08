# rölatif import için özel bir syntax, from .modül import nitelik, [nitelik]... syntaxıdır. .modül yazımına
# yalnızca __init__.py dosyalarında rastlanır.
from .calculator import creator, PI, subtract, add, area
# bu şekilde import ettiğimiz nitelikler, artık altozellikler paketi içersinde default olarak bulunacaklar-
# dır ve böylece calculator.py modülünü bir daha import etmemize gerek kalmaz.
#!! __init__.py dosyasını bu haliyle çalıştırdığımızda ImportError alıyoruz fakat sebebini çözemedim ://
#!! print("altozelliklerden geldim")
#!! 4. satır da aslında hatadan sonra çalışmasına rağmen üst klasörlerde altozellikler paketini çağırdı-
#!! mızda söz konusu dosyada çalışıyor (hatadan sonra yazıldığı için burada çalışmıyor.)