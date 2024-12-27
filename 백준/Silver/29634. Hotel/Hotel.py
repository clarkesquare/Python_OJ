n, m = map(int, input().split())
pattern = []

pattern.append(['*'] * (m+2))
for _ in range(n):
    pattern.append(['*'] + list(input()) + ['*'])

pattern.append(['*'] * (m+2))
cnt = 0
maximum = 0
answer = {}
tmp = {}

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt = 0
        if pattern[i][j] == '.':
            pattern[i][j] = '*'
            cnt += 1
            if pattern[i-1][j] == '.':
                answer[(i-1, j)] = ''
            
            if pattern[i+1][j] == '.':
                answer[(i+1, j)] = ''
            
            if pattern[i][j-1] == '.':
                answer[(i, j-1)] = ''
            
            if pattern[i][j+1] == '.':
                answer[(i, j+1)] = ''
            
            while len(answer) != 0:
                tmp = {}
                for k in answer:
                    cnt += 1
                    pattern[k[0]][k[1]] = '*'
                    if pattern[k[0]-1][k[1]] == '.' and (k[0]-1, k[1]) not in tmp:
                        tmp[(k[0]-1, k[1])] = ''
                    
                    if pattern[k[0]+1][k[1]] == '.' and (k[0]+1, k[1]) not in tmp:
                        tmp[(k[0]+1, k[1])] = ''
                    
                    if pattern[k[0]][k[1]-1] == '.' and (k[0], k[1]-1) not in tmp:
                        tmp[(k[0], k[1]-1)] = ''
                    
                    if pattern[k[0]][k[1]+1] == '.' and (k[0], k[1]+1) not in tmp:
                        tmp[(k[0], k[1]+1)] = ''
                
                answer = tmp
        
        if maximum <= cnt:
            maximum = cnt

if maximum == 0:
    print('-1')

else:
    print(maximum)