n, m, k = map(int, input().split())
pattern = []
answer = []
tmp = []
total = [0]
cnt = 0

for _ in range(n+2):
    pattern.append(list('.' * (m + 2)))

for _ in range(k):
    r, c = map(int, input().split())
    pattern[r][c] = '#'

for i in range(1, n+1):
    for j in range(1, m+1):
        if pattern[i][j] == '#':
            cnt = 0
            cnt += 1
            pattern[i][j] = '.'
            if pattern[i-1][j] == '#':
                answer.append([i-1, j])
            
            if pattern[i+1][j] == '#':
                answer.append([i+1, j])
            
            if pattern[i][j-1] == '#':
                answer.append([i, j-1])
            
            if pattern[i][j+1] == '#':
                answer.append([i, j+1])
            
            while len(answer) != 0:
                tmp = []
                for a in range(len(answer)):
                    cnt += 1
                    pattern[answer[a][0]][answer[a][1]] = '.'
                    if pattern[answer[a][0] - 1][answer[a][1]] == '#' and [answer[a][0] - 1, answer[a][1]] not in tmp:
                        tmp.append([answer[a][0] - 1, answer[a][1]])
                    
                    if pattern[answer[a][0] + 1][answer[a][1]] == '#' and [answer[a][0] + 1, answer[a][1]] not in tmp:
                        tmp.append([answer[a][0] + 1, answer[a][1]])
                    
                    if pattern[answer[a][0]][answer[a][1] - 1] == '#' and [answer[a][0], answer[a][1] - 1] not in tmp:
                        tmp.append([answer[a][0], answer[a][1] - 1])

                    if pattern[answer[a][0]][answer[a][1] + 1] == '#' and [answer[a][0], answer[a][1] + 1] not in tmp:
                        tmp.append([answer[a][0], answer[a][1] + 1])
                
                answer = tmp
            
            total.append(cnt)

print(max(total))