import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pattern = []
pattern.append(['?'] * (m + 2))
answer = {}
tmp = {}

for _ in range(n):
    pattern.append(['?'] + list(map(int, input().strip('\n'))) + ['?'])

pattern.append(['?'] * (m + 2))

x, y, num = map(int, input().strip('\n').split())
x += 1
y += 1
num = str(num)
cn = pattern[x][y]

pattern[x][y] = num
if pattern[x-1][y] == cn:
    answer[(x-1, y)] = ''

if pattern[x+1][y] == cn:
    answer[(x+1, y)] = ''

if pattern[x][y-1] == cn:
    answer[(x, y-1)] = ''

if pattern[x][y+1] == cn:
    answer[(x, y+1)] = ''

while len(answer) != 0:
    tmp = {}
    for k, v in answer.items():
        pattern[k[0]][k[1]] = num
        if pattern[k[0]-1][k[1]] == cn and (k[0]-1, k[1]) not in tmp:
            tmp[(k[0]-1, k[1])] = ''
        
        if pattern[k[0]+1][k[1]] == cn and (k[0]+1, k[1]) not in tmp:
            tmp[(k[0]+1, k[1])] = ''
        
        if pattern[k[0]][k[1]-1] == cn and (k[0], k[1]-1) not in tmp:
            tmp[(k[0], k[1]-1)] = ''
        
        if pattern[k[0]][k[1]+1] == cn and (k[0], k[1]+1) not in tmp:
            tmp[(k[0], k[1]+1)] = ''
    
    answer = tmp

for i in pattern[1:-1]:
    print(*i[1:-1], sep='')