from collections import deque
import sys

input = sys.stdin.readline
dq = deque()
cnt = 1

for i in range(int(input())):
    words = input().strip("\n").split()
    if words[0] == "A":
        if words[1] == "L":
            dq.appendleft(cnt)
        
        else:
            dq.append(cnt)
        
        cnt += 1

    else:
        if words[1] == "L":
            for _ in range(int(words[2])):
                dq.popleft()
            
        else:
            for _ in range(int(words[2])):
                dq.pop()

print(*dq, sep="\n")
