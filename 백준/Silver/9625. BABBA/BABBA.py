import sys

input = sys.stdin.readline
AB = [1, 0]

for _ in range(int(input())):
    AB[0], AB[1] = AB[1], AB[0] + AB[1]

print(*AB)