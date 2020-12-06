# raise keywordü, özel bir hata tipi oluşturulması veya bir hata tipinin çıktısının özelleştirilmesi için kullanılır. hangi koşulda hata tipinin değiştirile-
# ceği, koşullu ifadelerle beraber raise keywordünü kullanarak belirlenebilir.
def pozitifse_topla(a, b):
    # eğer try kullanmazsak program hatadan sonra sonlanacak.
    try:
        if a <= 0 or b <= 0:
            raise ValueError("Verilen parametrelerden en az biri geçersiz! Yalnızca pozitif sayıları kullanın.") # eğer argüman vermezsek yukarıdaki koşulda Va-
            # lueError verir. argümanla besleyerek hata mesajını da özelleştiriyoruz.
        return a + b
    except ValueError as e:
        return f"Bir hata oluştu: {e}"
# hata mesajımızı değiştirdik, kodumuzu deneme bloğuna aldık. şimdi senaryoları görelim:
print(pozitifse_topla(5, 6))
print(pozitifse_topla(5, -1))
print(pozitifse_topla(-3, 6))