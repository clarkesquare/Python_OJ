a, b, c = map(int, input().split())
pattern = []
answer = 0

for _ in range(a):
    pattern.append(input())

# 가로 검색
if b >= c:
    for i in range(a):
        for j in range(b-c+1):
            if pattern[i][j] == "." and "#" not in pattern[i][j:j+c]:
                answer += 1

pattern = list(map(list, zip(*pattern)))
# zip으로 일괄 뒤집고 다시 검색
if a >= c:
    for k in range(b):
        for l in range(a-c+1):
            if pattern[k][l] == "." and "#" not in pattern[k][l:l+c]:
                answer += 1

print(answer)