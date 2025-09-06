from collections import deque
import sys

input = sys.stdin.readline

tmp = deque(input().strip())
after = [deque(input().strip())]
for _ in range(len(after[0]) - len(tmp)):
    check = []
    for i in range(len(after)):
        if after[i][-1] == 'A':
            after[i].pop()
            check.append(after[i])
        
        else:
            after[i].pop()
            after[i].reverse()
            check.append(after[i])
    
    after = check

for i in after:
    if i == tmp:
        print(1)
        break

else:
    print(0)