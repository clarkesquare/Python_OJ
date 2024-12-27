while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    
    else:
        pattern = []
        answer = {}
        tmp = {}
        cnt = 0
        x = 0
        y = 0
        pattern.append(['#'] * (m+2))
        for i in range(n):
            word = list(input())
            if '@' in word:
                x = i+1
                y = word.index('@') + 1
            pattern.append(['#'] + word + ['#'])
        
        pattern.append(['#'] * (m+2))

        cnt += 1
        pattern[x][y] = '#'
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
                cnt += 1
                pattern[k[0]][k[1]] = '#'
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