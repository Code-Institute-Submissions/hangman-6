import random
import sys
import operator
import os

"""
code from Love sandwiches, for storing high scores in google sheets.
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_scores')

high_scores = SHEET.worksheet('highscores')
scores = high_scores.get_all_records()
game_score = {}


word_list = ['wares', 'soup', 'mount', 'extend', 'brown', 'computer',
             'apple', 'market', 'school', 'coin', 'money', 'dog',
             'transform', 'collect', 'party', 'friends', 'cool', 'banana',
             'cat', 'animal', 'justice', 'breakdance', 'happy', 'jump',
             'scream', 'python']


def update_score_sheet():
    """
    This function updates the google sheet with the players name and score.
    with help from stackowerflow.
    """
    keys = [str(eachvalue) for eachvalue in scores[0].keys()]
    values = [str(eachvalue) for eachvalue in scores[0].values()]
    update_score = [{'range': 'A1:Z1', 'values': [keys]},
                    {'range': 'A2:Z2', 'values': [values]}]
    high_scores.batch_update(update_score)


def clear_terminal():
    """
    Clearing the terminal.
    code from http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
    """
    os.system('cls' if os.name == 'nt' else 'clear')


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
    print('{:*^80}'.format(' WELCOME TO HANGMAN ! '))
    print('\n' * 4)
    print('{:^80}'.format(' 1: PLAY GAME '))
    print('{:^80}'.format(' 2: HIGH SCORES '))
    print('{:^80}'.format(' 3: QUIT '))
    print('\n' * 4)

    while True:
        user_choice = input(' ' * 28 + ' Please make a choice : ')
        # checks for user input to match choices.
        if user_choice == '1':
            player_info()
        elif user_choice == '2':
            clear_terminal()
            print('{:*^80}'.format(' HIGH SCORES '))
            print('\n')
            # sorts the scores in the 5 highest scores.
            ordered_player = (dict(sorted(scores[0].items(),
                              key=operator.itemgetter(1), reverse=True)[:5]))
            for key, val in ordered_player.items():
                print('{:^80}'.format(f'{key} : {val}'))
            print("\n" * 4)
            # Returns user to Welcome prompt.
            while True:
                if input(' ' * 33 + ' RETURN? (Y) : ').upper() == 'Y':
                    clear_terminal()
                    welcome()
                else:
                    print('{:^80}'.format(' Try again ! '))
        elif user_choice == '3':
            sys.exit()
        else:
            print('{:^81}'.format(' Must choose 1, 2 or 3 ! '))


def player_info():
    """
    To get each players name and update the player dict.
    """
    clear_terminal()
    tries = 0
    print('{:*^80}'.format(' Let´s play Hangman ! '))
    print('\n')
    print(display_hangman(tries))
    global user
    """
    To check if input is a char in the alphabet,
    and update the scores dict with the input and a score of 0.
    """
    while True:
        user = input(' ' * 27 + ' Please enter your name: ').upper()
        if user.isalpha():
            game_score[user] = 0
            play()
        else:
            print('{:^75}'.format(' Must choose letters '))


def play():
    """
    This function holds the game.
    """
    clear_terminal()
    word = get_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('{:*^80}'.format(' Let´s play Hangman ! '))
    print('\n')
    print('{:^80}'.format(' Good luck ' + user))
    print(display_hangman(tries))
    print('{:^80}'.format(word_completion))
    print('\n')

    while not guessed and tries > 0:
        # Getting user input
        guess = input(' ' * 25 + ' Please guess a letter or word: ').upper()
        # Checking if user input matches the letter in the "secret word".
        # and if it is a char in the alphabet.
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                clear_terminal()
                print('{:*^80}'.format(' Let´s play Hangman ! '))
                print('\n')
                print('{:^80}'.format(' You already guessed the letter '
                      + guess))
            elif guess not in word:
                clear_terminal()
                print('{:*^80}'.format(' Let´s play Hangman ! '))
                print('\n')
                print('{:^80}'.format(guess + ' is not in the word. '))
                tries -= 1
                guessed_letters.append(guess)
            else:
                clear_terminal()
                print('{:*^80}'.format(' Let´s play Hangman ! '))
                print('\n')
                print('{:^80}'.format(guess + ' is in the word! '))
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                # This code snippet is from stackoverflow.
                indices = [i for i, letter in enumerate(word)
                           if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        # Checking if user input matches the word of the "secret word".
        # and if it is a char in the alphabet.
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                clear_terminal()
                print('{:*^80}'.format(' Let´s play Hangman ! '))
                print('\n')
                print('{:^80}'.format(guess + ' is not in the word. '
                      + guess))
            elif guess != word:
                clear_terminal()
                print('{:*^80}'.format(' Let´s play Hangman ! '))
                print('\n')
                print('{:^80}'.format(guess + ' is not the word. '))
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            clear_terminal()
            print('{:*^80}'.format(' Let´s play Hangman ! '))
            print('\n')
            print('{:^80}'.format(' Not a valid guess, try again. '))
        print(display_hangman(tries))
        print('{:^80}'.format(word_completion))
        print('\n')

    if guessed:
        clear_terminal()
        print('{:*^80}'.format(' Let´s play Hangman ! '))
        print('\n')
        print(display_hangman(tries))
        print('{:^80}'.format(' Congrats ' + user +
              ', you guessed the word! You win! '))
        while True:
            play_again_win = input(' ' * 30 + ' Play Again? (Y/N) ').upper()
            if play_again_win == 'Y':
                game_score[user] += 1
                play()
            elif play_again_win == 'N':
                game_score[user] += 1
                if user not in scores[0].keys():
                    scores[0][user] = game_score[user]
                    update_score_sheet()
                    welcome()
                elif game_score[user] > scores[0][user]:
                    scores[0][user] = game_score[user]
                    update_score_sheet()
                    welcome()
                else:
                    welcome()
            else:
                print('{:^80}'.format(' Must choose Y or N '))

    else:
        clear_terminal()
        print('{:*^80}'.format(' Let´s play Hangman ! '))
        print('\n')
        print(display_hangman(tries))
        print('{:^80}'.format(' Sorry ' + user + ', you ran out of tries.' +
              ' The word was ' + word + '. Maybe next time!'))
        while True:
            play_again_lost = input(' ' * 30 + ' Play Again? (Y/N) ').upper()
            if play_again_lost == 'Y':
                play()
            elif play_again_lost == 'N':
                welcome()
            else:
                print('{:^80}'.format(' Must choose Y or N '))


def display_hangman(tries):
    """
    This function holds the different stages of user guesses
    and displays the graphic for a hangman.

    This code was taken from youtube
    """
    stages = [  # final state: head, torso, both arms, and both legs
                                """
                                    --------
                                    |      |
                                    |      O
                                    |     \\|/
                                    |      |
                                    |     / \\
                                    -
                                """,
                                # head, torso, both arms, and one leg
                                """
                                    --------
                                    |      |
                                    |      O
                                    |     \\|/
                                    |      |
                                    |     /
                                    -
                                """,
                                # head, torso, and both arms
                                """
                                    --------
                                    |      |
                                    |      O
                                    |     \\|/
                                    |      |
                                    |
                                    -
                                """,
                                # head, torso, and one arm
                                """
                                    --------
                                    |      |
                                    |      O
                                    |     \\|
                                    |      |
                                    |
                                    -
                                """,
                                # head and torso
                                """
                                    --------
                                    |      |
                                    |      O
                                    |      |
                                    |      |
                                    |
                                    -
                                """,
                                # head
                                """
                                    --------
                                    |      |
                                    |      O
                                    |
                                    |
                                    |
                                    -
                                """,
                                # initial empty state
                                """
                                    --------
                                    |      |
                                    |
                                    |
                                    |
                                    |
                                    -
                                """
    ]
    return stages[tries]


welcome()
