n, m = map(int, input().split())
u, l, r, d = map(int, input().split())
answer = []
tmp = ''
check = ['#', '.']
cnt = 0

# 위
for i in range(n + u + d):
    tmp = []
    cnt = i
    for j in range(m + l + r):
        tmp.append(check[cnt % 2])
        cnt += 1
    
    answer.append(tmp)

for i in range(u, u+n):
    word = input()
    for j in range(l-1, l-1+m):
        answer[i][j+1] = word[j-(l-1)]

for cnt in answer:
    print(*cnt, sep='')