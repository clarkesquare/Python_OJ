cows = {}

for _ in range(int(input())):
    tmp = tuple(sorted(input().split()))
    if tmp not in cows:
        cows[tmp] = 1
    else:
        cows[tmp] += 1

cows = list(cows.items())
cows.sort(key= lambda x:x[1], reverse=True)

print(cows[0][1])