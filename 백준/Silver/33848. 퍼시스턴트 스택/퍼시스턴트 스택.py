from collections import deque
import sys

stack = deque()
tmp = deque()
input = sys.stdin.readline

for _ in range(int(input())):
    pattern = list(map(int, input().split()))
    if pattern[0] == 1:
        stack.appendleft(pattern[1])
        tmp.appendleft([2])
    
    elif pattern[0] == 2:
        tmp.appendleft([1, stack.popleft()])
    
    elif pattern[0] == 3:
        for _ in range(pattern[1]):
            if tmp[0][0] == 1:
                stack.appendleft(tmp[0][1])
                tmp.popleft()
            
            else:
                stack.popleft()
                tmp.popleft()
    
    elif pattern[0] == 4:
        print(len(stack))
    
    else:
        if len(stack) != 0:
            print(stack[0])
        
        else:
            print(-1)