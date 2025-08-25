import sys
input = sys.stdin.readline

n = int(input())
h = [0] * 1001
min_x, max_x = 1000, 0

# 각 x의 최대 높이만 기록 (메모리/속도 절약)
for _ in range(n):
    x, y = map(int, input().split())
    if y > h[x]:
        h[x] = y
    if x < min_x: min_x = x
    if x > max_x: max_x = x

Hmax = max(h[min_x:max_x+1])
area = 0

# 높이 j마다, h[x] >= j 인 가장 왼쪽/오른쪽 x를 찾아 폭을 더함
for j in range(1, Hmax + 1):
    # 왼쪽 경계
    l = min_x
    while l <= max_x and h[l] < j:
        l += 1
    if l > max_x:          # 이 높이를 만족하는 기둥이 없음
        continue

    # 오른쪽 경계
    r = max_x
    while r >= min_x and h[r] < j:
        r -= 1

    area += (r - l + 1)    # 이 높이에서 채워지는 가로 폭

print(area)