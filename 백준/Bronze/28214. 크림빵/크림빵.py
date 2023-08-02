n, k, p = map(int, input().split())
bread = list(input().split())
answer = 0

for i in range(0, (len(bread))+1, k):
    if bread[i:i+k:].count('1') >= p:
        answer += 1

print(answer)