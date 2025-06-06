from collections import deque

deque = deque(range(1, int(input())+1))

while len(deque) != 1:
    deque.popleft()
    if len(deque) == 1:
        break

    deque.append(deque.popleft())

print(*deque)