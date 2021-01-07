import os
import sys
import time
import random
from roles import roles_and_places, places

class Player():
    def __init__(self, name):
        self.name = name
        self.place = str()
        self.role = str()
        self.isspy = False
    
    def show_role(self, limit = 5):
        print(f"Mekanı ve rolünüzü gördükten {limit} saniye sonra, bu mesaj kendini imha edecek.")
        print("????" if self.isspy else self.place + " için Mekan: " + self.place)
        print(self.name.title() + " için Rol: " + self.role)
        time.sleep(limit)
        os.system("cls" if os.name == "nt" else "clear")
    
    def __str__(self):
        return f"{self.name} adlı oyuncunun {self.place} mekanındaki rolü {self.role}."
    
    def __eq__(self, isequal):
        return self.name == isequal

class Game():
    def __init__(self):
        self.players = []
    
    def randomize_roles(self):
        place = random.choice(list(places))
        random.shuffle(roles_and_places[place])
        for i, player in enumerate(self.players):
            player.place = place
            player.role = roles_and_places[place][i]
        spy = random.choice(self.players)
        spy.isspy = True
        spy.role = 'Casus'

def play(num_players = 6, time_limit = 300): 
    game = Game()
    num = 1
    choice = str()
    start_or_not = str()
    result = str()
    while len(game.players) < num_players:
        name = input(f"Lütfen {num} numaralı kullanıcının adını giriniz: ").lower()
        if name in game.players:
            print("Aynı isim iki defa girilemez. lütfen başka bir isim giriniz.")
            continue
        game.players.append(Player(name))
        num += 1
    game.randomize_roles()
    os.system("cls" if os.name == "nt" else "clear")
    for player in game.players:
        while choice != "g":
            choice = input(f"{player.name.title()} isimli oyuncu, rolünü ve mekanı görmek için (G) yazsın: ").lower()
        choice = str()
        player.show_role()
    print("Oyuncular: " + ", ".join([player.name for player in game.players]))
    while start_or_not != "y":
        start_or_not = input(f"Süre ({time_limit / 60} dk) başlatılsın mı? (Y): ").lower()
    for remaining_time in range(time_limit):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} saniye.".format(time_limit - remaining_time))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\r")
    print("Süre doldu.")
    while result not in [player.name for player in game.players]:
        result = input("Grup kararı nedir?" ).lower()
        if result not in [player.name for player in game.players]:
            print("Girdiğiniz isim oyuncular arasında yok. Tekrar deneyin.")
            continue
    
    for player in game.players:
        if player.role == 'Casus':
            spy = player.name
            break
    
    if spy == result:
        print("Tebrikler casusu buldunuz!")
    else:
        print(f"Casusu bulamadınız. Gerçek casus {spy.title()} idi.")

if __name__ == "__main__":
    play()