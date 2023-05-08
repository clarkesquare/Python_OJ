n, m = map(int, input().split())
baskets = list(range(1, n+1))
temp = []

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    temp = baskets[a:b]
    temp.reverse()
    baskets[a:b] = temp

for i in baskets:
    print(i, end=' ')