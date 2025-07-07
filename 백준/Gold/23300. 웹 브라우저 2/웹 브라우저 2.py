from collections import deque

backward = deque()
forward = deque()
now = []
tmp = deque()

n, q = map(int, input().split())

for _ in range(q):
    check = input().split()
    if check[0] == 'B':
        if len(backward) >= 1:
            forward.appendleft(now.pop())
            now = [backward.pop()]
    
    elif check[0] == 'F':
        if len(forward) >= 1:
            backward.append(now.pop())
            now = [forward.popleft()]
    
    elif check[0] == 'A':
        if len(now) != 0:
            backward.append(now.pop())

        now = [int(check[1])]
        forward = deque()
    
    else:
        tmp = deque()
        for i in range(len(backward)):
            if i == 0:
                tmp.append(backward[i])
            
            else:
                if tmp[-1] != backward[i]:
                    tmp.append(backward[i])
        
        backward = tmp


print(now[0])
if len(backward) >= 1:
    print(*list(backward)[::-1])

else:
    print(-1)

if len(forward) >= 1:
    print(*list(forward))

else:
    print(-1)