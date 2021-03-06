# Egzersiz 10
def truthy_or_falsy(a):
    if bool(a) == True:
        b = "truthy"
    if bool(a) == False:
        b = "falsy"
    a = str(a)
    return "The value " + a + " is " + b

print(truthy_or_falsy(""))
print(truthy_or_falsy(5))

print()

# Egzersiz 10
def even_or_odd(a):
    if a % 2 == 1:
        b = "odd"
    if a % 2 == 0:
        b = "even"
    return b

print(even_or_odd(5))
print(even_or_odd(0))

print()

# Egzersiz 11 # if'le falan alakasını çözemedim valla
def up_and_down(a):
    str(a)
    return a.swapcase()
print(up_and_down("SASFA"))
print(up_and_down("akehljdf"))
print(up_and_down("ASDasdASDAfsad"))

print()

# Egzersiz 12
def string_theory(a):
    if a.startswith("S") and len(a) > 3:
        return True
    else:
        return False

print(string_theory("Sansar"))
print(string_theory("SOS"))

print()

# Egzersiz 12
def divisible_by_three_and_four(a):
    if a % 3 == 0 and a % 4 == 0:
        return True
    else:
        return False

print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(15))

print()

# Deneme
def reverse(str):
    rts = ""
    kontrol = -1
    while len(rts) < len(str):
        rts += str[kontrol]
        kontrol -= 1
    return rts

print(reverse("lajdalkd"))
print(reverse("Snape"))

print()

# Deneme 2
# aynı fonksiyonu recursion mantığıyla da yazabiliriz. fakat önce bir analiz etmek lazım.
# şimdi bi düşünelim. 1 karakterli stringin tersi de kendisidir yani base case'imiz (dur-
# durmak için kullanacağımız koşul ifadesi; if koşulu) aşağıdaki gibi olur:
# if len(str) <= 1:
#     return str # yani eğer str uzunluğu 1 veya daha küçükse aynısını yazdır. base case
# önemli. önce base case belirlemek gerekir.
# şimdi stringin son karakterini çağırmak için indeks bilgisini kullanalım. bir stringin
# son karakteri str[-1] şeklinde çağırılır. fonksiyonumuz önce stringin son karakterini
# almalı ardından bunu sondan bir önceki karakterle onu da ondan bir önceki karakterle
# vs birleştirerek son karaktere kadar ilerlemeli. yani str için str[-1] i aldıktan son-
# ra str'ın sondaki karakteri çıkarılmış halinin tekrar [-1] indeksini almalı. str'ın
# sondaki karakteri çıkmış halini şöyle elde etmemiz mümkündür: str[:-1] çünkü biliyo-
# ruz ki str'ın 0'dan -1'e kadar indeksini aldığımızda -1. karakter yeni oluşan stringe
# dahil edilmeyecektir. şöyle şematize edebiliriz:
# str = "Snape" olsun
# str[-1] = S
# e + reverse(str[:-1])
# e + p + reverse(str[:-1])
# e + p + a + reverse(str[:-1])
# e + p + a + n reverse(str[:-1])
# e + p + a + n + S olur.
def reverse2(str):   # str = egemen olsun
    if len(str) <= 1: # 6 <= 1 False o yüzden blok atlanıyor.
        return str
    return str[-1] + reverse2(str[:-1])
