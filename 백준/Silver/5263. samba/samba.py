import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pattern = {}

for _ in range(n):
    dancer = input().strip()
    if dancer not in pattern:
        pattern[dancer] = 1
    else:
        pattern[dancer] += 1

for i in pattern:
    if pattern[i] % m != 0:
        print(i)
        break