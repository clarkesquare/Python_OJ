from collections import deque

pattern = deque(['A', 'B', 'C', 'D', 'E'])
while True:
    button = int(input())
    if button == 4:
        input()
        break
    
    n = int(input())

    for _ in range(n):
        if button == 1:
            pattern.append(pattern.popleft())
        
        elif button == 2:
            pattern.appendleft(pattern.pop())
        
        else:
            pattern[0], pattern[1] = pattern[1], pattern[0]

print(*pattern)