cnt = 0

for _ in range(int(input())):
    pattern = []
    answer = []
    total = []
    tmp = []
    m, n, k = map(int, input().split())
    
    for _ in range(n+2):
        pattern.append([0] * (m + 2))
    
    for _ in range(k):
        j, i = map(int, input().split())
        pattern[i+1][j+1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if pattern[i][j] == 1:
                cnt = 0
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
                        if pattern[answer[a][0] - 1][answer[a][1]] == 1 and [answer[a][0]-1, answer[a][1]] not in tmp:
                            tmp.append([answer[a][0]-1, answer[a][1]])
                        
                        if pattern[answer[a][0] + 1][answer[a][1]] == 1 and [answer[a][0]+1, answer[a][1]] not in tmp:
                            tmp.append([answer[a][0]+1, answer[a][1]])
                        
                        if pattern[answer[a][0]][answer[a][1] - 1] == 1 and [answer[a][0], answer[a][1] - 1] not in tmp:
                            tmp.append([answer[a][0], answer[a][1] - 1])
                        
                        if pattern[answer[a][0]][answer[a][1] + 1] == 1 and [answer[a][0], answer[a][1] + 1] not in tmp:
                            tmp.append([answer[a][0], answer[a][1] + 1])
                        
                    answer = tmp
                
                total.append(cnt)
    
    print(len(total))