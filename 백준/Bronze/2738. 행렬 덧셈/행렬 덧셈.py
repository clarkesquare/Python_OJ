a, b, = map(int, input().split())
tmp = []
answer = []

for _ in range(a):
    tmp = list(map(int, input().split()))
    answer.append(tmp)

for i in range(a):
    tmp = list(map(int, input().split()))
    for j in range(b):
        answer[i][j] += tmp[j]
    
for k in answer:
    print(*k)