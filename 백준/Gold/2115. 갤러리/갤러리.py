a, b = map(int, input().split()) # X는 벽, .는 빈 공간
pattern = []
answer = 0
check = 0

for _ in range(a):
    pattern.append(input())

for i in range(a-1):
    for j in range(b-1): # 매번 검사, 2개일 경우 answer 1 증가하고 2개 점프
        if check == 1:
            check = 0
        
        else:
            if pattern[i][j] == pattern[i][j+1] and pattern[i][j] != pattern[i+1][j] and pattern[i+1][j] == pattern[i+1][j+1]:
                check = 1
                answer += 1

check = 0
for j in range(b-1):
    for i in range(a-1):
        if check == 1:
            check = 0
        
        else:
            if pattern[i][j] == pattern[i+1][j] and pattern[i][j] != pattern[i][j+1] and pattern[i][j+1] == pattern[i+1][j+1]:
                check = 1
                answer += 1

print(answer)
