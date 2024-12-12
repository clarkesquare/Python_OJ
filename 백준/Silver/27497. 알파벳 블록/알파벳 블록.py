from collections import deque
import sys

input = sys.stdin.readline
dq = deque()
stack = deque()

for _ in range(int(input())):
    word = input().strip("\n").split()
    if len(word) >= 2:
        if word[0] == "1":
            dq.append(word[1])
        
        else:
            dq.appendleft(word[1])
        
        stack.append(word)
    
    else:
        if len(stack) >= 1:
            if stack[-1][0] == "1":
                dq.pop()
            
            else:
                dq.popleft()
            
            stack.pop()

if len(stack) >= 1:
    print(*dq, sep="")

else:
    print(0)