pattern = []
pattern.append([-1] * 7)
for _ in range(5):
    pattern.append([-1] + list(map(int, input().split())) + [-1])

pattern.append([-1] * 7)

x, y = map(int, input().split())
cnt = 0
chk = 0
answer = {}
tmp = {}
answer[(x+1, y+1)] = 0

while len(answer) != 0 and chk == 0:
    tmp = {}
    for k in answer:
        if pattern[k[0]][k[1]] == 1:
            chk = 1
            break
        
        else:
            pattern[k[0]][k[1]] = -1

        if pattern[k[0]-1][k[1]] != -1 and (k[0]-1, k[1]) not in tmp:
            tmp[(k[0]-1, k[1])] = ''
        
        if pattern[k[0]+1][k[1]] != -1 and (k[0]+1, k[1]) not in tmp:
            tmp[(k[0]+1, k[1])] = ''
        
        if pattern[k[0]][k[1]-1] != -1 and (k[0], k[1]-1) not in tmp:
            tmp[(k[0], k[1]-1)] = ''
        
        if pattern[k[0]][k[1]+1] != -1 and (k[0], k[1]+1) not in tmp:
            tmp[(k[0], k[1]+1)] = ''
    
    answer = tmp
    if chk != 0:
        break

    cnt += 1

if chk != 0:
    print(cnt)

else:
    print(-1)