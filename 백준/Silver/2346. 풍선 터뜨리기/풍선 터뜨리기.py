from collections import deque

n = int(input())
numbers = deque()
chk = list(map(int, input().split()))
for i in range(n):
    numbers.append([chk[i], i+1])

answer = [numbers.popleft()]
while len(numbers) != 0:
    if answer[-1][0] > 0:
        for _ in range(answer[-1][0] - 1):
            numbers.append(numbers.popleft())
    
    else:
        for _ in range(answer[-1][0] * -1):
            numbers.appendleft(numbers.pop())
    
    answer.append(numbers.popleft())

for i in answer:
    print(i[1], end=' ')