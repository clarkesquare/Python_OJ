n = int(input())

answer = {n: ''}
tmp = {}
chk = 0
cnt = 0

while chk == 0:
    tmp = {}
    for k in answer:
        if k == 1:
            chk = 1
            break

        if k % 3 == 0 and (k // 3) not in tmp:
            tmp[k//3] = ''
        
        if k % 2 == 0 and (k // 2) not in tmp:
            tmp[k//2] = ''
        
        if n - 1 not in tmp:
            tmp[k-1] = ''

    if chk == 1:
        break
    
    cnt += 1
    answer = tmp

print(cnt)