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

# burada tanımladığımız RandomComputerPlayer sadece rastgele hamleler yapıyor ve genelde
# kaybediyor. bunu önlemek için minimax adı verilen bir algoritma kullanarak bilgisayarın her
# zaman en iyi hamleyi yapmasını sağlamak mümkündür.

# minimax kelimesi minimum-maximumdan türemiştir. sıfır kazançlı yani bir tarafın kazanmasının,
# diğer tarafın kaybetmesi anlamına gelen ve sonuçta sıfır toplamla bitan oyunlarda, oyun sonunun
# öngörülmesi için kullanılan bir algoritmadır. satranç, go, tictactoe gibi masa oyunları, sıfır
# kazançlı oyunların güzel örneklerindendir. algoritmayı anlamak için önce bir minimax ağacı çizmek
# gerekir. örnek bir ağaç üzerinden durumu daha iyi anlatabiliriz.
#                                   | O | O | X |   # hamle sırası Xte iken 3 adet boş kare yani
# İncelenen Konum  (1)              | X |   | O |   # Xin yapabileceği 3 adet hamle vardır.
#                                   |   |   | X |
#                                     |   |   |
#                                    /    |   \
#                  -----------------      |    ----------------------
#                 |                       |                          |
#          | O | O | X |            | O | O | X |              | O | O | X |        # O'nun hamle sırasında
# X oynar  | X | X | O | (2)        | X |   | O | (3)          | X |   | O | (4)    # oynayabileceği 2 kare
#          |   |   | X |            |   | X | X |              | X |   | X |        # kalmıştır. yani her bir
#            /       \                /      \                   /      \           # dal için ikişer dal daha
#           |        |               |       |                  |       |           # iner
#  O    |O|O|X|   |O|O|X|         |O|O|X|  |O|O|X|          |O|O|X|   |O|O|X|       
# Oynar |X|X|O|(5)|X|X|O| (6)  (7)|X| |O|  |X|O|O|(8)    (9)|X|O|O|   |X| |O|(10)   # her bir durumda X için bir
#       | |O|X|   |O| |X|         |O|X|X|  | |X|X|          |X| |X|   |X|O|X|       # hamle kalmıştır. buradan sonrası
#          |         |              |         |                |         |          # kazanç, kayıp veya beraberliği belirliyor.
#  X    |O|O|X|   |O|O|X|         |O|O|X|  |O|O|X|          |O|O|X|   |O|O|X|    
# Oynar |X|X|O|   |X|X|O|->0   0<-|X|X|O|  |X|O|O|->1    1<-|X|O|O|   |X|X|O|->1    # şimdi bu hamlelerin hepsinde artık oyun
#    1<-|X|O|X|   |O|X|X|         |O|X|X|  |X|X|X|          |X|X|X|   |X|O|X|       # bitti. bu sebeple artık incelemeye geçebiliriz
#                                                                                   # burada kazanç oyunlara 1 beraberliklere 0 kayıp
#                                                                                   # oyunlara -1 veriyoruz. 
# işin minimax kısmına geldik. Xin en iyi hamlesini belirlemek için ağacın en altından en üstüne doğru gitmemiz lazım. üste
# doğru giderken eğer hamleyi yapan X ise üste maximun olan sayıyı geçiriyoruz. çünkü X kendisi için maximun kazancı hedefler.
# fakat hamle sırası O'da ise bu sefer minimum olasılığı yukarı geçiriyoruz çünkü O'nun, X için minimum kazancı hedeflediğini
# farzediyoruz. Son sıradan bi yukarı node'a çıkarken zaten son hamle olduğu için doğrudan aynı sayılar geçecek. yani
# 5 => 1 | 6 => 0 | 7 => 0 | 8 => 1 | 9 => 1 ve 10 => 1 olur. O'nun oynadığı node'a geldiğimizde ise en üste çıkarken bu defa
# minimum olanı geçiriyoruz. yani 5 ve 6dan, 2ye geçerken 0, 7 ve 8den 3e geçerken 0 ve 9 ile 10dan 4e geçerken 1i alıyoruz
# son durumda 2 => 0 | 3 => 0 | 4 => 1 oluyor. şimdi de köke yani ilk duruma gideceğiz ve en iyi hamleyi belirleyeceğiz.
# burada X oynar hamlesinde olduğumuz maximumu seçmemiz gerek yani 4'ü seçeceğiz. sonuç olarak 1 numaralı konumda Xin yapabi-
# leceği en iyi hamle, 4 numaralı hamle olarak saptanmış oluyor.

