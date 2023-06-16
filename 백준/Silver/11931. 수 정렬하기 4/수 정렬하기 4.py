import sys

input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

numbers.sort(reverse=True)

for j in numbers:
    print(j)