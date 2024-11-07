pattern = {}

for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            if (i, j) not in pattern:
                pattern[(i, j)] = ""

print(len(pattern))