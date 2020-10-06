# dosyaların üstüne yazmak yerine dosyaya yeni veri eklemek istediğimiz durumlarda ikinci argüman olarak dosyayı açarken "w" değil "a" yani
# sonuna eklemek anlamında append ile dosya açılır.
with open("doludosya.txt", "a") as dosya:
    # sonuna eklemek için de dosya objesi üzerinde write metodu çalıştırılır.
    dosya.write("İkinci satıra bunu ekledim.")
    # dosyaya bakıldığında da görülebileceği gibi yukarıdaki string, dosyanın üzerine yazılmadı, sonuna eklendi.
    # yeni satır eklemek için yine escape karakterlerden faydalanılır:
    dosya.write("\nBu da üçüncü satır.")

# yine "w" ile açılan dosyalarda olduğu gibi "a" ile açılan dosyalar da eğer söz konusu konumda mevcut değilse oluşturulur.
with open("biryenidosyadaha.txt", "a") as dosya:
    dosya.write("Bu da yeni bir txt.")