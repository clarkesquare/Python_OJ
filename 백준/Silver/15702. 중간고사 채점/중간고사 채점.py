n, m = map(int, input().split())

score = list(map(int, input().split()))
max = [0, 0]
tmp = [0, 0]
player = []


for _ in range(m):
    player = input().split()
    tmp = [int(player[0]), 0]
    player = player[1:]
    for i in range(n):
        if player[i] == "O":
            tmp[1] += score[i]

    if max == [0, 0]:
        max = tmp
    
    else:
        if tmp[1] >= max[1]:
            if tmp[1] > max[1]:
                max = tmp
            
            elif tmp[1] == max[1] and tmp[0] < max[0]:
                max = tmp

print(*max)