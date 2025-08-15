import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ok = True
for _ in range(m):
    k = int(input())
    arr = list(map(int, input().split()))
    for i in range(k - 1):
        if arr[i] < arr[i + 1]:
            ok = False
            break
    if not ok:
        break

print("Yes" if ok else "No")
