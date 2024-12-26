n, m = map(int, input().split())
pattern = []

pattern.append(['0'] * (m + 2))
for _ in range(n):
    pattern.append(['0'] + list(input()) + ['0'])

pattern.append(['0'] * (m + 2))
answer = {}
tmp = {}
total = []
cnt = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt = 0
        if pattern[i][j] == '1':
            cnt += 1
            pattern[i][j] = '0'
            if pattern[i-1][j] == '1':
                answer[(i-1, j)] = ''
            
            if pattern[i+1][j] == '1':
                answer[(i+1, j)] = ''
            
            if pattern[i][j-1] == '1':
                answer[(i, j-1)] = ''
            
            if pattern[i][j+1] == '1':
                answer[(i, j+1)] = ''
            
            while len(answer) != 0:
                tmp = {}
                for a, v in answer.items():
                    cnt += 1
                    pattern[a[0]][a[1]] = '0'
                    if pattern[a[0] -1][a[1]] == '1' and (a[0]-1, a[1]) not in tmp:
                        tmp[(a[0]-1, a[1])] = ''
                    
                    if pattern[a[0] +1][a[1]] == '1' and (a[0]+1, a[1]) not in tmp:
                        tmp[(a[0]+1, a[1])] = ''
                    
                    if pattern[a[0]][a[1] -1] == '1' and (a[0], a[1]-1) not in tmp:
                        tmp[(a[0], a[1]-1)] = ''
                    
                    if pattern[a[0]][a[1] +1] == '1' and (a[0], a[1]+1) not in tmp:
                        tmp[(a[0], a[1]+1)] = ''
                
                answer = tmp
        
        if cnt != 0:
            total.append(cnt)

total.sort()
print(len(total))
print(*total)