#----------"n"          str = str[:-1] ----> egeme
#--------------------   if len(str) <= 1: -> 5 <= 1; False
#--------------------       if bloğu okunmayacak!
#--------------------   return str[-1] + reverse(str[:-1])
#------------------------------"e"          str = str[:-1] ----> egem
#----------------------------------------   if len(str) <= 1: -> 4 <= 1; False
#----------------------------------------       if bloğu okunmayacak!
#----------------------------------------   return str[-1] + reverse(str[:-1])
#--------------------------------------------------"m"          str = str[:-1] ----> ege
#------------------------------------------------------------   if len(str) <= 1: -> 3 <= 1; False
#------------------------------------------------------------       if bloğu okunmayacak!
#------------------------------------------------------------   return str[-1] + reverse(str[:-1])
#----------------------------------------------------------------------"e"          str = str[:-1] ----> eg
#--------------------------------------------------------------------------------   if len(str) <= 1: -> 2 <= 1; False
#--------------------------------------------------------------------------------       if bloğu okunmayacak!
#--------------------------------------------------------------------------------   return str[-1] + reverse(str[:-1])
#------------------------------------------------------------------------------------------"g"          str = str[:-1] ----> e
#----------------------------------------------------------------------------------------------------   if len(str) <= 1: -> 1 <= 1; True
#----------------------------------------------------------------------------------------------------       return str ----> yani burdan str çıkacak o da "e"
#----------------------------------------------------------------------------------------------------       fonksiyonun geri kalanı okunmayacak ve son fonk-
#                                                                                                           siyon çıktı olarak "e" verecek şimdi ilk fonksi-
#                                                                                                           yon bitene kadar geriye doğru okunacak bu durum-
#                                                                                                           da return "n" + "e" + "m" + "e" + "g" + "e" ola-
#                                                                                                           cak. bunu print edince de nemege olacak.
print(reverse2("Egemen"))

print()

# Deneme 3
def faktöriyel(sayı):
    kontrol = sayı
    if kontrol == 1:
        return sayı
    return sayı * faktöriyel(sayı-1)
print(faktöriyel(10))

print()

# Deneme 4
denemelik = "aksflaks aslkja"
for a in denemelik:
    print(a)

print()

# Deneme 5 # bir listedeki sadece tek sayıları toplayan fonksiyon
def total_odd(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 1:
            total += number
    return total

print(total_odd([3, 5, 6, 8, 9, 1, 4, 2, -101]))

print()

# Deneme 6
def largest_num(nums):
    largest = nums[0]
    for num in nums:
        if num > largest: # >= de aynısını yapar ama böyle daha az işlem olur.
            largest = num
    return largest

print(largest_num([3, 5, 6, 8, 9, 1, 4, 2, 101]))
print(largest_num([-3, -5, -6, -8, -9, -1, -4, -2, -100]))

print()

# Egzersiz 19
def super_sum(ls):
    total = 0
    if len(ls) == 0:
        return total
    else:    
        for element in ls:
            if element.find("s") > -1:
                total += element.find("s")
        return total

print(super_sum([]))
print(super_sum(["mustache"]))
print(super_sum(["mustache", "greatest"]))
print(super_sum(["mustache", "pessimist"]))
print(super_sum(["mustache", "greatest", "almost"]))

print()

# Egzersiz 19
def concatenate(ls):
    conc = ""
    for element in ls:
        if len(element) > 2:
            conc += element
    return conc

print(concatenate(["abc", "def", "ghi"])) 
print(concatenate(["abc", "de", "fgh", "ic"]))
print(concatenate(["ab", "cd", "ef", "gh"])) # ----> boş string çıkacak.

print()

# Egzersiz 19
def smallest_number(ls):
    smallest = ls[0]
    for number in ls:
        if number < smallest:
            smallest = number
    return smallest

print(smallest_number([1, 2, 3]))
print(smallest_number([3, 2, 1]))
print(smallest_number([4, 5, 4]))
print(smallest_number([-3, -2, -1]))

print()

# Egzersiz 20
def sum_of_values_and_indices(ls):
    total = 0
    for idx, num in enumerate(ls):
        total += (num + idx)
    return total

print(sum_of_values_and_indices([1, 2, 3]))
print(sum_of_values_and_indices([0, 0, 0]))
print(sum_of_values_and_indices([]))

print()

# Egzersiz 20 # find metoduyla aynı işi yapıyor.
def in_list(ls, st):
    loc = -1
    for idx, el in enumerate(ls):
        if st == el:
            loc = idx
    return loc

strings = ["enchanted", "sparks fly", "long live"]
print(in_list(strings, "enchanted"))
print(in_list(strings, "sparks fly"))
print(in_list(strings, "fifteen"))
print(in_list(strings, "love story"))

print()

# Deneme 7
def arama(sayı, liste):
    sonuc = False
    for herbir in liste:
        if herbir == sayı:
            sonuc = True
            break
    return sonuc

print(arama(3, [1, 3, 5, 8, 6, 9, 87, 25]))

print()

# Deneme 7
def arama2(sayı, liste):
    sonuc = False
    for _, herbir in enumerate(liste, 1):
        if herbir == sayı:
            sonuc = True
            print(f"Aranan sayı listede var.")
            break
    if sonuc == False:
        print("Aranan sayı listede yok.")
    return

arama2(3, [1,4,6787,828,64,65,787,6,3])
arama2(3, [21,21,21321,154,54,541,4574])

print()

# Egzersiz 21
def length_match(ls, i):
    count = 0
    for number in ls:
        if len(number) != i:
            continue
        count += 1
    return count

print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))
print(length_match([], 5))

