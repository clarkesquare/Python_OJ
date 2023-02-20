import sys

count = int(input())

for i in range(count):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)