from collections import deque

dq = deque()
answer = ""
n, k = map(int, input().split())

for i in range(1, n+1):
    dq.append(i)

if len(dq) >= k:
    while answer == "":

        
        dq.append(dq.popleft())
        for _ in range(k-1):
            dq.popleft()
        
        if len(dq) < k:
            answer = dq[0]
            break

else:
    answer = dq[0]

print(answer)