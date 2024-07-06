word = []

for _ in range(int(input())):
    word.append(input())

word.sort()
word.sort(key = len)
print(*word, sep="\n")