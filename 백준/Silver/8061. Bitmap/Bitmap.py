n, m = map(int, input().split())
pattern = []

pattern.append([-1] * (m+2))

answer = {}
tmp = {}
cnt = 0
for i in range(1, n+1):
    word = list(map(int, input()))
    if 1 in word:
        for j in range(m):
            if word[j] == 1:
                answer[(i, j+1)] = ''

    pattern.append([-1] + word + [-1])

pattern.append([-1] * (m+2))

while len(answer) != 0:
    tmp = {}
    for k in answer:
        if pattern[k[0]][k[1]] == 0 or cnt == 0:
            pattern[k[0]][k[1]] = str(cnt)

        if pattern[k[0]-1][k[1]] == 0 and (k[0]-1, k[1]) not in tmp:
            tmp[(k[0]-1, k[1])] = ''
        
        if pattern[k[0]+1][k[1]] == 0 and (k[0]+1, k[1]) not in tmp:
            tmp[(k[0]+1, k[1])] = ''
        
        if pattern[k[0]][k[1]-1] == 0 and (k[0], k[1]-1) not in tmp:
            tmp[(k[0], k[1]-1)] = ''
        
        if pattern[k[0]][k[1]+1] == 0 and (k[0], k[1]+1) not in tmp:
            tmp[(k[0], k[1]+1)] = ''
    
    answer = tmp
    cnt += 1

for i in pattern[1:-1]:
    print(*i[1:-1])