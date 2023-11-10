import sys
import random
from enum import Enum


def handgame():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def playgame():
        nonlocal player_wins
        nonlocal python_wins

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

            def judge_winner(player, computer):
                nonlocal player_wins
                nonlocal python_wins
                if player == computer:

                    return '🤯 Tie game!'
                elif player == 1 and computer == 3:
                    player_wins += 1
                    return '🥳 You won'
                elif player == 2 and computer == 1:
                    player_wins += 1
                    return '🥳 You won'
                elif player == 3 and computer == 2:
                    player_wins += 1
                    return '🥳 You won'
                else:
                    python_wins += 1
                    return '🐍 Computer won'

            game_result = judge_winner(player, computer)
            print('\nResult is ' + game_result)

            nonlocal game_count
            game_count += 1
            print('\nGame count: ' + str(game_count))
            print('\nPlayer wins: ' + str(player_wins))
            print('\nPython wins: ' + str(python_wins))

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

    return playgame


game = handgame()
game()
