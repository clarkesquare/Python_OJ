n, m = map(int, input().split())
x1, y1, x2, y2 = 0, 0, 0, 0
image = [[0]*100 for _ in range(100)]
cnt = 0

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            image[i][j] += 1

for k in range(100):
    for l in range(100):
        if image[k][l] > m:
            cnt += 1

print(cnt)