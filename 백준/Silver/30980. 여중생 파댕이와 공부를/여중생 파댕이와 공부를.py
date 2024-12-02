n, m = map(int, input().split())
pattern = []
tmp = []
number = ""
answer = 0

# 입력
for _ in range(n * 3):
    pattern.append(list(input()))

# 확인
for i in range(n):
    for j in range(m):
        tmp = pattern[3 * i + 1][j * 8 + 1:(j * 8) + 8]
        while "." in tmp:
            tmp.remove(".")

        number = ""
        for k in range(len(tmp) - 4):
            number += tmp[k + 4]

        answer = int(number)
        if int(tmp[0]) + int(tmp[2]) == answer:
            for a in range(len(tmp)):
                pattern[3 * i][(j * 8) + a + 1] = "*"
                pattern[3 * i + 2][(j * 8) + a + 1] = "*"
                pattern[3 * i + 1][j * 8] = "*"
                pattern[3 * i + 1][j * 8 + len(tmp) + 1] = "*"

        else:
            pattern[3 * i][j * 8 + 3] = "/"
            pattern[3 * i + 1][j * 8 + 2] = "/"
            pattern[3 * i + 2][j * 8 + 1] = "/"

# 결과 출력
for l in pattern:
    print(*l, sep="")