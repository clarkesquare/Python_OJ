from collections import deque

n, k = map(int, input().split())
word = deque(input())
tmp = deque()

for _ in range(n):
    if len(word) != 0:
        tmp.append(word.popleft())
    
    else:
        break

    chk = 0
    while len(tmp) >= k:
        for j in range(1, k):
            if tmp[-1 * j] != tmp[-1 * (j + 1)]:
                chk = 1
                break
        
        else:
            for _ in range(k):
                tmp.pop()
        
        if chk == 1:
            break

print(*tmp, sep='')