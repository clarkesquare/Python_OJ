import sys

input = sys.stdin.readline

n = int(input())
numbers = {}

for _ in range(n):
    a = int(input())
    if a not in numbers:
        numbers[a] = 1
    else:
        numbers[a] += 1

numbers = list(numbers.items())
numbers.sort(key= lambda x:x[0])

for i in numbers:
    for _ in range(i[1]):
        print(i[0])