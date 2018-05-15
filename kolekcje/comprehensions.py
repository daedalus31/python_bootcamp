lst = [i / 10 for i in range(0, 11)]

st = {(i, i ** 2, i ** 3) for i in range(-10, 10)}

strs = {'ala', 'ma', 'kota'}

dct = {s: len(s) for s in strs}

print(lst)
print(st)
print(dct)
