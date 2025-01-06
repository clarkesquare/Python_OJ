pattern = {}
answer = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            if (i, j) not in pattern:
                pattern[(i, j)] = ''

for i in pattern:
    if (i[0]-1, i[1]) not in pattern:
        answer += 1
    
    if (i[0]+1, i[1]) not in pattern:
        answer += 1
    
    if (i[0], i[1]-1) not in pattern:
        answer += 1
    
    if (i[0], i[1]+1) not in pattern:
        answer += 1

print(answer)