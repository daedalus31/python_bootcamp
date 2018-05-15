string = 'Ala ma kota, a kot ma Alę'
stats = {}

for ch in string.lower():
    if ch in stats:
        stats[ch] += 1
    else:
        stats[ch] = 1

for ch in stats:
    print(f'Znak "{ch}" wystąpił {stats[ch]} razy.')
