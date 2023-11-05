cambridge = 'CAMBRIDGE'

word = list(input())

for i in range(len(word)):
    if word[i] not in cambridge:
        print(word[i], end='')