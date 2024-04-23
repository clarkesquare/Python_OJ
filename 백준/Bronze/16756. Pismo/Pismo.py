import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
interval = 10 ** 9

for i in range(1, n):
    if abs(numbers[i] - numbers[i-1]) < interval:
        interval = abs(numbers[i] - numbers[i-1])

print(interval)