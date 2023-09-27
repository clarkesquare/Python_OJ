n, m = map(int, input().split())
pattern, answer = [], []

for _ in range(n):
    answer.append(['.']*m)

for _ in range(n):
    pattern.append(input())

for i in range(n):
    for j in range(m):
        if pattern[i][j] != '.':
            temp = pattern[i][j]
            answer[i][j] = temp
            answer[i][j*-1 -1] = temp

for i in range(n):
    temp = ''
    for j in range(m):
        temp += answer[i][j]
    print(temp)