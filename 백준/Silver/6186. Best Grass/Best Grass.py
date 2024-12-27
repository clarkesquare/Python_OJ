n, m = map(int, input().split())
chk = 0
total = 0

pattern = []
answer = {}
tmp = {}
pattern.append(['.'] * (m+2))
for _ in range(n):
    pattern.append(['.'] + list(input()) + ['.'])

pattern.append(['.'] * (m+2))

for i in range(1, n+1):
    for j in range(1, m+1):
        chk = 0
        if pattern[i][j] == '#':
            chk = 1
            pattern[i][j] = '.'
            if pattern[i-1][j] == '#':
                answer[(i-1, j)] = ''
            
            if pattern[i+1][j] == '#':
                answer[(i+1, j)] = ''
            
            if pattern[i][j-1] == '#':
                answer[(i, j-1)] = ''
            
            if pattern[i][j+1] == '#':
                answer[(i, j+1)] = ''
            
            while len(answer) != 0:
                tmp = {}
                for k in answer:
                    pattern[k[0]][k[1]] = '.'
                    if pattern[k[0]-1][k[1]] == '#' and (k[0]-1, k[1]) not in tmp:
                        tmp[(k[0]-1, k[1])] = ''
                    
                    if pattern[k[0]+1][k[1]] == '#' and (k[0]+1, k[1]) not in tmp:
                        tmp[(k[0]+1, k[1])] = ''
                    
                    if pattern[k[0]][k[1]-1] == '#' and (k[0], k[1]-1) not in tmp:
                        tmp[(k[0], k[1]-1)] = ''
                    
                    if pattern[k[0]][k[1]+1] == '#' and (k[0], k[1]+1) not in tmp:
                        tmp[(k[0], k[1]+1)] = ''
                
                answer = tmp
        
        if chk != 0:
            total += 1

print(total)