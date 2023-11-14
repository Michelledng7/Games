import sys
import random
from enum import Enum


def handgame(name='FirstPlayer'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def playgame():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class HANDGAME(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playagain = True
        while playagain:
            playerchoice = input(
                f'\n{name}, Please enter \n 1 for Rock, \n 2 for Paper, \n 3 for Scissors \n\n')

            if playerchoice not in ['1', '2', '3']:
                print(f'{name} please enter a number between 1 and 3')
                return playgame()  # Returns a recursive function call

            player = int(playerchoice)
            computerchoice = random.choice('123')
            computer = int(computerchoice)

            print(
                f"\n{name} you chose: {str(HANDGAME(player)).replace('HANDGAME.', '')}\n")
            print(
                f"Computer chose: { str(HANDGAME(computer)).replace('HANDGAME.', '')}.")

            def judge_winner(player, computer):
                nonlocal name
                nonlocal player_wins
                nonlocal python_wins
                if player == computer:
                    return '🤯 Tie game!'
                elif player == 1 and computer == 3:
                    player_wins += 1
                    return f'🥳 {name} You won'
                elif player == 2 and computer == 1:
                    player_wins += 1
                    return f'🥳 {name} You won'
                elif player == 3 and computer == 2:
                    player_wins += 1
                    return f'🥳 {name} You won'
                else:
                    python_wins += 1
                    return f'🐍 Computer won, sorry {name} 😥'

            game_result = judge_winner(player, computer)
            print(f'\n{game_result}')

            nonlocal game_count
            game_count += 1
            print(f'\nGame count: {game_count}')
            print(f'\n{name} wins: {player_wins}')
            print(f'\nPython wins: {python_wins}')
            print(f'\nPlay again? {name}')
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
                sys.exit(f'\n See ya {name}! \n')

    return playgame


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide an immersive game experience"
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The player's name"
    )
    args = parser.parse_args()

    game = handgame(args.name)
    game()
