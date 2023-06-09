import sys

n, m = map(int, sys.stdin.readline().split())
i = min(n, m)

while True:
    if n % i == 0 and m % i == 0:
        print(i)
        break
    i -= 1

print((n*m)//i)