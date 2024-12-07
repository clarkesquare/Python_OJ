n, m = map(int, input().split())
garo = [0, n]
sero = [0, m]
answer = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 0:
        sero.append(b)
    
    else:
        garo.append(b)

garo.sort()
sero.sort()
for i in range(1, len(garo)):
    for j in range(1, len(sero)):
        tmp = (garo[i] - garo[i-1]) * (sero[j] - sero[j - 1])
        if tmp > answer:
            answer = tmp

print(answer)