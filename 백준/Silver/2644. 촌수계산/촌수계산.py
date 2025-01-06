n = int(input())
a, b = map(int, input().split())
total = {a: ''}
pattern = {}
check = {}
tmp = {}
chk = 0
cnt = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x not in pattern:
        pattern[x] = [y]
    
    else:
        pattern[x].append(y)
    
    if y not in pattern:
        pattern[y] = [x]
    
    else:
        pattern[y].append(x)

check = {a: ''}
while len(check) != 0 and chk == 0:
    tmp = {}
    for i in check:
        if i == b:
            chk = 1
            break
        
        for j in pattern[i]:
            if j not in total and j not in tmp:
                total[j] = ''
                tmp[j] = ''

    check = tmp
    if chk == 1:
        break

    cnt += 1

if chk == 1:
    print(cnt)

else:
    print(-1)