n, m = map(int, input().split())
pattern = []
answer = []
tmp = []
score = [0, 0] # W, B
word = 'WB'
cnt = 0

pattern.append(['.'] * (n+2))
for _ in range(m):
    pattern.append(['.'] + list(input()) + [','])

pattern.append(['.'] * (n+2))

for i in range(1, m+1):
    for j in range(1, n+1):
        for k in range(len(word)):
            if pattern[i][j] == word[k]:
                cnt = 0
                cnt += 1
                pattern[i][j] = '.'
                if pattern[i-1][j] == word[k]:
                    answer.append([i-1, j])

                if pattern[i+1][j] == word[k]:
                    answer.append([i+1, j])
                
                if pattern[i][j-1] == word[k]:
                    answer.append([i, j-1])
                
                if pattern[i][j+1] == word[k]:
                    answer.append([i, j+1])
                
                while len(answer) != 0:
                    tmp = []
                    for a in range(len(answer)):
                        cnt += 1
                        pattern[answer[a][0]][answer[a][1]] = '.'
                        if pattern[answer[a][0] - 1][answer[a][1]] == word[k] and [answer[a][0]-1, answer[a][1]] not in tmp:
                            tmp.append([answer[a][0] - 1, answer[a][1]])
                        
                        if pattern[answer[a][0] + 1][answer[a][1]] == word[k] and [answer[a][0]+1, answer[a][1]] not in tmp:
                            tmp.append([answer[a][0] + 1, answer[a][1]])
                        
                        if pattern[answer[a][0]][answer[a][1] - 1] == word[k] and [answer[a][0], answer[a][1]-1] not in tmp:
                            tmp.append([answer[a][0], answer[a][1] - 1])
                        
                        if pattern[answer[a][0]][answer[a][1] + 1] == word[k] and [answer[a][0], answer[a][1]+1] not in tmp:
                            tmp.append([answer[a][0], answer[a][1] + 1])
                    
                    answer = tmp

                score[k] += cnt ** 2

print(*score)