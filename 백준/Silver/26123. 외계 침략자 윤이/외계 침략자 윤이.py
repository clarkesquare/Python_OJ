n, d = map(int, input().split())

chk = {}
answer = 0
max = 0

for i in list(map(int, input().split())):
    if i not in chk:
        chk[i] = 1
    
    else:
        chk[i] += 1
    
    if max < i:
        max = i

for _ in range(d):
    if max - 1 not in chk:
        chk[max-1] = chk[max]
    
    else:
        chk[max-1] += chk[max]
    
    answer += chk[max]
    del chk[max]
    max -= 1

    if max == 0:
        break

print(answer)