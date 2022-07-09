'''
game: guess my birthday
LUD: 7/8/2022 6:30pm
'''
from random import randint

def guess_my_name():
    name = input("Hi! What is your name? ")
    round = 1
    while round < 6:
        guess_m, guess_y= randint(1, 12), randint(1924, 2004)
        response = input('Guess {}: {} were you born in {}/{} (Y/N)? '.format(round, name, guess_m, guess_y)).lower()
        if response == 'y':
            print('I knew it!')
            exit()
        else:
            if round == 5 and response != 'yes':
                print('I have othr things to do. Good bye.')
            else:
                print('Drat! Lemme try again!')
        round += 1

guess_my_name()