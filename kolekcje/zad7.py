string = 'To jest jakiś napis, w którym będę liczyć samogłoski.'

vowels = 0
for ch in string.lower():
    if ch in 'aeiouyąęó':
        vowels += 1

print(f'Napis: "{string}" \nSamogłoski: {vowels}')
