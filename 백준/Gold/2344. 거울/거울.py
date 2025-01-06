n, m = map(int, input().split())
guard = {}
answer = []
check = {}
cnt = 0
way = 1 # 오른쪽부터 1, 시계방향으로 2 3 4

# 벽 체크
for i in range(n):
    word = input().split()
    for j in range(len(word)):
        if word[j] == '1':
            guard[(i+1, j+1)] = ''

# 목적지 체크
for i in range(1, n+1):
    cnt += 1
    check[(i, 0)] = cnt

for i in range(1, m+1):
    cnt += 1
    check[(n+1, i)] = cnt

for i in range(n, 0, -1):
    cnt += 1
    check[(i, m+1)] = cnt

for i in range(m, 0, -1):
    cnt += 1
    check[(0, i)] = cnt

# 왼쪽
for i in range(1, n+1):
    start = [i, 0]
    way = 1
    while True:
        if way == 1:
            start[1] += 1
        
        else:
            start[0] -= 1
        
        if (start[0], start[1]) in guard:
            if way == 1:
                way = 4
            
            else:
                way = 1
        
        if (start[0], start[1]) in check:
            answer.append(check[(start[0], start[1])])
            break

# 아래
for i in range(1, m+1):
    start = [n+1, i]
    way = 4
    while True:
        if way == 4:
            start[0] -= 1
        
        else:
            start[1] += 1
        
        if (start[0], start[1]) in guard:
            if way == 1:
                way = 4

            else:
                way = 1
        
        if (start[0], start[1]) in check:
            answer.append(check[(start[0], start[1])])
            break

# 오른쪽
for i in range(n, 0, -1):
    start = [i, m+1]
    way = 3
    while True:
        if way == 3:
            start[1] -= 1
        
        else:
            start[0] += 1
        
        if (start[0], start[1]) in guard:
            if way == 3:
                way = 2
            
            else:
                way = 3
        
        if (start[0], start[1]) in check:
            answer.append(check[(start[0], start[1])])
            break

# 위
for i in range(m, 0, -1):
    start = [0, i]
    way = 2
    while True:
        if way == 2:
            start[0] += 1
        
        else:
            start[1] -=1
        
        if (start[0], start[1]) in guard:
            if way == 2:
                way = 3
            
            else:
                way = 2
        
        if (start[0], start[1]) in check:
            answer.append(check[start[0], start[1]])
            break

# 결과 출력
print(*answer)