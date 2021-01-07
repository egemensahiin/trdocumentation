import random
roles_and_places = {
    "Okul": [
        "Öğretmen",
        "Öğrenci",
        "Müdür",
        "Hademe",
        "Müdür Yardımcısı",
        "Veli",
    ],
    "Hastane": [
        "Doktor",
        "Hasta Bakıcı",
        "Hemşire",
        "Hasta",
        "Başhekim",
        "Hasta Yakını",
    ],
}

places = roles_and_places.keys()
if __name__ == "__main__":
    print(random.shuffle(roles_and_places['Okul']))