word = []

for _ in range(int(input())):
    word = list(input().split())
    print(*word[2::], end=' ')
    print(*word[:2:], sep=' ')