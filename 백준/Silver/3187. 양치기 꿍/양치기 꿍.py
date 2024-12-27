n, m = map(int, input().split())

pattern = []
total_sw = [0, 0] # 양, 늑대 총합
tmp_sw = [0, 0] # 양, 늑대 임시시
kv = 'kv.'
answer = {}
tmp = {}
pattern.append(['#'] * (m+2))
for _ in range(n):
    pattern.append(['#'] + list(input()) + ['#'])

pattern.append(['#'] * (m+2))

for i in range(1, n+1):
    for j in range(1, m+1):
        if pattern[i][j] in kv: # k - 양, v - 늑대
            answer = {}
            tmp = {}
            tmp_sw = [0, 0]
            if pattern[i][j] == 'k':
                tmp_sw[0] += 1
            
            elif pattern[i][j] == 'v':
                tmp_sw[1] += 1
            
            pattern[i][j] = '#'
            if pattern[i-1][j] in kv:
                answer[(i-1, j)] = ''
            
            if pattern[i+1][j] in kv:
                answer[(i+1, j)] = ''
            
            if pattern[i][j-1] in kv:
                answer[(i, j-1)] = ''
            
            if pattern[i][j+1] in kv:
                answer[(i, j+1)] = ''
            
            while len(answer) != 0:
                tmp = {}
                for k in answer:
                    if pattern[k[0]][k[1]] == 'k':
                        tmp_sw[0] += 1
                    
                    elif pattern[k[0]][k[1]] == 'v':
                        tmp_sw[1] += 1
                    
                    pattern[k[0]][k[1]] = '#'

                    if pattern[k[0]-1][k[1]] in kv and (k[0]-1, k[1]) not in tmp:
                        tmp[(k[0]-1, k[1])] = ''
                    
                    if pattern[k[0]+1][k[1]] in kv and (k[0]+1, k[1]) not in tmp:
                        tmp[(k[0]+1, k[1])] = ''
                    
                    if pattern[k[0]][k[1]-1] in kv and (k[0], k[1]-1) not in tmp:
                        tmp[(k[0], k[1]-1)] = ''
                    
                    if pattern[k[0]][k[1]+1] in kv and (k[0], k[1]+1) not in tmp:
                        tmp[(k[0], k[1]+1)] = ''
                
                answer = tmp

            if tmp_sw[0] >= 1 or tmp_sw[1] >= 1:
                if tmp_sw[0] > tmp_sw[1]:
                    total_sw[0] += tmp_sw[0]
                
                else:
                    total_sw[1] += tmp_sw[1]
                
print(*total_sw)