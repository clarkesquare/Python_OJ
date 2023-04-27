n = int(input())

tickets = list(map(int, input().split()))
row = []
student = 1

for i in tickets:
    row.insert(i, student)
    student += 1

for i in reversed(row):
    print(i, end=' ')