print()

# Egzersiz 21
def same_index_values(als, bls):
    sls = []
    for i, a in enumerate(als):
        if bls[i] == a:
            sls += [i]
    return sls

print(same_index_values([1, 2, 3], [3, 2, 1]))
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))

print()

# Egzersiz 21
def sum_from(a, b):
    total = 0
    b = b + 1
    for i in range(a, b):
        total += i
    return total

print(sum_from(1, 5))
print(sum_from(3, 8))
print(sum_from(9, 12))

print()

# Deneme 8
def listenin_karesi(liste):
    kareler = []
    for eleman in liste:
        kareler.append(eleman ** 2)
    return kareler
print(listenin_karesi([1, 2, 6, 8, 9]))

print()

# Deneme 9
def floata_cevir(sayılar):
    floatlar = []
    for sayı in sayılar:
        floatlar.append(float(sayı))
    return floatlar
print(floata_cevir([1, 2, 6, 8, 9]))

print()

# Deneme 10
def even_or_odd2(liste):
    sonuc = []
    for sayı in liste:
        sonuc.append(sayı % 2 == 0) # şimdi burada sayı çift ise parantezin içi True, tek ise False olacak;
    return sonuc
print(even_or_odd2([1, 2, 6, 8, 9]))

print()

# Egzersiz 23
def only_evens(liste):
    result = list()
    for eleman in liste:
        if eleman % 2 == 0:
            result.append(eleman)
    return result
print(only_evens([4, 8, 15, 16, 23, 42]))
print(only_evens([1, 3, 5]))
print(only_evens([]))

print()

# Egzersiz 23
def long_strings(liste):
    result = list()
    for eleman in liste:
        if len(eleman) >= 5:
            result.append(eleman)
    return result
print(long_strings(["Ace", "Cat", "Job"]))
print(long_strings([]))
print(long_strings(["Hello", "Goodbye", "Sam"]))

print()

# Egzersiz 24
def factors(i):
    l = []
    for f in range(1, i + 1):
        if i % f == 0:
            l.append(f)
    return l
print(factors(1))
print(factors(2))
print(factors(10))
print(factors(64))

print()

# Egzersiz 25 bir liste ve bir obje kabul ediyor. obje listede varsa siliyor.
def delete_all(liste, obje):
    while obje in liste:
        liste.remove(obje)
    return liste

print(delete_all([1, 3, 5], 3))
print(delete_all([5, 3, 5], 5))
print(delete_all([4, 4, 4], 4))
print(delete_all([4, 4, 4], 6))

print()

# Egzersiz 25 bir listeyi iterate ediyoruz. eleman 5ten büyükse yeni listeye ekliyoruz. değilse (<=) yeni
#             listenin son elemanını siliyoruz (yani boş pop metodu)
def push_or_pop(liste):
    new_list = []
    for num in liste:
        if num > 5:
            new_list.append(num)
        else:
            new_list.pop()
    return new_list

print(push_or_pop([10]))
print(push_or_pop([10, 4]))
print(push_or_pop([10, 20, 30]))
print(push_or_pop([10, 20, 2, 30]))

print()

# Egzersiz 26 verilen stringdeki karakterleri alfabede 2 ilerletiyor.
def encrypt_message(string):
    alphabet = "abcdefghıjklmnopqrstuvwxyz"
    final = ""
    for char in string:
        if char == "y":
            new_char = "a"
        elif char == "z":
            new_char = "b"
        else:    
            ind = alphabet.index(char) + 2
            new_char = alphabet[ind]
        final += new_char
    return final

print(encrypt_message("abc"))
print(encrypt_message("xyz"))
print(encrypt_message(""))

print()

