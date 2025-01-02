n, m = map(int, input().split())
pattern = [[0] * (m+2)]
cnt = 0
answer = {}
total = {}
for i in range(n):
    word = list(map(int, input().split()))
    if 2 in word:
        for j in range(m):
            if word[j] == 2:
                answer[(i+1, j+1)] = ''
                break

    pattern.append([0] + word + [0])

pattern.append([0] * (m+2))

while len(answer) != 0:
    tmp = {}
    for i in answer:
        pattern[i[0]][i[1]] = cnt
        total[(i[0], i[1])] = ''
        if pattern[i[0]-1][i[1]] == 1 and (i[0]-1, i[1]) not in tmp and (i[0]-1, i[1]) not in total:
            tmp[(i[0]-1, i[1])] = ''
        
        if pattern[i[0]+1][i[1]] == 1 and (i[0]+1, i[1]) not in tmp and (i[0]+1, i[1]) not in total:
            tmp[(i[0]+1, i[1])] = ''
        
        if pattern[i[0]][i[1]-1] == 1 and (i[0], i[1]-1) not in tmp and (i[0], i[1]-1) not in total:
            tmp[(i[0], i[1]-1)] = ''
        
        if pattern[i[0]][i[1]+1] == 1 and (i[0], i[1]+1) not in tmp and (i[0], i[1]+1) not in total:
            tmp[(i[0], i[1]+1)] = ''

    answer = tmp
    cnt += 1

for i in range(1, n+1):
    word = []
    for j in range(1, m+1):
        if pattern[i][j] == 1 and (i, j) not in total:
            word.append(-1)
        
        else:
            word.append(pattern[i][j])
    
    print(*word)