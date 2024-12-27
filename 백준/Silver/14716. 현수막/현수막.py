n, m = map(int, input().split())

pattern = []

pattern.append([0] * (m+2))
for _ in range(n):
    pattern.append([0] + list(map(int, input().split())) + [0])

pattern.append([0] * (m+2))
answer = {}
tmp = {}
total = []

for i in range(1, n+1):
    for j in range(1, m+1):
        chk = 0
        if pattern[i][j] == 1:
            chk = 1
            pattern[i][j] = 0
            answer = {}
            for r in range(i-1, i+2, 1):
                for c in range(j-1, j+2, 1):
                    if pattern[r][c] == 1:
                        answer[(r, c)] = ''
            
            while len(answer) != 0:
                tmp = {}
                for k in answer:
                    pattern[k[0]][k[1]] = 0
                    for r in range(k[0]-1, k[0]+2, 1):
                        for c in range(k[1]-1, k[1]+2, 1):
                            if pattern[r][c] == 1 and (r, c) not in tmp:
                                tmp[(r, c)] = ''
                
                answer = tmp
            
            if chk != 0:
                total.append(chk)

print(len(total))