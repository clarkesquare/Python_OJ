while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    else:
        pattern = []
        answer = []
        tmp = []
        island = []
        pattern.append([0] * (w + 2))
        for _ in range(h):
            pattern.append([0] + list(map(int, input().split())) + [0])
        
        pattern.append([0] * (w + 2))

        for i in range(1, h+1):
            for j in range(1, w+1):
                if pattern[i][j] == 1:
                    cnt = 0
                    cnt += 1
                    pattern[i][j] = 0
                    for r in range(-1, 2, 1):
                        for c in range(-1, 2, 1):
                            if pattern[i+r][j+c] == 1 and not (r == 0 and c == 0):
                                answer.append([i+r, j+c])
                    
                    while len(answer) != 0:
                        cnt += 1
                        tmp = []
                        for a in range(len(answer)):
                            pattern[answer[a][0]][answer[a][1]] = 0
                            for r in range(-1, 2, 1):
                                for c in range(-1, 2, 1):
                                    if pattern[answer[a][0] + r][answer[a][1] + c] == 1 and [answer[a][0] + r, answer[a][1] + c] not in tmp:
                                        tmp.append([answer[a][0] + r, answer[a][1] + c])
                        
                        answer = tmp
        
                    island.append(cnt)

        print(len(island))