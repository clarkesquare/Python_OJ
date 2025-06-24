from collections import deque

n = int(input())
tmp = list(map(int, input().split()))
numbers = deque()

for i in range(1, n+1):
    numbers.append([tmp[i-1], i])

while len(numbers) != 1:
    for _ in range(numbers[0][0] % len(numbers)):
        numbers.append(numbers.popleft())
    
    numbers.pop()

print(numbers[0][1])