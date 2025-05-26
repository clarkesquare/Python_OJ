import sys

n, m = map(int, input().split())
tmp = 0
numbers = {}
input = sys.stdin.readline

for i in range(n, 0, -1):
    numbers[i] = ''

for _ in range(m):
    tmp = int(input())
    del numbers[tmp]
    numbers[tmp] = ''

for k,v in reversed(numbers.items()):
    print(k)