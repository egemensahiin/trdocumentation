import math
import random

# hem bilgisyar hem de kullanıcıyı tanımlayan bir oyuncu üst sınıfı
class Player():
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        # değişiklik yapmak isteyebiliriz. o yüzden init tanımlayalım nolur nolmaz
        super().__init__(letter)

    def get_move(self, game):
        choice = random.choice(game.available_moves())
        return choice

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_choice = False
        val = None
        while not valid_choice:
            choice = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(choice)
                if val not in game.available_moves():
                    raise ValueError
                valid_choice = True
            except ValueError:
                print('Invalid choice. Try again.')
        return val