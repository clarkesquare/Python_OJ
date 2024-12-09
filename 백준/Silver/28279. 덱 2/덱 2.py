from collections import deque
import sys

dq = deque()
input = sys.stdin.readline

for _ in range(int(input())):
    n = input().strip().split()
    if len(n) >= 2:
        n[1] = int(n[1])
        if n[0] == "1":
            dq.appendleft(int(n[1]))
        
        else:
            dq.append(int(n[1]))
    
    else:
        n[0] = int(n[0])
        if n[0] == 3:
            if len(dq) >= 1:
                print(dq.popleft())
                
            else:
                print(-1)
        
        elif n[0] == 4:
            if len(dq) >= 1:
                print(dq.pop())

            else:
                print(-1)
        
        elif n[0] == 5:
            print(len(dq))
        
        elif n[0] == 6:
            if len(dq) == 0:
                print(1)
            
            else:
                print(0)
        
        elif n[0] == 7:
            if len(dq) != 0:
                print(dq[0])
            
            else:
                print(-1)
        
        elif n[0] == 8:
            if len(dq) != 0:
                print(dq[-1])
            
            else:
                print(-1)