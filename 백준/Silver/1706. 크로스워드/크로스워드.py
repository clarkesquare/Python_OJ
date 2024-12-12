n, m = map(int, input().split())

words = []
pattern = []
tmp = ""

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
                words.append(tmp)
            
            tmp = ""
    
    if len(tmp) >= 2:
        words.append(tmp)

# 세로 검사
for i in range(m):
    tmp = ""
    for j in range(n):
        if pattern[j][i] != "#":
            tmp += pattern[j][i]
        
        else:
            if len(tmp) >= 2:
                words.append(tmp)

            tmp = ""
    
    if len(tmp) >= 2:
        words.append(tmp)

# 정답 출력
print(sorted(words)[0])