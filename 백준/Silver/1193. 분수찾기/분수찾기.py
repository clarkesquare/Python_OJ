n = int(input())
cnt = 0
chk = 0

while chk < n:
    cnt += 1
    chk += cnt

if cnt % 2 == 0:
    print(f'{n - (chk - cnt)}/{chk - n + 1}')

else:
    print(f'{chk - n + 1}/{n - (chk - cnt)}')