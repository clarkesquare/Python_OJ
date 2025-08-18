a, b = input().split()
answer = [['.' for _ in range(len(a))] for _ in range(len(b))]
chk = 0

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            chk = 1
            break
    
    if chk == 1:
        break

for x in range(len(b)):
    answer[x][i] = b[x]

answer[j] = list(a)
for tmp in answer:
    print(''.join(tmp))