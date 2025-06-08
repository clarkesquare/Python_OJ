answer = 1
chk = {}

for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, b):
        if i not in chk:
            chk[i] = 1
        
        else:
            chk[i] += 1

n = int(input())
for j in chk:
    if chk[j] > n:
        answer = 0
        break

print(answer)