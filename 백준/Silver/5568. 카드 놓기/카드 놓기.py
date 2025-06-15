from itertools import permutations

n = int(input())
k = int(input())
pattern = {}
cards = []
chk = []

for _ in range(n):
    cards.append(input())

chk = list(permutations(cards, k))

for i in chk:
    word = ''.join(i)
    if word not in pattern:
        pattern[word] = None

print(len(pattern))