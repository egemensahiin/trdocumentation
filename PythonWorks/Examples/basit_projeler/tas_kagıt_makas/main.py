import random
def is_win(player, opponent):
    # winning conditions: r s, s p, p r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def play():
    user = input(f'What is your choice? (r) for rock, (s) for scisoors and (p) for paper: \n')
    computer = random.choice(['r', 's', 'p'])
    if user == computer:
        return 'It is a tie.'
    if is_win(user, computer):
        return f'Congrats! Computer choosed ({computer}) and you won.'
    return f'Computer choosed ({computer}) and you lost! :/'

print(play())