m, n = map(int, input().split())
pattern = []

pattern.append([0] * (m+2))
for _ in range(n):
    pattern.append([0] + list(map(int, input().split())) + [0])

pattern.append([0] * (m+2))

answer = {}
tmp = {}

answer[(1, 1)] = ''
chk = 0

while len(answer) != 0 and chk == 0:
    tmp = {}
    for k in answer:
        if k[0] == n and k[1] == m:
            chk = 1
            break

        if pattern[k[0]+1][k[1]] == 1 and (k[0]+1, k[1]) not in tmp:
            tmp[k[0]+1, k[1]] = ''
        
        if pattern[k[0]][k[1]+1] == 1 and (k[0], k[1]+1) not in tmp:
            tmp[k[0], k[1]+1] = ''
    
    answer = tmp

if chk == 0:
    print("No")

else:
    print("Yes")