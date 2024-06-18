students = []

for _ in range(int(input())):
    students.append(input().split())

students.sort(key=lambda x:x[1], reverse=True)
students.sort(key=lambda x:x[0])

for i in students:
    print(*i)