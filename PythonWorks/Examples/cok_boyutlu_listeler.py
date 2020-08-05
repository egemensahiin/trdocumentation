bubble_tea_flavors = [ # bu şekilde çoklu boyutlu ya da iç içe listeler daha okunur oluyor. zorunlu değil
    ["Honeydew", "Mango", "Passion Fruit"], # ama mantıklı
    ["Peach", "Plum", "Strawberry", "Taro"],
    ["Kiwi", "Chocolate"]
]

# çok boyutlu ya da iç içe listelerde mantık basit fazla anlatmaya gerek yok

print(len(bubble_tea_flavors))
print(bubble_tea_flavors[0])
print(bubble_tea_flavors[1])
print(bubble_tea_flavors[-1])
print(len(bubble_tea_flavors[1]))

# indeks ile tek bir listede tek bir elemanı çağırmak için araya parantez vs koymadan [list ind][elem ind]
print(bubble_tea_flavors[1][2])
print(bubble_tea_flavors[0][0])
print(bubble_tea_flavors[2][1])

# tüm elemanlardan tek bir yeni liste oluşturalım
all_flavors = []

for flavor_pack in bubble_tea_flavors:
    for flavor in flavor_pack:
        all_flavors.append(flavor)

print(all_flavors)