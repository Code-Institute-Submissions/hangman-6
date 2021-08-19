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

# checks if a json file exist and loads the file if it does.
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

