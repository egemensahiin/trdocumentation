import random
import string
from words import words

def get_valid(words):
    word = random.choice(words)
    if (' ' in word) or ('-' in word):
        word = random.choice(words)
    return word.upper()

def hangman():
    lives = 6
    word = get_valid(words)
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    while len(word_letters) > 0 and lives > 0:
        state = [letter if letter in used_letters else '_' for letter in word]
        print(f'You have {lives} lives left.')
        print('Letters you used are: ', ' '.join(used_letters))
        print('Word in current state: ', ' '.join(state))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in used_letters:
            print(f'You used that letter ({user_letter}) before.')
        elif user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters: 
                print('Congrats! You gussed a letter correct.')
                word_letters.remove(user_letter)
            else:
                print('Letter you guessed is wrong.')
                lives -= 1
        print('---------------------------------------------------------')
    if lives == 0:
        print(f'Your journey ends here. The word was {word}. You Lost.')
    elif word_letters == used_letters:
        print(f'Congrats! You found the word {word} right. You Won!')

hangman()