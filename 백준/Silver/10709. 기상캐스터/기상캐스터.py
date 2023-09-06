h, w = map(int, input().split())
map, answer = [], []

for _ in range(h):
    map.append(list(input()))

for i in range(h):
    temp = []
    cloud = -1
    
    for j in range(w):
        if map[i][j] == '.' and cloud != -1:
            cloud += 1
        elif map[i][j] == 'c':
            cloud = 0

        temp.append(cloud)
    answer.append(temp)
                
for k in answer:
    print(*k)