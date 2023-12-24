n, m = map(int, input().split())
balloons = ['.'] * n

for _ in range(m):
    a, b = map(int, input().split())
    for i in range(a-1, n, b):
        if balloons[i] == '.':
            balloons[i] = 'Y'

print(balloons.count('.'))