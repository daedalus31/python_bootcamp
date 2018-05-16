import sys

try:
    with open(sys.argv[1], 'r') as file:
        for index, line in enumerate(file, start=1):
            print(f'{index}: ' + line, end='')
except FileNotFoundError:
    print('Nie ma takiego pliku!')
