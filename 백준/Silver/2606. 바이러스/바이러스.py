n = int(input())
m = int(input())

computer = {}
for i in range(1, n+1):
    computer[i] = 0

computer[1] = 1
answer = {(1): ''}
lines = {}
virus = {}

for _ in range(m):
    a, b = map(int, input().split())
    if a not in lines:
        lines[a] = [b]
    
    else:
        lines[a].append(b)
    
    if b not in lines:
        lines[b] = [a]
    
    else:
        lines[b].append(a)

if 1 not in lines:
    print(0)

else:
    while len(answer) != 0:
        tmp = {}
        for i in answer:
            virus[i] = ''
            if len(lines[i]) == 1:
                for j in lines[i]:
                    if j not in tmp and j not in virus:
                        tmp[j] = ''
                
            else:
                for j in lines[i]:
                    if j not in tmp and j not in virus:
                        tmp[j] = ''

        answer = tmp
    
    print(len(virus) - 1)