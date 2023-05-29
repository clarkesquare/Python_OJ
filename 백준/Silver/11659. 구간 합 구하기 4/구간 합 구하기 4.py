import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(prefix_sum[b] - prefix_sum[a-1])