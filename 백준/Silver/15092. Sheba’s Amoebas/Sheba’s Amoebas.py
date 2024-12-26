m, n = map(int, input().split())

pattern = []
answer = {}
tmp = {}
total = []
chk = 0

pattern.append(['.'] * (n+2))
for _ in range(m):
    pattern.append(['.'] + list(input()) + ['.'])

pattern.append(['.'] * (n+2))

for i in range(1, m+1):
    for j in range(1, n+1):
        chk = 0
        if pattern[i][j] == '#':
            chk = 1
            pattern[i][j] = '.'
            for r in range(i-1, i+2, 1):
                for c in range(j-1, j+2, 1):
                    if pattern[r][c] == '#':
                        answer[(r, c)] = ''
            
            while len(answer) != 0:
                tmp = {}
                for k, v in answer.items():
                    pattern[k[0]][k[1]] = '.'
                    for r in range(k[0]-1, k[0]+2, 1):
                        for c in range(k[1]-1, k[1]+2, 1):
                            if pattern[r][c] == '#':
                                tmp[(r, c)] = ''
                
                answer = tmp

        if chk != 0:
            total.append(chk)

print(len(total))