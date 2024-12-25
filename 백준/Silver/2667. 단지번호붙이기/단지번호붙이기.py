n = int(input())
pattern = []
cnt = 0
answer = []
tmp = []
total = []

pattern.append([0] * (n+2))
for _ in range(n):
    pattern.append([0] + list(map(int, input())) + [0])

pattern.append([0] * (n+2))

for i in range(1, n+1):
    for j in range(1, n+1):
        cnt = 0
        if pattern[i][j] == 1:
            cnt += 1
            pattern[i][j] = 0
            if pattern[i-1][j] == 1:
                answer.append([i-1, j])
            
            if pattern[i+1][j] == 1:
                answer.append([i+1, j])
            
            if pattern[i][j-1] == 1:
                answer.append([i, j-1])
            
            if pattern[i][j+1] == 1:
                answer.append([i, j+1])
            
            while len(answer) != 0:
                tmp = []
                for a in range(len(answer)):
                    pattern[answer[a][0]][answer[a][1]] = 0
                    cnt += 1
                    if pattern[answer[a][0] -1][answer[a][1]] == 1 and [answer[a][0]-1, answer[a][1]] not in tmp:
                        tmp.append([answer[a][0]-1, answer[a][1]])
                    
                    if pattern[answer[a][0] +1][answer[a][1]] == 1 and [answer[a][0]+1, answer[a][1]] not in tmp:
                        tmp.append([answer[a][0]+1, answer[a][1]])
                    
                    if pattern[answer[a][0]][answer[a][1] - 1] == 1 and [answer[a][0], answer[a][1] - 1] not in tmp:
                        tmp.append([answer[a][0], answer[a][1] - 1])
                    
                    if pattern[answer[a][0]][answer[a][1] + 1] == 1 and [answer[a][0], answer[a][1] + 1] not in tmp:
                        tmp.append([answer[a][0], answer[a][1] + 1])
                
                answer = tmp
            
            if cnt >= 1:
                total.append(cnt)

print(len(total))
print(*sorted(total), sep='\n')