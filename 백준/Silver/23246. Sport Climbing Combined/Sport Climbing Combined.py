score = []

# 처음엔 곱, 다음엔 합
for _ in range(int(input())):
    tmp = list(map(int, input().split()))
    score.append([tmp[0], tmp[1] + tmp[2] + tmp[3], tmp[1] * tmp[2] * tmp[3]])


score.sort(key= lambda x:x[0])
score.sort(key= lambda x:x[1])
score.sort(key= lambda x:x[2])

for i in score[:3]:
    print(i[0], end=" ")