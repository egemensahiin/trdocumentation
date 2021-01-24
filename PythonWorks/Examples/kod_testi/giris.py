# kurduğumuz her mantıkta, yazdığımız her satır kodda hatta yazdığımız her bir karakterde programımızın bozulması riski vardır. bu sebeple kodların test e-
# dilmesi oldukça önem arz eder. "testing" konseptinde hedef, diğer bir kodun işlevselliğini valide eden (doğrulayan) bir kod yazmaktır. testler pythona,
# yazdığımız programların doğruluğunu nasıl kontrol edeceğini anlatırlar; otomatizedirler, bilgisayar tarafından çalıştırılırlar. testlerin otomatize e-
# dilmesi, her bir durumu deneme gerekliliğini bilgisayara yükleyerek zamandan ve emekten kazanmamızı sağlar. otomatize testler hazırlayarak mesela kodda
# bir değişiklik yaptığımızda, tek tek ilgili kısımları çalıştırmak yerine testimizi yürütebiliriz ve bu sayede zaman kazanabiliriz. testler, gerilemeyi
# (regression) önler. burada bahsedilen "gerileme", daha önce çalışan bir işlevin artık çalışmamasıdır. testlerin bir başka faydası da kodumuz için bir
# nevi canlı dökümantasyon olmasıdır.
# 
# test kodları yazmadan önce edinmemiz gereken bir kaç terminolojik bilgi var. bunlardan ilki test suiti kavramı. pythonun test yazmak ve çalıştırmak için
# built-in bir modülü bulunmaktadır, unit testing modülü. unit test modülü, java için yazılmış olan j testing framework'ten esinlenlenilerek kodlanmıştır.
# bu modül bizim bir "test süiti" oluşturmamıza olanak verir. test süiti, ilgili işlevselliği hedefleyen testlerin bir toplamıdır. genellikle rehberlere
# göre testler, izole ve bağımsız olmalıdır yani ideal olarak her test, programdaki bir uniti veya bölümü (mesela tek bir sınıfı veya tek bir fonksiyonu)
# test etmeye çalışır. bağımsız ve izole testler, hangi sırayla yürütülürse yürütülsün aynı sonuçları almamızı ve işlevleri ayrı ayrı test edebilmemizi
# sağlar. bir başka kavram da "kod kapsamı" veya "test kapsamı" kavramıdır ki adından da anlaşılabileceği gibi yazdığımız testin, programın yüzde ne ka-
# darını test edebildiğini ifade eder. bunu analiz eden araçlar mevcuttur. örnek olarak, iki dosyadan oluşan bir program için hazırladığımız test, bu dos-
# yalardan birini tamamen test ediyorsa bu testin kapsamı %50dir. ideal olarak test kapsamının %100 olması istenir fakat gerçek kodlarda bu genellikle
# mümkün olmaz (gerek de yoktur zaten) bu yüzden test kapsamının %100e olabildiğince yakın olması istenir. 