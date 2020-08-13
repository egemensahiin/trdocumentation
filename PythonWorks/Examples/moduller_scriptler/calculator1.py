creator = "Egemen1"

PI = 3.14159

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def area(radius):
    return PI * radius * radius

# # çalışıp çalışmadığını test etmek için.
# print(add(1, 3))

calculator = 1

print("calculator1.py'da __name__ çıktısı:", __name__)
# __name__'den yararlanarak modül-script kontrolü:
if __name__ == "__main__":
    print("Bu satır yalnızca calculator.py'da okunacak.")
    print(subtract(3, 5))
    değişken = 5