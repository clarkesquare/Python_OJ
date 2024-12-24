n, m = map(int, input().split())

answer = [0, 0, 0, 0]

# 입력
pattern = [list('.' * (m + 2))]
for _ in range(n):
    pattern.append(['.'] + list(input()) + ['.'])

pattern.append(list('.' * (m + 2)))

# 바다 체크

for i in range(1, n+1):
    for j in range(1, m+1):
        if pattern[i][j] == "X":
            cnt = 0
            if pattern[i-1][j] == ".":
                cnt += 1
            
            if pattern[i+1][j] == ".":
                cnt += 1
            
            if pattern[i][j-1] == ".":
                cnt += 1
            
            if pattern[i][j+1] == ".":
                cnt += 1
            
            if cnt >= 3:
                pattern[i][j] = "?"


# 위쪽부터 범위
for i in range(n+2):
    if 'X' in pattern[i]:
        answer[0] = i
        break

# 아래부터 범위
for i in range(n+1, -1, -1):
    if 'X' in pattern[i]:
        answer[1] = i
        break

# 왼쪽부터 범위
for j in range(m+2):
    for i in range(n+2):
        if pattern[i][j] == "X":
            answer[2] = j
            break
    
    if answer[2] != 0:
        break

# 오른쪽부터 범위
for j in range(m+1, -1, -1):
    for i in range(n+2):
        if pattern[i][j] == "X":
            answer[3] = j
            break
    
    if answer[3] != 0:
        break

# 최종 결과
for i in range(answer[0], answer[1]+1):
    tmp = ''
    for j in range(answer[2], answer[3]+1):
        if pattern[i][j] == 'X':
            tmp += 'X'
        
        else:
            tmp += '.'
    
    print(tmp)