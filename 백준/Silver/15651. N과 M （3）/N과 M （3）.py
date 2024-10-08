def nnm():
    tmp = []
    global numbers
    for j in numbers:
        for k in range(1, n+1):
            tmp.append(str(j) + " " + str(k))

    numbers = tmp
    return 0

n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]
for _ in range(m - 1):
    nnm()

print(*numbers, sep = "\n")