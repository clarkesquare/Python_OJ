n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0

for i in range(len(cards)-2):
    for j in range(i+1, len(cards)-1):
        for k in range(j+1, len(cards)):
            if (cards[i] + cards[j] + cards[k]) <= m and (cards[i]+cards[j]+cards[k] >= answer):
                answer = cards[i] + cards[j] + cards[k]

print(answer)