n, m = map(int, input().split())

pattern = []
x = 0
y = 0
cnt = 0
answer = {}
tmp = {}

pattern.append(['X'] * (m+2))
for i in range(n):
    word = list(input())
    if 'I' in word:
        y = word.index('I') + 1
        x = i + 1
    pattern.append(['X'] + word + ['X'])

pattern.append(['X'] * (m+2))

pattern[x][y] = 'X'
if pattern[x-1][y] != 'X':
    answer[(x-1), y] = ''

if pattern[x+1][y] != 'X':
    answer[(x+1), y] = ''

if pattern[x][y-1] != 'X':
    answer[(x, y-1)] = ''

if pattern[x][y+1] != 'X':
    answer[(x, y+1)] = ''

while len(answer) != 0:
    tmp = {}
    for k in answer:
        if pattern[k[0]][k[1]] == 'P':
            cnt += 1

        pattern[k[0]][k[1]] = 'X'
        if pattern[k[0]-1][k[1]] != 'X' and (k[0]-1, k[1]) not in tmp:
            tmp[(k[0]-1, k[1])] = ''
        
        if pattern[k[0]+1][k[1]] != 'X' and (k[0]+1, k[1]) not in tmp:
            tmp[(k[0]+1, k[1])] = ''
        
        if pattern[k[0]][k[1]-1] != 'X' and (k[0], k[1]-1) not in tmp:
            tmp[(k[0], k[1]-1)] = ''
        
        if pattern[k[0]][k[1]+1] != 'X' and (k[0], k[1]+1) not in tmp:
            tmp[(k[0], k[1]+1)] = ''
        
    answer = tmp

if cnt >= 1:
    print(cnt)

else:
    print('TT')