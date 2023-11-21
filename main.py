import os

try:
    if os.path.exists('project.txt'):
        f = open('context.txt', 'a')
        f.write('\nHi my name is creek!!!!')
except FileNotFoundError as error:
    print(f'{error}')

# print(len('Hi my name is creek!!!!'))
