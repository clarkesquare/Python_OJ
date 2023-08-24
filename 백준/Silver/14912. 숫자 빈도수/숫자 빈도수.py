n, m = input().split()

s = list(map(str, range(1, int(n)+1)))
cnt = 0

for i in s:
    if m in i:
        cnt += i.count(m)

print(cnt)