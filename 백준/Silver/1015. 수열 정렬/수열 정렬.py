n = int(input())
numbers = list(map(int, input().split()))
chk = {}
cnt = 0
answer = [0] * n

for i in range(n):
    if numbers[i] not in chk:
        chk[numbers[i]] = [i]
    
    else:
        chk[numbers[i]].append(i)

for k, v in sorted(chk.items(), key=lambda x:x[0]):
    for num in v:
        answer[num] = cnt
        cnt += 1

print(*answer)