# puanlamaları yaparken, hamle uzunluğunu hesaba katmak da faydalı bir pratiktir. bu durumda bilgisayar, sadece kazancı değil
# en kısa yoldan kazancı hedefleyecektir. bunu yapmak için puanlamaya bir parametre olarak hamle sayısı da eklenmelidir ki
# kalan hamle sayısı, kalan boş kare sayısının bir fonksiyonudur. başka bir ilk konumdan yola çıkarak bir ağaç daha oluşturabiliriz
#                                                  | X | O | X |
#              Ilk durum                           | X | O |   |
#                                                  |   |   | O |
#                                                   |   |   |
#      MAXIMIZER                    (-2)           /    |   \             (0)
#  (üste maximum)               -----------------/      |    \----------------------
#                              /                     (3)|                           \
#                      | X | O | X |             | X | O | X |               | X | O | X | 
# X oynar              | X | O | X |             | X | O |   |               | X | O |   |
#                      |   |   | O |             | X |   | O |               |   | X | O |
#     MINIMIZER     (0) |       |(-2)            UF=1*(2+1)=3              (1) |       | (0)
# (üste minimum)       /        \                                             /        \
#              | X | O | X |     | X | O | X |                      | X | O | X |      | X | O | X |
# O oynar      | X | O | X |     | X | O | X |                      | X | O | O |      | X | O |   |
#              | O |   | O |     |   | O | O |                      |   | X | O |      | O | X | O |
#    MAXIMIZER       | (0)       UF=-1*(1+1)=-2                           | (1)              | (0)
# (üste max)   | X | O | X |                                        | X | O | X |      | X | O | X |
# X oynar      | X | O | X |                                        | X | O | O |      | X | O | X |
#              | O | X | O |                                        | X | X | O |      | O | X | O |
#             UF=0*(0+1)=0                                          UF=1*(0+1)=1       UF=0*(0+1)=0
#
# yukarıdaki karar ağacında oyun sonu için çok daha fazla olasılık var. X kaybedebilir, 1 veya 2 hamlede kazanabilir veya oyun
# berabere bitebilir. bu gibi bir durumda, hamlelerin puanlanması için 1, 0, -1 sistemi yetersiz kalır çünkü yararı doğru şekilde
# saptayamaz. bunun için bir yarar fonksiyonu (utility function) oluşturulmalıdır. yarar fonksiyonu, durumun kazanç veya kayıp
# olmasını ve bu duruma kaç kaç hamlede gelindiğini içermelidir. bunun için de, konumun durumunu (1, 0 veya -1) tahtada kalan
# boş kare sayısının 1 fazlası ile (son konumda kazancın 0 değil 1 olması için 1 fazlası) çarpmamız gerekiyor. daha sonra yukardaki
# gibi Xin hamlelerinden maksimum, Onun hamlelerinden minimumları alarak köke kadar çıkmamız gerek.
# yani en avantajlı hamle, bize +3 utility fonksiyonu veren hamle oluyor.
#
# şimdi bunu kodumuza yerleştirmemiz lazım
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # eğer tüm konumlar boşsa rastgele hamle yapması yeterli. daha fazlasına gerek yok
        if len(game.available_moves()) == 9:
            choice = random.choice(game.available_moves())
        else:
            # burada ise oynanacak kareyi minimax algoritmasına göre belirlememiz lazım. bunun için minimax
            # adı verilen bi metod oluşturacağız ve bunu burada çağıracağız.
            choice = self.minimax(game, self.letter)['position'] # çıktı olarak sözlük alıyoruz pozisyon değil.
        return choice
    # def minimax(self, state, player):
    #     max_player = self.letter  # yourself
    #     other_player = 'O' if player == 'X' else 'X'

    #     # first we want to check if the previous move is a winner
    #     if state.current_winner == other_player:
    #         return {'position': None, 'score': 1 * (len(state.available_moves()) + 1) if other_player == max_player else -1 * (len(state.available_moves()) + 1)}
    #     elif not state.empty_squares():
    #         return {'position': None, 'score': 0}

    #     if player == max_player:
    #         best = {'position': None, 'score': -math.inf}  # each score should maximize
    #     else:
    #         best = {'position': None, 'score': math.inf}  # each score should minimize
    #     for possible_move in state.available_moves():
    #         state.make_move(possible_move, player)
    #         sim_score = self.minimax(state, other_player)  # simulate a game after making that move

    #         # undo move
    #         state.board[possible_move] = ' '
    #         state.current_winner = None
    #         sim_score['position'] = possible_move  # this represents the move optimal next move

    #         if player == max_player:  # X is max player
    #             if sim_score['score'] > best['score']:
    #                 best = sim_score
    #         else:
    #             if sim_score['score'] < best['score']:
    #                 best = sim_score
    #     return best
    def minimax(self, state, player): # burada game yerine state dedik çünkü daha anlaşılır. metod oyunun genelini değil, oyunun
        # o an alınmış bir görüntüsünü değerlendiriyor. tamamen anlamsal yani aslında gene oyunun kendisi ama state demek daha
        # anlaşılır.
        # iki nitelik tanımlayacağız. maximum player yani biz ve other player yani rakip:
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X' # BURAYA DIKKAT! yanlışlıkla burda max_player yaptığımda rastgelenin bi tık iyisi
        # gibi oynuyodu. büyük ihtimalle ilk hamle tahmininden sonra other_player değişmediği için bu durum oluyodu.
        # öncelikle mevcut konumda bir kazanan olup olmadığını kontrol edelim ki oyun bittiyse boşa yorulmayalım:
        # minimax fonksiyonu recursive bi fonksiyon yani kendi içinde tekrarlanan bir fonksiyon ve her tekrarda max player ve other
        # player değişiyor. rakibin oynadığı pozisyonları hesaplarken rakip max player, biz ise other player olacağız. bu sebeple,
        # 137de, eğer rakip, max player ise score -1 ile çarpılmalı, değilse +1 ile çarpılmalı (ifli ifadenin sebebi)
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (len(state.available_moves()) + 1) if other_player == max_player else -1 * (len(state.available_moves()) + 1)
            }
        elif not state.available_moves(): # yani hiç hamle kalmamış ve current_winner yok ise yani incelenen konum berabere ise:
            return {'position': None, 'score': 0}
        # eğer kazanan yoksa ve boş kareler varsa buradan sonrasına devam edecek fonksiyon. o yüzden else koymaya gerek yok
        # zaten kısıtlayıcı durumlarda fonksiyon, uygun sözlükleri return edeceği için bitecek ve gerisi okunmayacak
        # önce temel sözlüklerimizi oluşturalım. bunlar. pozisyonu None, score'u da default olarak -sonsuz (oyuncu max player ise
        # hamle yapılmaması -sonsuz yani her halükarda küçük kalsın diye) veya +sonsuz (rakip max player ise) olarak içeren
        # sözlüklerdir. bu değerleri oyunun durumuna göre güncelleyeceğiz fonksiyonun ilerleyen aşamalarında.
        if player == max_player:                                 # sonsuzların kullanılmasının sebebi, hamle yapılmayan koşulu
            best_choice = {'position': None, 'score': -math.inf} # her halükarda hamle yapılan koşuldan küçük veya büyük kılmak
        else:                                                    # bu sebeple max oyuncu biz isek -math.inf rakip ise +math.inf
            best_choice = {'position': None, 'score': math.inf}  # oluyor. burası biraz karışık anlamak önemli
        # şimdi de tüm olası hamleleri kontrol edeceğiz. bunun için mümkün olan hamleleri yani boş konumları for döngüsüyle taramak
        # gerekir.
        for possible_move in state.available_moves():
            # bu hamleyi yapmış olduğumuzu farz edeceğiz. hatırlanacağı üzere TicTacToe sınıfında make_move fonksiyonu ile hamle
            # yapacağız:
            state.make_move(possible_move, player)
            # hamle yapıldıktan sonra score'u simüle etmemiz lazım. şimdi state üzerinde make_move çalıştırdıktan sonra artık state,
            # bu hamlenin yapıldığı konum oluyor. buradan sonra diğer oyuncuyla tekrar minimax çalıştırmamız gerekiyor. işin recursion
            # kısmı da bu kısım. minimax iki argüman alıyor: state ve player. bu sefer yeni state ile other playerı kullanacağız:
            sim_score = self.minimax(state, other_player)
            # bu recursion bittiğinde yani kazanma-kaybetme-beraberlik koşuluna kadar tarandıktan sonra pozisyonu sıfırlamamız lazım
            # ki sonraki olası hamleyi denerken ilk pozisyon hesaplansın. ayrıca kazananı da sıfırlamamız lazım.
            state.board[possible_move] = ' '
            state.current_winner = None
            # burada da sim_score sözlüğündeki pozisyon değişkenini, possible_move yapıyoruz ki sonuçta elde edilen pozisyon elemanı
            # denenen hamleyi temsil etsin:
            sim_score['position'] = possible_move
            # artık sim_score; döngüde denenen hamleyi ve hamle sonucu elde edilen score'u içeren iki elemanlı bir sözlük oldu.
            # eğer bu hamlenin score'u, mevcut hesaplanmış en iyi score'dan (best_choice) daha iyiyse bu sim_score sözlüğünü, best
            # choice yapacağız. fakar burda oyuncunun kim olduğunu da kontrol etmemiz gerek. eğer max_player biz isek, daha büyük
            # olan score'u, rakip ise daha küçük olan score'u alacağız çünkü rakip max_player iken bizim için en kötü olan hamleyi
            # yani score'u en küçük hamleyi yapacağını varsayıyoruz.
            if player == max_player:
                if sim_score['score'] > best_choice['score']:
                    best_choice = sim_score
            else:
                if sim_score['score'] < best_choice['score']:
                    best_choice = sim_score
        return best_choice # SONUNDA BİTTİ anlamak için bi baştan oku :'D