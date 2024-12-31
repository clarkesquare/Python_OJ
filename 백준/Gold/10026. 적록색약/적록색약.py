n = int(input())
pattern = []
total = [0, 0]

pattern.append(['?'] * (n+2))

for _ in range(n):
    pattern.append(['?'] + list(input()) + ['?'])

pattern.append(['?'] * (n+2))

# 일반
checking = {}
answer = {}
tmp = {}
chk = ''
for i in range(1, n+1):
    for j in range(1, n+1):
        # 적록
        chk = ''
        if (i, j) not in checking:
            chk = pattern[i][j]
            answer[(i, j)] = ''

        while (len(answer)) != 0:
            tmp = {}
            for k in answer:
                checking[(k[0], k[1])] = ''
                if pattern[k[0]-1][k[1]] in chk and (k[0]-1, k[1]) not in tmp and (k[0]-1, k[1]) not in checking:
                    tmp[(k[0]-1, k[1])] = ''
                
                if pattern[k[0]+1][k[1]] in chk and (k[0]+1, k[1]) not in tmp and (k[0]+1, k[1]) not in checking:
                    tmp[(k[0]+1, k[1])] = ''
                
                if pattern[k[0]][k[1]-1] in chk and (k[0], k[1]-1) not in tmp and (k[0], k[1]-1) not in checking:
                    tmp[(k[0], k[1]-1)] = ''
                
                if pattern[k[0]][k[1]+1] in chk and (k[0], k[1]+1) not in tmp and (k[0], k[1]+1) not in checking:
                    tmp[(k[0], k[1]+1)] = ''
            
            answer = tmp
        
        if chk != '':
            total[0] += 1


# 적록색약
checking = {}
answer = {}
tmp = {}
chk = ''
for i in range(1, n+1):
    for j in range(1, n+1):
        # 적록
        chk = ''
        if (pattern[i][j] == 'R' or pattern[i][j] == 'G') and (i, j) not in checking:
            chk = 'RG'
            answer[(i, j)] = ''

        # 파
        elif pattern[i][j] == 'B' and (i, j) not in checking:
            chk = 'B'
            answer[(i, j)] = ''
        
        while (len(answer)) != 0:
            tmp = {}
            for k in answer:
                checking[(k[0], k[1])] = ''
                if pattern[k[0]-1][k[1]] in chk and (k[0]-1, k[1]) not in tmp and (k[0]-1, k[1]) not in checking:
                    tmp[(k[0]-1, k[1])] = ''
                
                if pattern[k[0]+1][k[1]] in chk and (k[0]+1, k[1]) not in tmp and (k[0]+1, k[1]) not in checking:
                    tmp[(k[0]+1, k[1])] = ''
                
                if pattern[k[0]][k[1]-1] in chk and (k[0], k[1]-1) not in tmp and (k[0], k[1]-1) not in checking:
                    tmp[(k[0], k[1]-1)] = ''
                
                if pattern[k[0]][k[1]+1] in chk and (k[0], k[1]+1) not in tmp and (k[0], k[1]+1) not in checking:
                    tmp[(k[0], k[1]+1)] = ''
            
            answer = tmp
        
        if chk != '':
            total[1] += 1

# 답 출력
print(*total)