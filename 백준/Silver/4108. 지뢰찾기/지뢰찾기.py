while True:
    r, c = map(int, input().split())
    if r != 0 and c != 0:
        pattern = []
        pattern.append(['.'] * (c + 2))
        for _ in range(r):
            pattern.append(['.'] + list(input()) + ['.'])

        pattern.append(['.'] * (c + 2))
        for i in range(1, r+1):
            for j in range(1, c+1):
                if pattern[i][j] == '*':
                    a = -1
                    for _ in range(3):
                        b = -1
                        for _ in range(3):
                            if pattern[i+a][j+b] != '*':
                                if pattern[i+a][j+b] == '.':
                                    pattern[i+a][j+b] = 1
                                
                                else:
                                    pattern[i+a][j+b] += 1

                            b += 1
                        
                        a += 1
                
                elif pattern[i][j] == '.':
                    pattern[i][j] = 0
        
        for i in range(1, r+1):
            print(*pattern[i][1:-1], sep='')

    else:
        break