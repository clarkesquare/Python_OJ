n, m = input().split()

n = int(n[::-1])
m = int(m[::-1])

if n > m:
    print(n)
else:
    print(m)