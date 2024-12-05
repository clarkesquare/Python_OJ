n = int(input())

pattern = []
original = []

for _ in range(n):
    original.append(input())

for _ in range(n+2):
    pattern.append([0] * (n + 2))

for i in range(1, n+1):
    for j in range(1, n+1):
        if original[i-1][j-1].isnumeric():
            pattern[i][j] = "*"
            for a in range(i-1, i+2):
                for b in range(j-1, j+2):
                    if str(pattern[a][b]).isnumeric():
                        pattern[a][b] += int(original[i-1][j-1])
                        if pattern[a][b] >= 10:
                            pattern[a][b] = "M"

for i in range(1, n+1):
    print(*pattern[i][1:n+1], sep="")