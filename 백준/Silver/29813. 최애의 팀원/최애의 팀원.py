from collections import deque

n = int(input())
students = deque()
chk = []

for _ in range(n):
    a, b = input().split()
    students.append([a, int(b)])

while len(students) != 1:
    chk = students.popleft()
    for i in range((chk[1] - 1) % len(students)):
        students.append(students.popleft())
    
    students.popleft()

print(students[0][0])