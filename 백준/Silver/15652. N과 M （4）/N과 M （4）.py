def nnm():
    tmp = []
    global numbers
    for j in numbers:
        for k in range(1, n+1):
            if j[-1] <= k:
                tmp.append(j + [k])

    numbers = tmp
    return 0

n, m = map(int, input().split())
numbers = [[i] for i in range(1, n+1)]

for _ in range(m - 1):
    nnm()

for l in numbers:
    print(*l)