n = int(input())
number = n * (n ** 2 + 1 ) // 2
answer = "TRUE"
tmp = []
pattern = []
duplications = []

# 가로 검사
for _ in range(n):
    tmp = list(map(int, input().split()))
    duplications += tmp
    if sum(tmp) != number:
        answer = "FALSE"

    pattern.append(tmp)

# 세로 검사
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(pattern[i][j])
    
if sum(tmp) != number:
    answer = "FALSE"

# 대각 검사
tmp = 0
for k in range(n):
    tmp += pattern[k][k]

if tmp != number:
    answer = "FALSE"

tmp = 0
for l in range(n):
    tmp += pattern[(n-1)-l][l]

if tmp != number:
    answer = "FALSE"

for v in duplications:
    if duplications.count(v) >= 2:
        answer = "FALSE"
        break

# 답 출력
print(answer)