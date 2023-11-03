import sys
import random
from enum import Enum


class HANDGAME(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True
while playagain:
    playerchoice = input(
        '\nPlease enter \n 1 for Rock, \n 2 for Paper, \n 3 for Scissors \n\n')
    player = int(playerchoice)

    computerchoice = random.choice('123')
    computer = int(computerchoice)

    if player > 3 or player < 1:
        sys.exit('You must enter a number between 1 and 3')

    print('\nYou chose: ' + str(HANDGAME(player)).replace('HANDGAME.', '') + '.\n')
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

    playagain = input('\nPlay again? (y/n): \n')
    if playagain.lower() == 'y':
        continue
    else:
        playagain = False
        print('\n🎉🎉🎉🎉 Thanks for playing!\n')
sys.exit('\n See ya! \n')
