import random # rastgele sayılar elde etmek için

higher = 0
choice = ''

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} '))
        if guess < random_number:
            print(f'The number {guess} is too low')
        elif guess > random_number:
            print(f'The number {guess} is too high')
    print(f'Congrats! You guessed the number {random_number} correctly!')

def computer_guess(x):
    low = 1
    high = x
    guess = 0
    feedback = ''
    while feedback != 'c':
        if low != high: # eşit range'de randint hata veriyor.
            guess = random.randint(low, high)
        else:
            guess = low # high da yazılsa farketmez zaten eşitlik koşulu
        feedback = input(f'Is number {guess} too high (H), too low (L) or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Computer guessed number {guess} correctly!')

while choice != 'g' and choice != 'c':
    choice = input('Which one do you want to play? Guess (G) or Computer Guess (C) ').lower()
    if choice != 'g' and choice != 'c':
        print(f'Your choice ({choice}) is not valid. Please give another choice.')

while higher <= 1:
    higher = int(input('What is the higher (higher than 1) number do you want to play with? '))
    if higher <= 1:
        print(f'The higher number you gave {higher} is not valid. Please give another number.')


if choice == 'g':
    guess(higher)
elif choice == 'c':
    computer_guess(higher)