string = 'Ala ma <kota>, a kot ma Alę.'
between_brackets = False
chars_in_brackets = 0

for ch in string:
    if ch == '<':
        between_brackets = True
    elif ch == '>':
        between_brackets = False
    elif between_brackets:
        chars_in_brackets += 1

print(string)
print(chars_in_brackets)

one_liner = len(string[string.index('<')+1:string.index('>')])
print(one_liner)
