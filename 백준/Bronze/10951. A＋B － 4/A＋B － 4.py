import sys

while True:
    try:
        n, m = map(int, sys.stdin.readline().split())
        print(n + m)
    except:
        break