# Egzersiz 27
def word_lengths(string):
    liste = []
    ayrım = string.split(" ")
    for kelime in ayrım:
        liste.append(len(kelime))
    return liste

print(word_lengths("Mary Poppins was a nanny"))
print(word_lengths("Somebody stole my donut"))

print()

# Egzersiz 27
def cleanup(liste):
    for eleman in liste:
        if eleman.isspace() == True:
            liste.remove(eleman)
        elif eleman == "":
            liste.remove(eleman)
    return " ".join(liste)

print(cleanup(["cat", "er", "pillar"]))
print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["", "", " "]))

print()

# Egzersiz 28 # çokboyutlu (iç içe) listelere örnek
def nested_sum(upper_list):
    total = 0
    for lower_list in upper_list:
        for number in lower_list:
            total += number
    return total

print(nested_sum([[1, 2, 3], [4, 5]]))
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
print(nested_sum([[]]))

print()

# Egzersiz 28
def fancy_concatenate(upper_list):
    concat = ""
    for lower_list in upper_list:
        if len(lower_list) == 3:
            for string in lower_list:
                concat += string
        else:
            continue
    return concat

print(fancy_concatenate([["A", "B", "C"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))
print(fancy_concatenate([["A", "B"], ["C", "D"]]))

print()

# Egzersiz 29
# The floats variable should store the floating point values for each string in the values list.
values = ["3.14", "9.99", "567.324", "5.678"]
floats = [float(sayı) for sayı in values]
print(floats)
# The letters variable should store a list of 5 strings. 
# Each of the strings should be a character from name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
name = "Egemen"
letters = [harf * 3 for harf in name]
print(letters)
# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
lengths = [len(element) for element in elements]
print(lengths)

print()

# Egzersiz 29

def destroy_elements(fst_list, scd_list):
    new_list = [el for el in fst_list if not el in scd_list]
    return new_list

print(destroy_elements([1, 2, 3], [1, 2]))
print(destroy_elements([1, 2, 3], [1, 2, 3]))
print(destroy_elements([1, 2, 3], [4, 5]))

print()

# Egzersiz 30
def right_words(liste, sayı):
    return list(filter(lambda eleman: len(eleman) == sayı, liste))
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))
print(right_words([], 4))

print()

# Egzersiz 30
def only_odds(sayılar):
    return list(filter(lambda sayı: sayı % 2 == 1, sayılar))
print(only_odds([1, 3, 5, 6, 7, 8]))
print(only_odds([2, 4, 6, 8]))

print()

# Egzersiz 30
def count_of_a(kelimeler):
    return list(map(lambda kelime: kelime.count("a"), kelimeler))
print(count_of_a(["alligator", "aardvark", "albatross"]))
print(count_of_a(["plywood"]))
print(count_of_a([]))

print()

# Egzersiz 31
def greater_sum(lst1, lst2):
    if sum(lst2) > sum(lst1):
        return lst2
    else:
        return lst1
print(greater_sum([1, 2, 3], [1, 2, 4]))
print(greater_sum([4, 5], [2, 3, 6]))
print(greater_sum([1], []))

print()

# Exercise 'Dictionaries from lists'
def to_dictionary(liste):
    sozluk = {}
    for indeks, eleman in enumerate(liste):
        sozluk[eleman] = indeks
    return sozluk

detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
print(to_dictionary(detectives))

print()

# Exercise 'Dictionaries from lists'
def length_counts(liste):
    counts = {}
    for eleman in liste:
        uzunluk = len(eleman)
        if uzunluk in counts:
            counts[uzunluk] += 1
        else:
            counts[uzunluk] = 1
    return counts

sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
print(length_counts(sa_countries))

print()

# Exercise 'The items Method'
def invert(d):
    empty = {}
    for key, value in d.items():
        empty[value] = key
    return empty
my_dict = {
  "A": "B", 
  "C": "D",
  "E": "F"
}
print(invert(my_dict))

print()

# Exercise 'The items Method'
def count_of_value(d, i):
    count = 0
    for _, value in d.items():
        if value == i:
            count += 1
    return count
my_dict = { "a" : 5, "b" : 3, "c" : 5 }
print(count_of_value(my_dict, 5))
print(count_of_value(my_dict, 3))

print()

