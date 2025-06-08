n, m = map(int, input().split())
A = []
B = []
answer = []
num = 0

for _ in range(n):
    A.append(list(map(int, input().split())))
    answer.append([])

m, k = map(int, input().split())

for _ in range(m):
    B.append(list(map(int, input().split())))

for i in range(n):
    for j in range(k):
        num = 0
        for l in range(m):
            num += A[i][l]* B[l][j]
        
        answer[i].append(num)

for cnt in answer:
    print(*cnt)