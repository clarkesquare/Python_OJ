import sys

n = str(sys.stdin.readline())
f = int(sys.stdin.readline())

n = int(n[:-3] + '00')
while n % f != 0:
    n += 1

print(str(n)[-2:])