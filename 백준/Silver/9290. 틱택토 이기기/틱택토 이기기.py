for i in range(1, int(input()) + 1):
    pattern = []
    for _ in range(3):
        pattern.append(list(input()))

    chk = 0
    win = input()

    # 가로 검사
    if chk == 0:
        for j in range(3):
            if (pattern[j][0], pattern[j][1], pattern[j][2]).count(win) == 2:
                pattern[j][0], pattern[j][1], pattern[j][2] = win, win, win
                chk = 1
                break

    # 세로 검사
    if chk == 0:
        for j in range(3):
            if (pattern[0][j], pattern[1][j], pattern[2][j]).count(win) == 2:
                pattern[0][j], pattern[1][j], pattern[2][j] = win, win, win
                chk = 1
                break

    # 대각 검사
    if chk == 0:
        if (pattern[0][0], pattern[1][1], pattern[2][2]).count(win) == 2:
            pattern[0][0], pattern[1][1], pattern[2][2] = win, win, win
            chk = 1
    
    if chk == 0:
        if (pattern[0][2], pattern[1][1], pattern[2][0]).count(win) == 2:
            pattern[0][2], pattern[1][1], pattern[2][0] = win, win, win
            chk = 1

    # 결과 출력:
    print(f"Case {i}:")
    for k in pattern:
        print(''.join(k))