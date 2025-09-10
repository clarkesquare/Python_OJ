import sys

input = sys.stdin.readline

n = int(input())
counts = {}
total = 0
warnings = 0

for _ in range(n):
    name = input().strip()
    cur = counts.get(name, 0)
    if 2 * cur > total:
        warnings += 1
        
    counts[name] = cur + 1
    total += 1

print(warnings)