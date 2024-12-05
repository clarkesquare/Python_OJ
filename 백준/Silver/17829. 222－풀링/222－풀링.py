n = int(input())

pattern = []
check = []
tmp = []

for _ in range(n):
    pattern.append(list(map(int, input().split())))

while n != 1:
    check = []
    for i in range(0, n, 2):
        tmp = []
        for j in range(0, n, 2):
            tmp.append(sorted([pattern[i][j], pattern[i+1][j], pattern[i][j+1], pattern[i+1][j+1]], reverse=True)[1])

        check.append(tmp)

    pattern = check
    n //= 2

print(pattern[0][0])