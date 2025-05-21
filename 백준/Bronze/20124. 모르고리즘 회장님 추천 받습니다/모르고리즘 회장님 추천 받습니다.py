import sys

n = int(input())
students = {}
input = sys.stdin.readline

for _ in range(n):
    a, b = input().split()
    b = int(b)
    if a not in students:
        students[a] = b
    
    else:
        students[a] += b

students = list(students.items())
students.sort(key = lambda x:x[0])
students.sort(key = lambda x:x[1], reverse=True)

print(students[0][0])