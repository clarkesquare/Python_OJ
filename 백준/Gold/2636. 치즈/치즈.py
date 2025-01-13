import time

n, m = map(int, input().split())

total = {}
cheese = {}
answer = {}
tmp = {}
cnt = 0
pattern = []
cheese_cnt = 0

pattern.append([2] * (m+2))

for _ in range(n):
    pattern.append([2] + list(map(int, input().split())) + [2])

pattern.append([2] * (m+2))

for i in range(n):
    answer[(i+1, 1)] = ''
    answer[(i+1, m)] = ''
    total[(i+1, 1)] = ''
    total[(i+1, m)] = ''

for i in range(m):
    answer[(1, i+1)] = ''
    answer[(n, i+1)] = ''
    total[(1, i+1)] = ''
    total[(n, i+1)] = ''

while len(total) != (n * m):
    while len(answer) != 0:
        tmp = {}
        for i in answer:
            total[i] = ''
            if pattern[i[0]-1][i[1]] == 0 and (i[0]-1, i[1]) not in tmp and (i[0]-1, i[1]) not in total:
                tmp[(i[0]-1, i[1])] = ''
            
            if pattern[i[0]+1][i[1]] == 0 and (i[0]+1, i[1]) not in tmp and (i[0]+1, i[1]) not in total:
                tmp[(i[0]+1, i[1])] = ''
            
            if pattern[i[0]][i[1]-1] == 0 and (i[0], i[1]-1) not in tmp and (i[0], i[1]-1) not in total:
                tmp[(i[0], i[1]-1)] = ''
            
            if pattern[i[0]][i[1]+1] == 0 and (i[0], i[1]+1) not in tmp and (i[0], i[1]+1) not in total:
                tmp[(i[0], i[1]+1)] = ''
            
            if pattern[i[0]-1][i[1]] == 1 and (i[0]-1, i[1]) not in cheese:
                cheese[(i[0]-1, i[1])] = ''
            
            if pattern[i[0]+1][i[1]] == 1 and (i[0]+1, i[1]) not in cheese:
                cheese[(i[0]+1, i[1])] = ''
            
            if pattern[i[0]][i[1]-1] == 1 and (i[0], i[1]-1) not in cheese:
                cheese[(i[0], i[1]-1)] = ''
            
            if pattern[i[0]][i[1]+1] == 1 and (i[0], i[1]+1) not in cheese:
                cheese[(i[0], i[1]+1)] = ''
        
        answer = tmp
    
    if len(total) == (n * m):
        break

    if len(cheese) != 0:
        cnt += 1
        for j in cheese: # 치즈 녹은 자리 0으로 만들고 answer에 cheese를 넣어 계속 검사 진행
            pattern[j[0]][j[1]] = 0
            total[(j[0], j[1])] = ''
        
        cheese_cnt = len(cheese)
    
    answer = cheese
    cheese = {}

print(cnt)
print(cheese_cnt)