n = int(input())
pattern = []
cnt = n
point = [0, n-1]
position = 1

pattern.append(list(range(1, n+1)))

for i in range(n-1):
    pattern.append([0] * n)

while n > 0:
    n -= 1
    # 세로 이동
    for i in range(n):
        cnt += 1
        point[0] += position
        pattern[point[0]][point[1]] = cnt
    
    # 가로 이동
    position *= -1
    for i in range(n):
        cnt += 1
        point[1] += position
        pattern[point[0]][point[1]] = cnt

for i in pattern:
    print(*i)