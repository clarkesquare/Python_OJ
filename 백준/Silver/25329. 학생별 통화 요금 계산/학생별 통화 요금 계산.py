chk = {}
answer = []

for _ in range(int(input())):
    call, name = input().split()
    if name not in chk:
        chk[name] = int(call[:2]) * 60 + int(call[3:])
    
    else:
        chk[name] += int(call[:2]) * 60 + int(call[3:])

for k, v in chk.items():
    tmp = 0
    v -= 100
    tmp += 10
    if v < 0:
        v = 0
    
    tmp += (v // 50) * 3
    v %= 50
    if v >= 1:
        tmp += 3
        v = 0

    answer.append([k, tmp])

answer.sort(key= lambda x:x[0])
answer.sort(key= lambda x:x[1], reverse=True)

for i in answer:
    print(*i)