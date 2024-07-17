n, m = map(int, input().split())
pattern = []
answer = []

for _ in range(n):
    pattern.append(input())
    answer.append(["."] * m)

for j in range(m):
    for i in range(n):
        if pattern[i][j] == "#":
            answer[i][j], answer[i+1][j], answer[i][j+1], answer[i+1][j+1] = "#", "#", "#", "#"

for k in answer:
    print(*k, sep="")