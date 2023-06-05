case = int(input())

for _ in range(case):
    students = int(input())
    temp = {}
    for i in range(students):
        n, m = map(str, input().split())
        temp[n] = int(m)
    print(max(temp, key=temp.get))