while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    else:
        pattern = []
        x = 0
        y = 0
        cnt = 0
        answer = {}
        tmp = {}
        pattern.append(['#'] * (n+2))
        for i in range(m):
            word = list(input())
            if 'A' in word:
                x = i + 1
                y = word.index('A') + 1
            pattern.append(['#'] + word + ['#'])
        
        pattern.append(['#'] * (n+2))
        pattern[x][y] = '?'
        cnt += 1
        if pattern[x-1][y] == '.':
            answer[(x-1, y)] = ''
        
        if pattern[x+1][y] == '.':
            answer[(x+1, y)] = ''
        
        if pattern[x][y-1] == '.':
            answer[(x, y-1)] = ''
        
        if pattern[x][y+1] == '.':
            answer[(x, y+1)] = ''
        
        while len(answer) != 0:
            tmp = {}
            for k in answer:
                pattern[k[0]][k[1]] = '#'
                cnt += 1
                if pattern[k[0]-1][k[1]] == '.' and (k[0]-1, k[1]) not in tmp:
                    tmp[(k[0]-1, k[1])] = ''
                
                if pattern[k[0]+1][k[1]] == '.' and (k[0]+1, k[1]) not in tmp:
                    tmp[(k[0]+1, k[1])] = ''
                
                if pattern[k[0]][k[1]-1] == '.' and (k[0], k[1]-1) not in tmp:
                    tmp[(k[0], k[1]-1)] = ''

                if pattern[k[0]][k[1]+1] == '.' and (k[0], k[1]+1) not in tmp:
                    tmp[(k[0], k[1]+1)] = ''
            
            answer = tmp
        
        print(cnt)