# Exercise 'The items Method'
def sum_of_values(d, l):
    tot = 0
    for key, value in d.items():
        if key in l:
            tot += value
    return tot

my_dict = { "a": 5, "b": 3, "c": 10 }
print(sum_of_values(my_dict, ["a"]))
print(sum_of_values(my_dict, ["a", "c"]))
print(sum_of_values(my_dict, ["a", "c", "b"]))
print(sum_of_values(my_dict, ["z"]))

print()

# Exercise 'Keyword Arguments'
def plenty_of_arguments(a, b, **kwargs):
    kw = 0
    for vals in kwargs.values():
        kw += vals
    sq = a + b
    return (kw + sq) > 100

print(plenty_of_arguments(20, 30))
print(plenty_of_arguments(a = 50, b = 75))
print(plenty_of_arguments(a = 50, b = 25, c = 50))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 25))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 26))

print()

# Exercise 'Dictionary Comprehensions'
def coaster_conversion(sozluk):
    return { coaster: round(height * 3.28084) for coaster, height in sozluk.items() }
coasters = {
  "Kingda Ka": 139,
  "Top Thrill Dragster": 130,
  "Superman: Escape From Krypton": 126
}
print(coaster_conversion(coasters))

print()

# Exercise 'Dictionary Comprehensions'
def stations_to_numbers(sozluk):
    return { channel: number for number, channel in sozluk.items() }
channels = {
  2: "CBS",
  4: "NBC",
  5: "FOX",
  7: "ABC"
}
print(stations_to_numbers(channels))

print()

# Exercise 'Set Basics'
def remove_duplicates(ls):
    return list(set(ls))
print(remove_duplicates([1, 2, 1, 2]))
print(remove_duplicates([1, 2, 3, 4]))

print()

# Exercise 'Instance Methods'
class Musician():
    def __init__(self, age, income):
        self.age = age
        self.income = income
    def enter_club(self):
        if self.age < 21:
            return "Access denied!"
        else:
            return "Access granted!"
    def play_show(self):
        self.income += 5

cliff = Musician(age = 27, income = 0)
print(cliff.age)    # 27
print(cliff.enter_club())  # "Access granted!"
print(cliff.income) # 0
cliff.play_show()
print(cliff.income) # 5
cliff.play_show()
print(cliff.income) # 10

print()

# Exercise 'Protected Attributes'
class Book():
    def __init__(self, author, publisher, page_count):
        self._author = author
        self._publisher = publisher
        self.page_count = page_count
    def copyright(self):
        return "Copyright " + self._author + ", " + self._publisher
    def rip_in_half(self):
        if self.page_count > 1:
            self.page_count /= 2
        else:
            self.page_count = 0

book = Book(author = "Grant Cardone", publisher = "10X Enterprises", page_count = 10)

print(book.copyright()) # Copyright Grant Cardone, 10X Enterprises

print(book.page_count) # 10
book.rip_in_half()
print(book.page_count) # 5.0
book.rip_in_half()
print(book.page_count) # 2.5
book.rip_in_half()
print(book.page_count) # 1.25
book.rip_in_half()
print(book.page_count) # 0.625
book.rip_in_half()
print(book.page_count) # 0
book.rip_in_half()
print(book.page_count) # 0

print()

class PizzaPie():
    def __init__(self, total_slices):
        self._slices_eaten = 0
        self.total_slices = total_slices
    @property
    def slices_eaten(self):
        return self._slices_eaten
    @slices_eaten.setter
    def slices_eaten(self, slices_eaten):
        if slices_eaten < self.total_slices:
            self._slices_eaten = slices_eaten
    @property
    def percentage(self):
        return self._slices_eaten / self.total_slices

cheese = PizzaPie(8)
cheese.slices_eaten = 2
print(cheese.percentage) # 0.25

cheese.slices_eaten = 4
print(cheese.percentage) # 0.5

cheese.slices_eaten = 10 # _slices_eaten should not change because there's only 8 slices in pie
print(cheese.percentage) # 0.5

# cheese.percentage = 0.50 AttributeError çünkü setter tanımlamadık

print()

# Exercise 'Equality and String Representation'

# Part A: Instantiation

