n = int(input())
answer = [0, 0, 0]
chk = [5*60, 1*60, 10]

for i in range(3):
    if n // chk[i] >= 1:
        answer[i] += n // chk[i]
        n %= chk[i]

if n == 0:
    print(*answer)

else:
    print(-1)