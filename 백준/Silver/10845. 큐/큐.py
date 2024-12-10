from collections import deque
import sys

input = sys.stdin.readline

dq = deque()

for _ in range(int(input())):
    n = input().strip("\n").split()
    if len(n) >= 2:
        n[1] = int(n[1])
        dq.append(n[1])
    
    else:
        if n[0] == "pop":
            if len(dq) >= 1:
                print(dq.popleft())
            
            else:
                print(-1)
        
        elif n[0] == "size":
            print(len(dq))
        
        elif n[0] == "empty":
            if len(dq) == 0:
                print(1)
            
            else:
                print(0)
        
        elif n[0] == "front":
            if len(dq) >= 1:
                print(dq[0])
            
            else:
                print(-1)
            
        elif n[0] == "back":
            if len(dq) >= 1:
                print(dq[-1])
            
            else:
                print(-1)