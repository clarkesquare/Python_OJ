n, m = map(int, input().split())
cnt = 0

if n >= m:
    cnt = (n - 1) + ((m -1) * n)
else:
    cnt = (m - 1) + ((n - 1) * m)

print(cnt)