# Define a BusTrip class that is initialized with a destination, 
# a bus company, and a price for the trip. 
# Preserve the arguments as attributes on the object.
# The choice of whether to use protected attributes is up to you.
class BusTrip():
    def __init__(self, destination, company, price):
        self.destination = destination
        self.company = company
        self.price = price
# Part B: String Representation

# The string representation of a BusTrip object must be a string in the form of:
#    "You paid 24.99 to Greyhound to go to Boston.""
# In this example, “Boston” is the destination, “Greyhound” is the bus company, and 24.99 is the price.
# These are all fed in as arguments when a BusTrip object is initialized.
    def __str__(self):
        return f"You paid {self.price} to {self.company} to go to {self.destination}."
# Part C: Equality

# Implement equality logic between two different BusTrip objects.
# Two BusTrips object are considered equal if:
#   -- they have the same destination
#   -- their price is within 3 dollars of each other
# HINT: Use Python’s abs function to calculate the absolute value of a number.
    def __eq__(self, anotherObj):
        return self.destination == anotherObj.destination and abs(self.price - anotherObj.price) <= 3
# Sample Execution
boston1 = BusTrip(destination = "Boston", company = "Greyhound", price = 24.99)
boston2 = BusTrip(destination = "Boston", company = "Megabus", price = 22.99)
boston3 = BusTrip(destination = "Boston", company = "Megabus", price = 49.99)
philly  = BusTrip(destination = "Philadelphia", company = "Peter Pan", price = 12.99)

print(boston1)            # You paid 24.99 to Greyhound to go to Boston.
print(boston1 == philly)  # False - different destinations
print(boston1 == boston2) # True - same destination and insignificant price difference
print(boston1 == boston3) # False - large price difference

print()

# Exercise 'Custom Indexing and Iteration'

# Define a Car class that accepts a maker (string), model (string),
# and year (number) parameters and assigns them to respective
# attributes

# Define a Dealership class. Each Dealership object should instantiate
# with a "cars" attribute set to an empty list.

# A Dealership object should have a accept_delivery instance method
# that accepts a Car object and adds it to the Dealership's internal
# "cars" list

# Indexing into a Dealership with a number should access a specific
# Car object in the Dealership.

# An index position in a Dealership should also be overwriteable
# with a new Car object (see examples below)
import collections
Car = collections.namedtuple("Car", ["maker", "model", "year"])
class Dealership():
    def __init__(self):
        self.cars = []
    def accept_delivery(self, delivery):
        self.cars.append(delivery)
    def __getitem__(self, index):
        return self.cars[index]
    def __setitem__(self, index, value):
        self.cars[index] = value

f150 = Car(maker = "Ford", model = "F-150", year = 2019)
camry = Car(maker = "Toyota", model = "Camry", year = 2020)
porsche = Car (maker = "Porsche", model = "911 Carrera", year = 2021)

dealership = Dealership()

dealership.accept_delivery(f150)
dealership.accept_delivery(camry)

print(dealership[0].year) # 2019 -- the F150's year

dealership[0] = porsche

for car in dealership:
  print(car.maker) # Porsche, Toyota

print()

# Example 'Magic Methods'
# Declare a Newspaper class.

# Each Newspaper will have a 'pages' attribute set to an integer
# and a 'sections' attribute set to a dictionary.
# The keys in 'sections' will be strings representing a section (i.e. "Politics")
# and the values will be the starting page for that section (i.e. "A5").

# The length of a newspaper should be equal to the number of pages it holds.

# Indexing the newspaper by a section should return the starting pasge for that section.

# Make it so two newspapers are considered equal if they have the
# same number of pages AND the same number of sections

class Newspaper():
    def __init__(self, pages, sections):
        self.pages = pages
        self.sections = sections
    def __len__(self):
        return self.pages
    def __getitem__(self, key):
        return self.sections[key]
    def __eq__(self, other):
        return self.pages == other.pages and len(self.sections) == len(other.sections)

monday_sections = {
  "Politics": "A5",
  "Sports": "B2",
  "Entertainment": "C3"
}

tuesday_sections = {
  "Travel": "A5",
  "Cooking": "B2",
}

wednesday_sections = {
  "Classifieds": "A5",
  "Weddings": "B2",
  "Weather": "C3"
}

