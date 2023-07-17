import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = [1, 1, 2, 4]
    n = int(input())
    if n == 0 or n == 1 or n == 2 or n == 3:
        print(arr[n])
    else:
        for _ in range(n-3):
            arr.append(sum(arr[-1:-5:-1]))
        print(arr[-1])