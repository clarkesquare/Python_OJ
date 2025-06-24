from collections import deque

n, l = map(int, input().split())
numbers = list(map(int, input().split()))
pattern = deque(range(1, n+1))

while len(pattern) != 1:
    for i in range(l):
        for j in range(numbers[i] - 1):
            pattern.append(pattern.popleft())
        
        pattern.popleft()
        if len(pattern) == 1:
            break

print(pattern[0])