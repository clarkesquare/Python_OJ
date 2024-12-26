while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    else:
        pattern = []
        answer = {}
        tmp = {}
        chk = 0
        total = []

        pattern.append(['*'] * (m+2))
        for _ in range(n):
            pattern.append(['*'] + list(input()) + ['*'])
        
        pattern.append(['*'] * (m+2))
        for i in range(1, n+1):
            for j in range(1, m+1):
                chk = 0
                if pattern[i][j] == '@':
                    chk = 1
                    pattern[i][j] = '*'
                    for r in range(i-1, i+2, 1):
                        for c in range(j-1, j+2, 1):
                            if pattern[r][c] == '@' and (r, c) not in answer:
                                answer[(r, c)] = ''
                    
                    while len(answer) != 0:
                        tmp = {}
                        for a, v in answer.items():
                            pattern[a[0]][a[1]] = '*'
                            for r in range(a[0]-1, a[0]+2, 1):
                                for c in range(a[1]-1, a[1]+2, 1):
                                    if pattern[r][c] == '@' and (r, c) not in tmp:
                                        tmp[(r, c)] = ''
                        
                        answer = tmp

                if chk != 0:
                    total.append(chk)

        print(len(total))
            