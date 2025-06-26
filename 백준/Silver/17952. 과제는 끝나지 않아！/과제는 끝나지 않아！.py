from collections import deque
import sys

input = sys.stdin.readline

answer = 0
homework = deque()
for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    if numbers[0] != 0:
        homework.appendleft([numbers[1], numbers[2]])
    
    if len(homework) >= 1:
        homework[0][1] -= 1
        if homework[0][1] == 0:
            answer += homework[0][0]
            homework.popleft()

print(answer)