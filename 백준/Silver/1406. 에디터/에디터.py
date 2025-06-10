from collections import deque

chk = deque(input())
text = deque()

for _ in range(int(input())):
    pattern = input()
    if pattern == 'L':
        if len(chk) != 0:
            text.appendleft(chk.pop())

    elif pattern == 'D':
        if len(text) != 0:
            chk.append(text.popleft())
    
    elif pattern == 'B':
        if len(chk) != 0:
            chk.pop()
    
    else:
        chk.append(pattern[-1])

print(*(chk + text), sep='')