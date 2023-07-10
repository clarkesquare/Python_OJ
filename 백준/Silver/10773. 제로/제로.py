import sys
input = sys.stdin.readline

numbers = []

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        del numbers[-1]
    else:
        numbers.append(n)

print(sum(numbers))