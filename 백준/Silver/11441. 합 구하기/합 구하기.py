import sys

input = sys.stdin.readline

n = int(input())
prefix_sum = [0]
total = 0
for i in list(map(int, input().split())):
    total += i
    prefix_sum.append(total)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])