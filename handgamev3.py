import sys
import random
from enum import Enum


def playgame():
    class HANDGAME(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playagain = True
    while playagain:
        playerchoice = input(
            '\nPlease enter \n 1 for Rock, \n 2 for Paper, \n 3 for Scissors \n\n')

        if playerchoice not in ['1', '2', '3']:
            print('You must enter a number between 1 and 3')
            return playgame()  # Returns a recursive function call

        player = int(playerchoice)

        computerchoice = random.choice('123')
        computer = int(computerchoice)

        print('\nYou chose: ' + str(HANDGAME(player)
                                    ).replace('HANDGAME.', '') + '.\n')
        print('Computer chose: ' + str(HANDGAME(computer)
                                       ).replace('HANDGAME.', '') + '.')

        if player == computer:
            print('🤯 Tie game!')
        elif player == 1 and computer == 3:
            print('🥳 You won')
        elif player == 2 and computer == 1:
            print('🥳 You won')
        elif player == 3 and computer == 2:
            print('🥳 You won')
        else:
            print('🐍 Computer won')

        print('\nPlay again?')
        while True:
            playagain = input('\nY for yes or \nQ to quit: \n')
            if playagain.lower() not in ['y', 'q']:
                continue
            else:
                break
        if playagain.lower() == 'y':
            return playgame()
        else:
            print('\n🎉🎉🎉🎉 Thanks for playing!\n')
            sys.exit('\n See ya! \n')


playgame()
