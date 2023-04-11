from string import ascii_lowercase

alphabets = list(ascii_lowercase)
S = input()

for i in alphabets:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end= ' ')