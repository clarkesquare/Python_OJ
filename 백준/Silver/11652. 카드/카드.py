import sys

input = sys.stdin.readline
cards = {}
answer = []

for _ in range(int(input())):
    n = int(input())
    if n not in cards:
        cards[n] = 1
    
    else:
        cards[n] += 1

answer = list(cards.items())

answer.sort(key= lambda x:x[0])
answer.sort(key= lambda x:x[1], reverse=True)

print(answer[0][0])