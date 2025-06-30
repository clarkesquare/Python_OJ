from collections import deque

n, k, a, b = map(int, input().split())
plants = deque([k] * n)
chk = 0
answer = 0

while True:
    if answer in plants:
        break

    for _ in range(a):
        plants.append(plants.popleft() + b)
    
    answer += 1

print(answer)