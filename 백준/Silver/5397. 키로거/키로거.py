from collections import deque

for _ in range(int(input())):
    word = input()
    left = deque()
    right = deque()
    for i in word:
        if i == '<':
            if len(left) >= 1:
                right.appendleft(left.pop())
        
        elif i == '>':
            if len(right) >= 1:
                left.append(right.popleft())
        
        elif i == '-':
            if len(left) >= 1:
                left.pop()
        
        else:
            left.append(i)

    print(''.join(left) + ''.join(right))
