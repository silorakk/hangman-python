#!/usr/bin/env python
import random

list_of_words = ['test', 'cookie', 'python', 'programming', 'stairs', 'window', 'random', 'person']

chosen_word = random.choice(list_of_words)

length = len(chosen_word)
health = 10
game_board = []


def create_game_board():
    for i in range(length):
        game_board.append('_')


def start_game(lives):
    print("Welcome to the game of Hangman!")
    print("A word has been selected from the word bank.")
    print('The word has {0} letters. You have {1} lives.'.format(length, lives))
    print(''.join(game_board))
    guesses = []
    gameon = 1
    while gameon == 1:
        guess = str(input('Please enter your guess: '))
        correct = False
        if guess in guesses:
            print("You have already guessed this letter.")
            continue
        else:
            guesses.append(guess)

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                correct = True
                game_board[i] = chosen_word[i]
                print(''.join(game_board))
                if '_' not in game_board:
                    print("Congratulations, you won the game!")
                    quit()
                    break
            elif i == len(chosen_word) - 1:
                if not correct:
                    lives = lives - 1
                    if lives == 0:
                        print('You have lost.')
                    else:
                        print("Incorrect, you have lost a live. You now have {0} lives.".format(lives))
                else:
                    correct = False


create_game_board()
start_game(health)
