n, m = map(int, input().split())
pattern = []
tmp = ""
answer = []

for _ in range(n):
    pattern.append(input())

# 가로 검사
for i in range(n):
    tmp = ""
    for j in range(m):
        if pattern[i][j] != "#":
            tmp += pattern[i][j]
        
        else:
            if len(tmp) >= 2:
                answer.append(tmp)

            tmp = ""
        
    if len(tmp) >= 2:
        answer.append(tmp)

# 세로 검사
for k in range(m):
    tmp = ""
    for l in range(n):
        if pattern[l][k] != "#":
            tmp += pattern[l][k]
        
        else:
            if len(tmp) >= 2:
                answer.append(tmp)

            tmp = ""
    
    if len(tmp) >= 2:
        answer.append(tmp)

# 정답 출력
answer.sort()
print(answer[0])