# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import json
import sys
import operator

word_list = [
        'wares',
        'soup',
        'mount',
        'extend',
        'brown',
        'computer',
        'apple',
        'market',
        'school',
        'coin',
        'money',
        'dog',
        'transform',
        'collect',
        'party',
        'friends',
        'cool',
        'banana',
        'cat',
        'animal',
        'justice',
        'breakdance',
        'happy'
    ]
player = {'GORAN': 0}

"""
checks if a json file exist and loads the file if it does.
code for json from
http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
"""
filename = 'player.json'
try:
    with open(filename) as f_obj:
        player = json.load(f_obj)
except (FileNotFoundError, KeyError, ValueError):
    pass


def get_word():
    """
    Gets a random word from my word_list and return the word
    with the word in uppercase.
    """
    word = random.choice(word_list)
    return word.upper()


def welcome():
    """
    Displays the welcome prompt.
    And navigation to start a game or look at high scores.
    """
    print('{:*^70}'.format(' WELCOME TO HANGMAN ! '))
    print('\n' * 4)
    print('{:^68}'.format(' 1: PLAY GAME '))
    print('{:^68}'.format(' 2: HIGH SCORES '))
    print('{:^68}'.format(' 3: QUIT '))
    print('\n' * 4)

    

welcome()
