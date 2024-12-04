def check():
    global answer
    if cnt == number:
        answer = [x + 1, y + 1]

n = int(input())
number = int(input())

pattern = []
x = n//2
y = n//2
answer = [x + 1, y + 1]
cnt = 1

for _ in range(n):
    pattern.append([0] * n)

pattern[x][y] = 1

for i in range(1, n):
    if i % 2 != 0:
        for _ in range(i):
            cnt += 1
            x -= 1
            pattern[x][y] = cnt
            check()
        
        for _ in range(i):
            cnt += 1
            y += 1
            pattern[x][y] = cnt
            check()

    else:
        for _ in range(i):
            cnt += 1
            x += 1
            pattern[x][y] = cnt
            check()
        
        for _ in range(i):
            cnt += 1
            y -= 1
            pattern[x][y] = cnt
            check()

for _ in range(i):
    cnt += 1
    x -= 1
    pattern[x][y] = cnt
    check()

for j in pattern:
    print(*j)

print(*answer)