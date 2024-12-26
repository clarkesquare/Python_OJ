for _ in range(int(input())):
    n, m = map(int, input().split())
    pattern = []
    total = []
    answer = []
    tmp = []

    pattern.append(['.'] * (m + 2))
    for _ in range(n):
        pattern.append(['.'] + list(input()) + ['.'])
    
    pattern.append(['.'] * (m + 2))
    
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
                        pattern[answer[a][0]][answer[a][1]] = '.'
                        cnt += 1
                        if pattern[answer[a][0] -1][answer[a][1]] == '#' and [answer[a][0]-1, answer[a][1]] not in tmp:
                            tmp.append([answer[a][0]-1, answer[a][1]])
                        
                        if pattern[answer[a][0] +1][answer[a][1]] == '#' and [answer[a][0] + 1, answer[a][1]] not in tmp:
                            tmp.append([answer[a][0] + 1, answer[a][1]])
                        
                        if pattern[answer[a][0]][answer[a][1] -1] == '#' and [answer[a][0], answer[a][1] - 1] not in tmp:
                            tmp.append([answer[a][0], answer[a][1] - 1])
                        
                        if pattern[answer[a][0]][answer[a][1] +1] == '#' and [answer[a][0], answer[a][1] + 1] not in tmp:
                            tmp.append([answer[a][0], answer[a][1] + 1])
                    
                    answer = tmp
            
                total.append(cnt)

    print(len(total))