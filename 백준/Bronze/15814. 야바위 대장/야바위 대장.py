word = list(input())

for _ in range(int(input())):
    a, b = map(int, input().split())
    word[a], word[b] = word[b], word[a]

print(*word, sep='')