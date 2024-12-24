n = int(input())
pattern = []
for _ in range(n * 2): 
    pattern.append(list('0') * (2 * n -1))

pattern[n-1][n-1] = "." # 시작지점
coordinate = [n-1, n-1] # 홍준이 위치
map_limit = [-1, -1, -1, -1] # 맵 한계지점, .을 활용해 지정정
way = 2 # 2는 남쪽, 시계 방향으로 3, 4, 1

position = input()
for i in range(n):
    if position[i] == "F":
        if way == 2:
            coordinate[0] += 1
        
        elif way == 3:
            coordinate[1] -= 1
        
        elif way == 4:
            coordinate[0] -= 1
        
        else:
            coordinate[1] += 1
        
        pattern[coordinate[0]][coordinate[1]] = "."
    
    elif position[i] == "L":
        way -= 1
        if way == 0:
            way = 4
        
    else:
        way += 1
        if way == 5:
            way = 1

for i in range(len(pattern)): # 위부터 검사
    if '.' in pattern[i]:
        map_limit[0] = i
        break

for i in range(len(pattern)-1, -1, -1): # 아래부터 검사
    if '.' in pattern[i]:
        map_limit[1] = i
        break

for j in range(len(pattern[0])): # 왼쪽부터 검사
    for i in range(len(pattern)):
        if pattern[i][j] == ".":
            map_limit[2] = j
            break
    
    if map_limit[2] != -1:
        break

for j in range(len(pattern[0])-1, -1, -1): # 오른쪽부터 검사
    for i in range(len(pattern)-1):
        if pattern[i][j] == ".":
            map_limit[3] = j
            break
    
    if map_limit[3] != -1:
        break

for i in range(map_limit[0], map_limit[1]+1): # 최종 간결한 맵 출력
    tmp = ''
    for j in range(map_limit[2], map_limit[3]+1):
        if pattern[i][j] == "0":
            tmp += '#'
        
        else:
            tmp += '.'
    
    print(tmp)