import time

w, h = map(int, input().split())

pattern = []
answer = {}
tmp = {}
cnt = 0
maximum = 0

pattern.append(['*'] * (w+2))
for _ in range(h):
    pattern.append(['*'] + list(input()) + ['*'])

pattern.append(['*'] * (w+2))

for i in range(1, h+1):
    for j in range(1, w+1):
        if pattern[i][j] == '.':
            cnt = 0
            cnt += 1
            pattern[i][j] = '*'
            for r in range(i-1, i+2, 1):
                for c in range(j-1, j+2, 1):
                    if pattern[r][c] == '.':
                        answer[(r, c)] = ''
            
            while len(answer) != 0:
                tmp = {}
                for k, v in answer.items():
                    if pattern[k[0]][k[1]] == '.':
                        pattern[k[0]][k[1]] = '*'
                        cnt += 1
                    for r in range(k[0]-1, k[0]+2, 1):
                        for c in range(k[1]-1, k[1]+2, 1):
                            if pattern[r][c] == '.' and (r, c) not in tmp:
                                tmp[(r, c)] = ''
                
                answer = tmp
            
            if maximum < cnt:
                maximum = cnt

print(maximum)