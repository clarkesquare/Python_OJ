import sys

n = int(input())
numbers = []
rank = {}

input = sys.stdin.readline

for _ in range(n):
    numbers.append(int(input()))

chk = sorted(numbers, reverse=True)

for i in range(1, n + 1):
    if chk[i-1] not in rank:
        rank[chk[i-1]] = i

for i in range(n):
    print(rank[numbers[i]])