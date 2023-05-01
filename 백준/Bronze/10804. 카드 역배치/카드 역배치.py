cards = list(range(1, 21))
answer = []

for _ in range(10):
    a, b = map(int, input().split())
    a -= 1
    answer = cards[:a] + cards[a:b][::-1] + cards[b:]
    cards = answer

for i in answer:
    print(i, end=' ')