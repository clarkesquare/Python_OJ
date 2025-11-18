r, c = map(int, input().split())
answer = [0 for _ in range(1, 10)]

check = []
ranking = 1
for _ in range(r):
    check.append(input()[1:-1])

for i in range(c-3, -1, -1):
    tmp = 0
    for j in range(r):
        if check[j][i] != '.' and answer[int(check[j][i])-1] == 0:
            answer[int(check[j][i])-1] = ranking
            tmp = 1
    
    if tmp == 1:
        ranking += 1

print(*answer, sep='\n')