np1 = Newspaper(pages = 80, sections = monday_sections)
np2 = Newspaper(pages = 60, sections = tuesday_sections)
np3 = Newspaper(pages = 80, sections = wednesday_sections)

print(len(np1))        # 80
print(len(np2))        # 60
print(np1 == np2)      # False -- np1 has 3 sections while np2 has 2 sections
print(np1 == np3)      # True -- both have 80 pages and 3 sections
print(np1["Politics"]) # "A5"
print(np2["Cooking"])  # "B2"

print()

# Egzersiz 'The super Function'
class Musician2():
    def __init__(self, name):
        self.name = name
        self.albums = []
    def release_album(self, title):
        self.albums.append(title)
class Drummer(Musician2):
    def __init__(self, name, stamina):
        super().__init__(name)
        self.stamina = stamina

lars = Drummer(name = "Lars", stamina = 2)
print(lars.name)   # "Lars"
print(lars.stamina) # 2
print(lars.albums) # []

lars.release_album("Ride the Lightning")
print(lars.albums) # ["Ride the Lightning"]

lars.release_album("Master of Puppets")
print(lars.albums)  # ["Ride the Lightning", 'Master of Puppets']

print()

# Exersice 'Polymorphism'

import random
# In this exercise, we'll be modelling a routine for proper dental health,
# which includes brushing our teeth, flossing, and using mouthwash.
# The order of these three varies from person to person.

# Declare a DentalHealthItem class. Its initialization should set a "price"
# attribute.

# Declare a Toothbrush subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Brushing the teeth"

# Declare a Floss subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Flossing the teeth"

# Declare a Mouthwash subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Washing the teeth"

# Instantiate an instance of a Toothbrush and assign it a "toothbrush" variable.
# Instantiate an instance of a Floss and assign it a "floss" variable.
# Instantiate an instance of a Mouthwash and assign it a "mouthwash" variable.

# Declare a "dental_health_kit" variable. It should be a list that stores the three objects.

# Import the "random" module (see last lesson for reference).
# Invoke the "shuffle" function from the module, passing in the dental_health_kit list.
# This will mutate the list, randomizing the order of its elements.

# Use list comprehension to invoke the "use" method on all three objects in "dental_health_kit".
# Assign the resulting list of strings to an "actions" variable.
class DentalHealthItem():
    def __init__(self, price):
        self.price = price

class Toothbrush(DentalHealthItem):
    def use(self):
        return "Brushing the teeth"

class Floss(DentalHealthItem):
    def use(self):
        return "Flossing the teeth"

class Mouthwash(DentalHealthItem):
    def use(self):
        return "Washing the teeth"

toothbrush = Toothbrush(5.99)
floss = Floss(8.99)
mouthwash = Mouthwash(10.99)

dental_health_kit = [toothbrush, floss, mouthwash]
actions = []
random.shuffle(dental_health_kit)

for action in dental_health_kit:
    actions.append(action.use())
print(actions)

print()

# Exercise 'Creating Mocks'
from unittest.mock import Mock

# Let's mock a fake Airport object.
# Create a Mock object and assign it to a variable called 'airport'. 

# The airport mock should have a 'gates' attribute set to a list of the strings “A1”, “B2”, and “C3”.

# The airport mock should have a 'departures' attribute set to a dictionary where 
# the keys are strings representing cities and the 
# values are strings representating their departure times.

# {
#   "Atlanta": "12:00PM",
#   "Nashville": "04:30PM"
# }

# The airport mock should have a 'close' attribute that is callable (i.e. an instance method). 
# When invoked, it should return the string “Closing”.

# The airport should have an 'open' attribute that is callable (i.e. an instance method). .
# When invoked the first time, it should return “Opening…”. 
# When invoked the second time, it should return “Already open”.

airport = Mock()
airport.configure_mock(
    gates = ["A1", "B2", "C3"],
    departures = { "Atlanta": "12:00PM", "Nashville": "04:30PM" }
    )
airport.close.return_value = "Closing"
airport.open.side_effect = ["Opening...", "Already open"]

print(airport.gates)      # ["A1", "B2", "C3"]
print(airport.departures) # { "Atlanta": "12:00PM", "Nashville": "04:30PM" }
print(airport.close())    # Closing
print(airport.open())     # Opening...
print(airport.open())     # Already open
