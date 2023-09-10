import sys
input = sys.stdin.readline
quadrant = [0, 0, 0, 0, 0]

for _ in range(int(input())):
    n, m = map(int, input().split())
    if n > 0 and m > 0:
        quadrant[0] = quadrant[0] + 1
    elif n < 0 and m > 0:
        quadrant[1] = quadrant[1] + 1
    elif n < 0 and m < 0:
        quadrant[2] = quadrant[2] + 1
    elif n > 0 and m < 0:
        quadrant[3] = quadrant[3] + 1
    else:
        quadrant[4] = quadrant[4] + 1

print('Q1:', quadrant[0])
print('Q2:', quadrant[1])
print('Q3:', quadrant[2])
print('Q4:', quadrant[3])
print('AXIS:', quadrant[4])