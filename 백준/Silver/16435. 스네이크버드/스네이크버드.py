n, m = map(int, input().split())
feed = list(map(int, input().split()))

feed.sort()

for i in feed:
    if i <= m:
        m += 1
    else:
        break

print(m)