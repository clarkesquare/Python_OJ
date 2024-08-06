import sys

input = sys.stdin.readline

exts = {}

for _ in range(int(input())):
    a, b = input().split(".")
    b = b.strip()
    if b not in exts:
        exts[b] = 1
    else:
        exts[b] += 1

exts = list(exts.items())
exts.sort(key = lambda x:x[0])

for i in exts:
    print(*i)