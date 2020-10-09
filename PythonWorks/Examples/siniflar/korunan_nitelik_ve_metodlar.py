# python, kullanıcılarının sorumlu programcılar olduğunu farzeder ve nokta syntaxıyla niteliklerin değiştirilmesine ve örnek metodlarının public olarak o-
# larak kullanılmasına her koşulda izin verir. fakar pythondaki önemli konseptlerden biri enkapsülasyondur. eğer yazdığımız sınıftaki nitelik veya modül-
# lerin programın mantığı açısından değiştirilmemesi isteniyorsa bunu diğer kullanıcıların anlaması için söz konusu nitelik veya modülün başına "_" konu-
# lur. bir niteliğin başında "_" gördüğümüzde bunu nokta syntaxı ile değil eğer varsa modifiye edebilecek bir örnek modülü ile modifiye etmemiz gerektiği-
# ni; bir modülün başında "_" gördüğümüzde ise bu modülün kendi başına değil başka bir modülle beraber çalıştırılması gerektiğini anlarız.
class AkıllıTelefon():
    def __init__(self):
        self._firma = "Xiaomi"
        self._android = 10.0
    def update(self):
        self._android += 1

# firma ve android nitelikleri yarı özel nitelikler. yani bunları public olarak değiştirebiliyor olsak da programcı bunların public olarak değiştirilmeme-
# si gerektiğini belirmiş.
mi_a_3 = AkıllıTelefon()
print(mi_a_3._firma)
print(mi_a_3._android)
# fakat android niteliğini değiştirebileceğimiz bir modül de yazmış
mi_a_3.update()
print(mi_a_3._android)
