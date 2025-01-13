n = int(input())
chk = 0
answer = {(1, 1)}
finish = (n, n)
tmp = {}

pattern = []

pattern.append(['x'] * (n + 2))
for _ in range(n):
    pattern.append(['x'] + list(input()) + ['x'])

pattern.append(['x'] * (n + 2))

while len(answer) != 0 and chk != 1:
    tmp = {}
    for i in answer:
        if i == finish:
            chk = 1
            break
        
        if pattern[i[0]+1][i[1]] == '.' and (i[0]+1, i[1]) not in tmp:
            tmp[(i[0]+1, i[1])] = ''
        
        if pattern[i[0]][i[1]+1] == '.' and (i[0], i[1]+1) not in tmp:
            tmp[(i[0], i[1]+1)] = ''

    answer = tmp

if chk == 1:
    print("Yes")

else:
    print("No")