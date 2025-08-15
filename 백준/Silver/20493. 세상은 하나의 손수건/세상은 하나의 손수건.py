def posit(x):
    if position == 0:
        coordinate[0] += x
    
    elif position == 1:
        coordinate[1] -= x
    
    elif position == 2:
        coordinate[0] -= x
    
    else:
        coordinate[1] += x

coordinate = [0, 0]
a, b = map(int, input().split())
position = 0
chk = 0

for _ in range(a):
    t, way = input().split()
    t = int(t)
    posit(t - chk)
    chk = t
    if way == 'right': # 방향 변환
        position += 1
    
    else:
        position -= 1
    
    if position == 4:
        position = 0
    
    if position == -1:
        position = 3

if chk != b:
    posit(b - chk)

print(*coordinate)