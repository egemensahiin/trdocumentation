import re
import random
# 1. aşama olarak tahtayı oluşturuyoruz:
class Board(): # öncelikle tahtamızı oluşturalım.
    def __init__(self, size, num_bombs):
        self.size = size
        self.num_bombs = num_bombs

        # tahtayı oluşturalım. burada bir yardımcı metoddan faydalanıyoruz. bu sayede Board objesi
        # örneklendiğinde Board otomatik oluşmuş oluyor.
        self.board = self.make_board()
        self.values_for_board()
        
        # kazılmış alanları da takip etmemiz lazım. bu sebeple __init__ altında kazılmış alanları
        # depoladığımız bir set oluşturuyoruz. kazılmış alanları, (sat, süt) şeklinde tuple'lar olarak
        # depolayacağız.
        self.dug = set()

    def make_board(self):
        board = [[None for _ in range(self.size)] for _ in range(self.size)]
        # tahtayı oluşturduk şimdi bombaları yerleştireceğiz:
        bombs_planted = 0
        while bombs_planted < self.num_bombs: # ilk bakışta bir for döngüsü daha iyi olur gibi geliyor ama
            # for döngüsüyle bunu yaptığımızda aynı yere iki defa bomba gelmesi durumunu çözemiyoruz.
            loc = random.randint(0, self.size ** 2 - 1)
            row = loc // self.size # bunun yerine hem row hem de col için 0 ile size -1 arasında random sayılar
            col = loc % self.size  # atanabilirdi ama bu pratikte tahta, size**2 den oluşan bir indeksler dizisi
                                   # gibi düşünüldüğü için daha çok hoşuma gitti böyle. bir sayı seçiyoruz ve bu
                                   # sayının size'a bölümünün sonucu bize satırları, kalanı ise sütunları veriyor.
            if board[row][col] != '*':
                board[row][col] = '*'
                bombs_planted += 1
        return board

    def values_for_board(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == '*':
                    continue # mevcut konumda bomba varsa bi şey yapma
                self.board[r][c] = self.num_neig_bombs(r, c)

    def num_neig_bombs(self, row, col):
        # sınırların dışına çıkılmadığından emin olmak lazım bunun için for döngülerinde max ve min fonksiyonlarından
        # faydalanacağız. max, verilen iki argümandan daha büyük olanı çıkarır. yani max(0, row - 1) yaptığımızda eğer
        # 0. row'u kontrol ediyorsak -1 yerine 0 alınır. min de aynı mantıkla çalışır. yalnız min'e argüman olarak size
        # değil size - 1 vermeliyiz çünkü en son indeks size'ın 1 eksiği olur.
        num_bombs = 0
        for r in range(max(0, row - 1), min(self.size - 1, row + 1) + 1): # ekstra atrı 1, range fonksiyonu ekskluzif çalıştığı için
            for c in range(max(0, col - 1), min(self.size - 1, col + 1) + 1):
                if r == row and c == col: # başlangıç konumu, kontrol etmeye gerek yok
                    continue
                if self.board[r][c] == '*':
                    num_bombs += 1
        return num_bombs
    
    # tahtayı string olarak __str__ metodundan return ederek baya bi iş azaltıyoruz. metod karışık gözüküyor çünkü bolca list comprahension var
    # ama göründüğü kadar karışık değil aslında. ama 10x10'dan büyük tahtalarda sıkıntı ://
    def __str__(self):
        printed_board = '___|_' + '_|_'.join([str(i) for i in range(self.size)]) + '_|\n'
        for r in range(self.size):
            single_row = f'_{r}_| ' + ' | '.join([str(self.board[r][c]) if (r, c) in self.dug else ' ' for c in range(self.size)]) + ' |\n'
            printed_board += single_row
        return printed_board
    
    def dig(self, row, col):
        # önce direk kazılan alanı, kazılmışlara ekleyelim:
        self.dug.add((row, col))
        # eğer bombaysa False:
        if self.board[row][col] == '*':
            return False
        # eğer yakınında bomba varsa True:
        elif self.board[row][col] > 0:
            return True
        # kazılan yerin yakınında bomba yoksa, yakınında bomba olan noktalara kadar her yeri kaz:
        for r in range(max(0, row - 1), min(self.size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

def play(size = 10, num_bombs = 10):
    # oyunun algoritması şu aşamalardan oluşuyor:
    # 1. aşama: bir tahta oluşturup bombaları yerleştir.
    game = Board(size, num_bombs)

    # 2. aşama: nerenin kazılmak istendiğini sor.
    safe = True
    while len(game.dug) < size ** 2 - num_bombs:
        print(game)

        # 3a. aşama: kazılmak istenen alanda mayın varsa oyunu bitir ve tüm tahtayı göster:
        # 3b. aşama: kazılmak istenen alanda mayın yoksa, mayına komşu karelere kadar recursive olarak
        #            kaz, mayına komşu karelerde etrafında kaç mayın olduğu yazsın.
        # 4. aşama: oyun bitene kadar 2 ve 3a/b aşamalarını tekrarla

        # regular expression kütüphanesi, stringlerin belirli bir düzenli ifadeyle eşleşip eşleşmediğini kontrol etmemizi sağlar.
        # split fonkyonu ise stringleri belirli bir düzende bölmek için kullanılır. (syntaxı ayrı bi konu burada , ve ,den sonraki 
        # boşluklardan stringi 2 parçaya bölmek ve liste şeklinde depolamak için kullanılmış.)
        user_choice = re.split(',(\\s)*', input('Where would you like to dig? Give input as row, col: '))
        row, col = int(user_choice[0]), int(user_choice[-1])

        if row < 0 or col < 0 or row >= size or col >= size or (row, col) in game.dug:
            # eğer alan kazılmışsa veya geçersizse uyarı mesajı ver ve döngüyü baştan al:
            print("Location you want to dig isn\'t valid, try again.")
            continue

        safe = game.dig(row, col)
        if not safe: # eğer kazılan konum bombaysa dug metodu False veriyor. Bu durumda döngüyü bitir.
            break
    # while döngüsü bittiğinde, ya safe=False olmuş ve oyun kaybedilmiştir veya safe=True iken hamle yapılacak yer kalmamış ve oyun kazanılmıştır
    # safe'e koşullu bir game over yazalım:
    if safe:
        print("Congrats! You won.")
    else:
        game.dug = [(r, c) for r in range(size) for c in range(size)]
        print(game)
        print("Sorry, you dug a bomb and you are lost..")

if __name__ == '__main__':
    play()