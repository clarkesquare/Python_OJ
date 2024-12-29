for _ in range(int(input())):
    n = int(input())
    pattern = []
    x = 0
    y = 0
    answer = {}
    tmp = {}

    pattern.append(['*'] * (n+2))
    for i in range(n):
        word = list(input())
        if 's' in word:
            x = i + 1
            for j in range(n):
                if word[j] == 's':
                    y = j + 1
                    break
        
        pattern.append(['*'] + word + ['*'])

    pattern.append(['*'] * (n+2))
    pattern[x][y] = '-'
    answer[(x, y)] = ''
    chk = 0
    cnt = 0
    while len(answer) != 0 and chk == 0:
        tmp = {}
        for k in answer:
            if pattern[k[0]][k[1]] == '-':
                pattern[k[0]][k[1]] = '*'
            
            else:
                chk = 1
                break

            if pattern[k[0]-1][k[1]] != '*' and (k[0]-1, k[1]) not in tmp:
                tmp[(k[0]-1, k[1])] = ''
            
            if pattern[k[0]+1][k[1]] != '*' and (k[0]+1, k[1]) not in tmp:
                tmp[(k[0]+1, k[1])] = ''
            
            if pattern[k[0]][k[1]-1] != '*' and (k[0], k[1]-1) not in tmp:
                tmp[(k[0], k[1]-1)] = ''
            
            if pattern[k[0]][k[1]+1] != '*' and (k[0], k[1]+1) not in tmp:
                tmp[(k[0], k[1]+1)] = ''
        
        if chk == 1:
            break

        cnt += 1
        answer = tmp
    
    if chk != 0:
        print(cnt)
    
    else:
        print(-1)
