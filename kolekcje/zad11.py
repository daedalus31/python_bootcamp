nums = set()

while True:
    inp = input('Podaj liczbę: ')
    if inp == '':
        break
    elif inp.isdigit():
        nums.add(int(inp))

even_nums = set(range(0, 101, 2))

print(f'Unikalnych liczb: {len(nums)}')
print(f'Liczb parzystych w zakresie 0-100: {len(nums & even_nums)}')
