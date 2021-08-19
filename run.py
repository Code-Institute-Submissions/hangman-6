import random
import json
import sys
import operator
import os

word_list = [''' 'wares', 'soup', 'mount', 'extend', 'brown', 'computer',
             'apple', 'market', 'school', 'coin', 'money', 'dog',
             'transform', 'collect', 'party', 'friends', 'cool',
             'banana', 'cat', 'animal', 'justice', 'breakdance',
             'happy', 'jump', 'scream', 'python' ''']

player = {'GORAN': 0}


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    clear_terminal()
    print('{:*^70}'.format(' WELCOME TO HANGMAN ! '))
    print('\n' * 4)
    print('{:^68}'.format(' 1: PLAY GAME '))
    print('{:^68}'.format(' 2: HIGH SCORES '))
    print('{:^68}'.format(' 3: QUIT '))
    print('\n' * 4)

    while True:
        user_choice = input('                       Please make a choice : ')

        # checks for user input to match choice 1 or 2.
        if user_choice == '1':
            return player_info()

        elif user_choice == '2':
            clear_terminal()
            print('{:*^70}'.format(' HIGH SCORES '))
            print('\n')
            # sorts the player dict and prints out the 5 highest scores.
            ordered_player = dict(sorted(
                player.items(), key=operator.itemgetter(1),
                reverse=True)[:5])
            for key, val in ordered_player.items():
                print('{:^70}'.format(f'{key} : {val}'))
            print("\n" * 4)

            # Returns user to Welcome prompt.
            while True:
                if input('''
                          RETURN? (Y) : ''').upper() == 'Y':
                    clear_terminal()
                    welcome()
                else:
                    print('{:^70}'.format(' Try again ! '))

        elif user_choice == '3':
            sys.exit()
        else:
            print('{:^70}'.format(' Must choose 1, 2 or 3 ! '))


def player_info():
    """
    To get each players name and update the player dict.
    """
    clear_terminal()
    tries = 0
    print('{:*^70}'.format(' Let´s play Hangman ! '))
    print(display_hangman(tries))
    global user
    user = input('                       Please enter your name: ').upper()
    for name in player.keys():
        if name != user:
            player[user] = 0
            break
        else:
            pass
    return play()


welcome()
