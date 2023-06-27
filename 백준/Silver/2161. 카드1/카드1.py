n = int(input())
answer = []
cards = list(range(1, n+1))

while len(cards) >= 2:
    answer.append(cards[0])
    cards.remove(cards[0])
    cards.append(cards[0])
    cards = cards[1::]

answer = answer + cards
print(*answer)