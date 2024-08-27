n = int(input())

pattern = []
answer = "YES"

for _ in range(n):
    pattern.append(input())

for i in range(n):
    for j in range(n):
        if pattern[i][j] != pattern[j][i]:
            answer = "NO"
            break

print(answer)