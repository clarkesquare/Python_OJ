pattern = {}
check = []
tmp = []
answer = []
chk = ''

for _ in range(9):
    check.append(input().split())

for i in range(1, 9, 3):
    for j in range(1, 9, 3):
        tmp = []
        for a in range(i-1, i+2):
            for b in range(j-1, j+2):
                if a != i or b != j:
                    tmp.append(check[a][b])

        pattern[check[i][j]] = sorted(tmp)

for i in range(8):
    chk = pattern[check[4][4]][i]
    print(f'#{i + 1}. {chk}')
    for j in range(8):
        print(f'#{i + 1}-{j + 1}. {pattern[chk][j]}')