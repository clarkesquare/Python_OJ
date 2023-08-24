n, m = input().split()
cnt = 0

s = list(map(str, range(1, int(n)+1)))

for i in s:
    if m in i:
        cnt += i.count(m)

print(cnt)