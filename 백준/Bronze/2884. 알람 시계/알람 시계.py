h, m = map(int, input().split())
remain = 0

if h > 0:
    if m >= 45:
        m -= 45
    else:
        h -= 1
        remain = 45 - m
        m = 60 - remain
else:
    if m >= 45:
        m -=45
    else:
        h = 23
        remain = 45 - m
        m = 60 - remain

print(h, m)