from collections import deque

unwashed = deque()
notdried = deque()
dried = deque()

a = int(input())
for i in range(a, 0, -1):
    unwashed.append(i)

while True:
    n, m = map(int, input().split())
    if n == 1:
        for _ in range(m):
            notdried.append(unwashed.pop())

    else:
        for _ in range(m):
            dried.append(notdried.pop())
    
    if len(dried) == a:
        break

dried.reverse()
print(*dried, sep="\n")