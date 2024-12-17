from collections import deque

n, k, m = map(int, input().split())
cnt = 0
way = 0

dq = deque(list(range(1, n+1)))
answer = []

while len(dq) >= 1:
    for _ in range(k - 1):
        if way == 0:
            dq.append(dq.popleft())
        
        else:
            dq.appendleft(dq.pop())
    
    if way == 0:
        answer.append(dq.popleft())
    
    else:
        answer.append(dq.pop())
        
    cnt += 1
    if cnt == m:
        if way == 0:
            way = 1
        
        else:
            way = 0

        cnt = 0

print(*answer, sep = "\n")