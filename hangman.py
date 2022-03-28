#!/bin/python3

import core

MAX_MISS = 5
HIDDEN_CHAR = '_'
BOARD_WIDTH = 50
BORDER_CHAR = '#'
SPACE_CHAR = ' '

word = ""
miss_counter = 0
guessed_chars = []
guess = ''
word_guessed = False

def make_word_hidden():
    word_hidden = ""
    for char in word:
        if char in guessed_chars:
            word_hidden += char
        else:
            word_hidden += HIDDEN_CHAR
    return word_hidden

def print_board():
    miss_counter_str = f"missed: {miss_counter}/{MAX_MISS}"
    word_hidden_str = make_word_hidden()
    space_width = max(0, BOARD_WIDTH - len(miss_counter_str) - len(word_hidden_str) - 4)
    space_str = space_width * SPACE_CHAR

    print(BORDER_CHAR * BOARD_WIDTH)
    print(BORDER_CHAR + SPACE_CHAR + word_hidden_str + space_str + miss_counter_str + SPACE_CHAR + BORDER_CHAR)
    print(BORDER_CHAR * BOARD_WIDTH)

def step():
    global guessed_chars, miss_counter, word_guessed

    if guess not in guessed_chars:
        guessed_chars.append(guess)
        if guess not in word:
            miss_counter += 1

    all_chars_guessed = True
    for char in word:
        if char not in guessed_chars:
            all_chars_guessed = False
            break
    word_guessed = all_chars_guessed

word = core.read_args(1)[0]
print('\n' * 50)
print("LET'S GO!")
print()
print_board()

while not word_guessed and miss_counter < MAX_MISS:
    guess = input("your guess: ")[0]
    step()
    print()
    print_board()

print()
if word_guessed:
    print("YAY - you did it <(^_^)>")
else:
    print(f"RIP - btw, the word was '{word}' ¯\_(ツ)_/¯")
print()
