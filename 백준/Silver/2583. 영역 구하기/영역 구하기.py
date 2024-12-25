m, n, k = map(int, input().split())
pattern = []
answer = []
tmp = []
total = []
cnt = 0
check = 0

# 지도 생성 및 셋팅
pattern.append([1] * (n+2))
for _ in range(m):
    pattern.append([1] + [0] * (n) + [1])

pattern.append([1] * (n+2))

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            if pattern[i+1][j+1] != 1:
                pattern[i+1][j+1] = 1

# 답 검색
for i in range(1, m+1):
    for j in range(1, n+1):
        cnt = 0
        if pattern[i][j] == 0:
            pattern[i][j] = 1
            check = 0
            cnt += 1
            answer = []
            if pattern[i-1][j] == 0:
                answer.append([i-1, j])
            
            if pattern[i+1][j] == 0:
                answer.append([i+1, j])

            if pattern[i][j-1] == 0:
                answer.append([i, j-1])

            if pattern[i][j+1] == 0:
                answer.append([i, j+1])

            while len(answer) != 0:
                tmp = []
                for i in range(len(answer)):
                    cnt += 1
                    pattern[answer[i][0]][answer[i][1]] = 1
                    if pattern[answer[i][0] - 1][answer[i][1]] == 0 and [answer[i][0] - 1, answer[i][1]] not in tmp:
                        tmp.append([answer[i][0] - 1, answer[i][1]])
                    
                    if pattern[answer[i][0] + 1][answer[i][1]] == 0 and [answer[i][0] + 1, answer[i][1]] not in tmp:
                        tmp.append([answer[i][0] + 1, answer[i][1]])
                    
                    if pattern[answer[i][0]][answer[i][1] - 1] == 0 and [answer[i][0], answer[i][1] - 1] not in tmp:
                        tmp.append([answer[i][0], answer[i][1] - 1])
                    
                    if pattern[answer[i][0]][answer[i][1] + 1] == 0 and [answer[i][0], answer[i][1] + 1] not in tmp:
                        tmp.append([answer[i][0], answer[i][1] + 1])
                
                answer = tmp
    
        if cnt != 0:
            total.append(cnt)

print(len(total))
print(*sorted(total))