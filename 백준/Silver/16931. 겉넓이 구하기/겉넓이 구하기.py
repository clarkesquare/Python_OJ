a, b = map(int, input().split())

pattern = []
answer = a * b * 2 # 위, 아래 겉넓이 저장

for _ in range(a):
    pattern.append(list(map(int, input().split())))

# 가로 겉널이 저장
for i in range(a):
    answer += pattern[i][0] + pattern[i][b-1]
    for j in range(1, b):
        answer += abs(pattern[i][j-1] - pattern[i][j])

# 세로 겉넓이 저장
for i in range(b):
    answer += pattern[0][i] + pattern[a-1][i]
    for j in range(1, a):
        answer += abs(pattern[j-1][i] - pattern[j][i])

# 정답 출력
print(answer)