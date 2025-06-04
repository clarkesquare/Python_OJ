from itertools import permutations

chk = input()
word = sorted(list(chk))
pattern = list(permutations(word, len(word)))[::-1]
chk = tuple(list(chk))
answer = 0

if chk in pattern and chk != pattern[0]:
    print(*pattern[pattern.index(chk) - 1], sep='')

else:
    print(0)