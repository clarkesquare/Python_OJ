b, n, m = map(int, input().split())
items = {}
chk = 0

for _ in range(n):
    i, p = input().split()
    items[i] = int(p)

for _ in range(m):
    chk += items[input()]

if chk > b:
    print('unacceptable')

else:
    print('acceptable')