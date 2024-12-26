n = int(input())
pattern = []
answer = {}
tmp = []
chk = 0
total = []

pattern.append(['.'] * (n+2))
for _ in range(n):
    pattern.append(['.'] + list(input()) + ['.'])

pattern.append(['.'] * (n+2))

for i in range(1, n+1):
    for j in range(1, n+1):
        chk = 0
        if pattern[i][j] == '*':
            chk = 1
            pattern[i][j] = '.'
            if pattern[i-1][j] == '*':
                answer[i-1, j] = ''
            
            if pattern[i+1][j] == '*':
                answer[i+1, j] = ''

            if pattern[i][j-1] == '*':
                answer[i, j-1] = ''
            
            if pattern[i][j+1] == '*':
                answer[i, j+1] = ''

            while len(answer) != 0:
                tmp = {}
                for a, v in answer.items():
                    pattern[a[0]][a[1]] = '.'
                    if pattern[a[0] -1][a[1]] == '*' and (a[0]-1, a[1]) not in tmp:
                        tmp[(a[0]-1, a[1])] = ''
                    
                    if pattern[a[0] +1][a[1]] == '*' and (a[0]+1, a[1]) not in tmp:
                        tmp[(a[0]+1, a[1])] = ''
                    
                    if pattern[a[0]][a[1]-1] == '*' and (a[0], a[1] -1) not in tmp:
                        tmp[(a[0], a[1] -1)] = ''
                    
                    if pattern[a[0]][a[1]+1] == '*' and (a[0], a[1] +1) not in tmp:
                        tmp[(a[0], a[1]+1)] = ''
                
                answer = tmp
        
        if chk == 1:
            total.append(chk)

print(len(total))