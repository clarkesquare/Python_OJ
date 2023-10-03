n = list(map(int, input()))
answer = ''

for i in range(len(n)-1, 0, -1):
    if n[i] >= 5:
        n[i-1], n[i] = n[i-1]+1, 0
    else:
        n[i] = 0

for j in n:
    answer += str(j)

print(answer)