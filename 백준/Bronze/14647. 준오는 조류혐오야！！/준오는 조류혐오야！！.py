n, m = map(int, input().split())
pattern = []
tmp = []
answer = [0, 0] # 0번 인덱스는 9의 총 갯수, 1번 인덱스는 행 or 렬 중 가장 많은 9의 갯수
cnt = 0 # 행 or 렬 9의 갯수 검사

# 9의 총 갯수와 각 요소의 9의 갯수로 변환
for _ in range(n):
    tmp = input().split()
    for i in range(m):
        answer[0] += tmp[i].count("9")
        tmp[i] = tmp[i].count("9")
    
    pattern.append(tmp)

# 행 검사
for i in pattern:
    cnt = sum(i)
    if cnt > answer[1]:
        answer[1] = cnt

# 열 검사
for j in range(m):
    cnt = 0
    for k in range(n):
        cnt += pattern[k][j]
    
    if cnt > answer[1]:
        answer[1] = cnt

# 최종 결과 출력
print(answer[0] - answer[1])