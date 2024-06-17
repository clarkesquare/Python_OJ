students = []
score = []
tmp = []

n = int(input())
students = list(input().split())
score = [0] * len(students)

for _ in range(n):
    tmp = list(input().split())
    for i in tmp:
        score[students.index(i)] += 1

for j in range(len(students)):
    students[j] = [students[j]]
    students[j].append(score[j])

students.sort(key=lambda x:x[1], reverse=True)

for k in students:
    print(*k)