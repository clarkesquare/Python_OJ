cows = []
max = 0
n = int(input())
answer = [0, 0]

for _ in range(n):
    cows.append(list(map(int, input().split())))

for i in range(n-1):
    for j in range(i+1, n):
        tmp = abs(cows[i][0] - cows[j][0]) + abs(cows[i][1] - cows[j][1])
        if tmp > max:
            max = tmp
            answer = [i+1, j+1]

print(*answer)