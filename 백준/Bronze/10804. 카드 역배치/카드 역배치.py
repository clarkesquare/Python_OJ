cards = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())
    a -= 1
    cards = cards[:a] + cards[a:b][::-1] + cards[b:]

for i in cards:
    print(i, end=' ')