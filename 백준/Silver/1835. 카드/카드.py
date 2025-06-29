from collections import deque

n = int(input())

cards = deque()
numbers = list(range(1, n+1))

while len(numbers) != 0:
    cards.appendleft(numbers.pop())
    for _ in range(n):
        cards.appendleft(cards.pop())
    
    n -= 1

print(*cards)