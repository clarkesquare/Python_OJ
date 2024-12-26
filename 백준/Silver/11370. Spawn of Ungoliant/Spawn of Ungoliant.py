while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    else:
        pattern = []
        pattern.append(['.'] * (n+2))
        answer = {}
        tmp = {}
        for i in range(m):
            word = list(input())
            if 'S' in word:
                x, y = i+1, word.index('S')+1
            pattern.append(['.'] + word + ['.'])
        
        pattern.append(['.'] * (n+2))

        if pattern[x-1][y] == 'T':
            answer[(x-1, y)] = ''
        
        if pattern[x+1][y] == 'T':
            answer[(x+1, y)] = ''
        
        if pattern[x][y-1] == 'T':
            answer[(x, y-1)] = ''
        
        if pattern[x][y+1] == 'T':
            answer[(x, y+1)] = ''
        
        while len(answer) != 0:
            tmp = {}
            for k, v in answer.items():
                pattern[k[0]][k[1]] = 'S'
                if pattern[k[0]-1][k[1]] == 'T' and (k[0]-1, k[1]) not in tmp:
                    tmp[(k[0]-1, k[1])] = ''
                
                if pattern[k[0]+1][k[1]] == 'T' and (k[0]+1, k[1]) not in tmp:
                    tmp[(k[0]+1, k[1])] = ''
                
                if pattern[k[0]][k[1]-1] == 'T' and (k[0], k[1]-1) not in tmp:
                    tmp[(k[0], k[1]-1)] = ''
                
                if pattern[k[0]][k[1]+1] == 'T' and (k[0], k[1]+1) not in tmp:
                    tmp[(k[0], k[1]+1)] = ''
            
            answer = tmp

        for i in pattern[1:-1]:
            print(*i[1:-1], sep='')