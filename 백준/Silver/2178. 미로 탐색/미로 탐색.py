n, m = map(int, input().split())
pattern = []
cnt = 0
total = {}
answer = {}
tmp = {}
chk = 0

pattern.append([0] * (m+2))
for _ in range(n):
    pattern.append([0] + list(map(int, input())) + [0])

pattern.append([0] * (m+2))

answer[(1, 1)] = ''
total[(1, 1)] = ''

while chk == 0:
    tmp = {}
    for i in answer:
        total[i] = ''
        if i[0] == n and i[1] == m:
            chk = 1
            break
        
        else:
            if pattern[i[0]-1][i[1]] == 1 and pattern[i[0]-1][i[1]] not in total and pattern[i[0]-1][i[1]] not in tmp:
                tmp[(i[0]-1, i[1])] = ''
            
            if pattern[i[0]+1][i[1]] == 1 and pattern[i[0]+1][i[1]] not in total and pattern[i[0]+1][i[1]] not in tmp:
                tmp[(i[0]+1, i[1])] = ''
            
            if pattern[i[0]][i[1]-1] == 1 and pattern[i[0]][i[1]-1] not in total and pattern[i[0]][i[1]-1] not in tmp:
                tmp[(i[0], i[1]-1)] = ''
            
            if pattern[i[0]][i[1]+1] == 1 and pattern[i[0]][i[1]+1] not in total and pattern[i[0]][i[1]+1] not in tmp:
                tmp[(i[0], i[1]+1)] = ''

    cnt += 1
    if chk != 0:
        break
    
    answer = tmp

print(cnt)