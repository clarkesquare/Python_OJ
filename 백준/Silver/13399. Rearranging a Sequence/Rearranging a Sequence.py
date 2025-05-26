import sys

n, m = map(int, input().split())
tmp = 0
numbers = {}
answer = []
input = sys.stdin.readline

for i in range(n, 0, -1):
    numbers[i] = ''

for _ in range(m):
    tmp = int(input())
    del numbers[tmp]
    numbers[tmp] = ''

answer = list(numbers.items())
for k, v in answer[::-1]:
    print(k)