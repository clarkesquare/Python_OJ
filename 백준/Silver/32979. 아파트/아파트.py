from collections import deque

dq = deque()
answer = []

n = int(input())
m = int(input())
for i in list(map(int, input().split())):
    dq.append(i)

pattern = list(map(int, input().split()))
for i in range(m):
    for _ in range(pattern[i]-1):
        dq.append(dq.popleft())
    
    answer.append(dq[0])

print(*answer)