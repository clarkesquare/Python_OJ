n, m = map(int, input().split())
pattern = []
answer = []

for _ in range(n):
    pattern.append(list(map(int, input().split())))

for i in range(n):
    chk = {}
    axis = [i, 0]
    way = 0
    while True:
        if way == 0:
            axis[1] += pattern[axis[0]][axis[1]]
        
        elif way == 1:
            axis[0] += pattern[axis[0]][axis[1]]
        
        elif way == 2:
            axis[1] -= pattern[axis[0]][axis[1]]
        
        else:
            axis[0] -= pattern[axis[0]][axis[1]]

        way += 1
        way %= 4
        if 0 <= axis[0] <= n-1 and 0 <= axis[1] <= m-1:
            if (axis[0], axis[1], way) not in chk:
                chk[(axis[0], axis[1], way)] = None
            
            else:
                answer.append(i+1)
                break
        
        else:
            break

print(len(answer))
if len(answer) >= 1:
    print(*answer)