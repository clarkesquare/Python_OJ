n, m = map(int, input().split())
answer = [0, 0]
tmp = 0
way = 0

for _ in range(m):
    a, b = input().split()
    b = int(b)
    if a == "MOVE":
        if way == 0:
            answer[0] += b
        
        elif way == 1 or way == -3:
            answer[1] += b

        elif way == 2 or way == -2:
            answer[0] -= b
        
        else:
            answer[1] -= b

    else:
        if b == 0:
            way += 1
        
        else:
            way -= 1
        
        if way == 4 or way == -4:
            way = 0
    
    if answer[0] < 0 or answer[1] < 0 or answer[0] > n or answer[1] > n:
        tmp = -1
    
if tmp != -1:
    print(*answer)

else:
    print(tmp)