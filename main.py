import random

from pprint import pprint as pprint
from typing import List
from string import ascii_letters
from generate_words import complete_wordle_words


def choose_word(word_list):
    word = random.choice(word_list)
    return word


def create_board(char: str, width: int, height: int) -> List:
    board = [[char for _ in range(width)] for _ in range(height)]
    return board


def is_valid_word(word: str) -> bool:
    alphabet = ascii_letters.upper()
    if len(word) != 5:
        return False
    for char in word.upper():
        if char not in alphabet:
            return False
    if word not in complete_wordle_words():
        return False
    return True


def play_wordle():
    board = create_board('-', 5, 5)
    original_word = choose_word(complete_wordle_words()).upper()
    letters_used = set()
    letters_wrong_pos = set()
    n_try = 0
    winner = False
    while not winner and n_try < 5:
        if letters_wrong_pos:
            print('You guessed ', letters_wrong_pos, 'letter(s), but the position is wrong')
        if letters_used:
            print('You used letters: ', letters_used)
        pprint(board)
        user_word = input(f'Choose a 5-letter English word. This is your {n_try+1} try. You have 5 in total: ')
        while not is_valid_word(user_word):
            user_word = input("Choose only valid words: ")
        user_word = user_word.upper()
        for i, letter in enumerate(user_word):
            letters_used.add(letter)
            for j, char in enumerate(original_word):
                if letter == char and i == j:
                    board[n_try][i] = letter
                    if board[n_try] == list(original_word):
                        pprint(board)
                        winner = True
                if letter == char and i != j:
                    letters_wrong_pos.add(letter)
        n_try +=1

    if winner:
        play_next = input(f'Success, you are a genius! The word was {original_word}. Play with another word? (yes/no): ')
        if play_next == 'yes':
            play_wordle()
    else:
        play_next = input(f'You lost. The word was {original_word}. Play with another word? (yes/no):')
        if play_next == 'yes':
            play_wordle()






if __name__ == '__main__':
    play_wordle()



