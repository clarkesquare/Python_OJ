n = int(input())
students = []
answer = []
cnt = 1

for _ in range(n):
    students.append(list(map(int, input().split())))

for i in range(n):
    cnt = 1
    for j in range(n):
        if i != j:
            if students[i][0] < students[j][0] and students[i][1] < students[j][1]:
                cnt += 1
    
    answer.append(cnt)

print(*answer)