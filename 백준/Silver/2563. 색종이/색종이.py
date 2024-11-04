pattern = {}

for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            if (i, j) not in pattern:
                pattern[(i, j)] = ""

print(len(pattern))