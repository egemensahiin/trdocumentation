from player import RandomComputerPlayer, HumanPlayer

class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # bu kısımda yukarıda oluşturduğumuz board listesini, indeksine göre
        # üç gruba ayırıyoruz ki bunlar bize 3 tane ' ' içeren listeler veriyor
        # ve her bir liste için aşağıdaki print işlemini yapıyoruz:
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            # burada da şunu yapıyoruz: baştaki ve sondaki ve | tahtamızın sınırları.
            # ortada olan olay ise, satırdaki yani list comprehension içersindeki
            # 3 liste her seferinde row olarak geliyor. biz de bunların elemanlarını
            # yani ' ' stringerini, ' | ' seperatörüyle joinliyoruz. böylece 3 adet
            # boşluk oluşmuş oluyor.
    @staticmethod # oyunla bi alakası yok statik atamak daha iyi
    def print_number_board():
        # bu number_board listesi, 0-2, 3-5 ve 6-8 aralıklarındaki sayıların stringlerinden
        # oluşan üç farklı listenin listesi. mantığı yukardakine benziyor.
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # yani; tahtada boşluk olarak görülen konumları, bir liste haline getirmiş olduk
    
    def empty_squares(self):
        return self.board.count(' ') # hatırlanacağı üzere 0, Falsie diğer bütün sayılar
        # Truthie. yani tahtada boş kare kalmayınca bu method False olacak.
    
    def make_move(self, choice, letter):
        if choice in self.available_moves():
            self.board[choice] = letter
            if self.winner(choice, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, choice, letter):
        # oyunun kazanma koşulları, bir sıra, sütun veya çaprazın tamamen aynı harf olması.

        # sıra indeksi, yapılan seçimin 3e bölümünün yuvarlanmasıyla elde edilir. mesela 5
        # için 5 / 3, 1e yuvarlanır ve 5. kare 1 indeksli sıradadır.
        row_ind = choice // 3 # // aşağı yuvarlanmış bölüm için
        # tüm sırayı elde etmek için self.board'daki bir aralığı almamız gerek:
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]): # burada bir liste oluşturuyoruz. bu liste
            # sıradaki tüm harflerin, letter'a eşitliğini kontrol ediyoruz. all fonksiyonu da
            # bir iterable yani bu durumda burdaki listede tüm elemanlar True olduğunda True
            # çıktısı veriyor.
            return True
        
        # sıra nasıl üçe bölümün yuvarlanmasıyla elde edilen indeks ise sütun da 3e bölümden
        # kalanın alınmasıyla elde edilen indekstir. mesela 5in sütunu, 5 % 3 işleminden
        # 2 olur.
        col_ind = 5 % 3
        col = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # çaprazlar biraz daha sıkıntılı. çaprazların listesini bir satırda oluşturamıyoruz ama
        # şunu biliyoruz ki 0, 4, 8 veya 2, 4, 6 aynı harf olduğunda çapraz aynı harf olmuş demek
        # eğer seçim çift değilse kontrole gerek yok:
        if choice % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diag1]) or all([spot == letter for spot in diag2]):
                return True
        
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_number_board()
    letter = 'X' # oyuncu için default harf
    while game.empty_squares(): # yani boş kare oldukça devam edecek döngü.
        # uygun oyuncudan hamle alalım:
        if letter == 'O':
            choice = o_player.get_move(game)
        else:
            choice = x_player.get_move(game)
        if game.make_move(choice, letter):
        # eğer make_move True çıktısı veriyorsa yani oyuncu geçerli bir kareye hamle
        # yaptıysa hamle yaptığını belirtelim (eğer print_game istendiyse) ve oyuncu
        # değiştirelim
            if print_game:
                print(f'{letter} made a move to {choice}')
                game.print_board()
                print('-----------------------------------------')
            if game.current_winner:
                if print_game:
                    print(f'{letter} won! Game over.')
                return letter
            letter = 'O' if letter == 'X' else 'X'
    if print_game: # eğer bu döngü bitmişse ve 94. satırdaki koşullu ifade, return yapmamışsa
        # (eğer kazanan olmazsa game.current_winner None çıktısı verir) bu durumda oyun beraberedir
        # çünkü kareler bitmiş demektir.
        print('It\'s a tie.')

if __name__ == '__main__':
    player1 = HumanPlayer('X')
    player2 = HumanPlayer('O')
    t = TicTacToe()
    play(t, player1, player2, print_game=True)