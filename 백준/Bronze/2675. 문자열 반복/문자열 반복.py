n = int(input())

for _ in range(n):
    word = ''
    i, j = map(str, input().split())
    i = int(i)
    for k in j:
        word += k * i
    print(word)