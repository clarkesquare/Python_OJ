cnt = 1
n = int(input())

while n != 1:
    cnt += 1
    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n+1

print(cnt)