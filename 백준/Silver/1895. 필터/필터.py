pattern_i = []
tmp = []
answer = 0
filtering = 0

n, m = map(int, input().split())
for _ in range(n):
    pattern_i.append(list(map(int, input().split())))

filtering = int(input())

for i in range(n-2):
    for j in range(m-2):
        tmp = []
        for k in range(i, i+3):
            tmp += pattern_i[k][j:j+3]
    
        tmp.sort()
        if tmp[4] >= filtering:
            answer += 1

print(answer)