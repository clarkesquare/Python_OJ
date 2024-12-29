for _ in range(int(input())):
    n, m = map(int, input().split())
    pattern = []
    answer = {}
    tmp = {}
    cnt = 0
    chk = 0

    pattern.append(['X'] * (m+2))
    for i in range(n):
        word = list(input())
        if 'S' in word:
            x = i+1
            y = word.index('S') + 1

        pattern.append(['X'] + list(word) + ['X'])
    
    pattern.append(['X'] * (m+2))
    answer[(x, y)] = ''
    
    while len(answer) != 0 and chk == 0:
        tmp = {}
        for k in answer:
            if pattern[k[0]][k[1]] == 'G':
                chk = 1
                break

            else:
                pattern[k[0]][k[1]] = 'X'
            
            if pattern[k[0]-1][k[1]] != 'X' and (k[0]-1, k[1]) not in tmp:
                tmp[(k[0]-1, k[1])] = ''
            
            if pattern[k[0]+1][k[1]] != 'X' and (k[0]+1, k[1]) not in tmp:
                tmp[(k[0]+1, k[1])] = ''
            
            if pattern[k[0]][k[1]-1] != 'X' and (k[0], k[1]-1) not in tmp:
                tmp[(k[0], k[1]-1)] = ''
            
            if pattern[k[0]][k[1]+1] != "X" and (k[0], k[1]+1) not in tmp:
                tmp[(k[0], k[1]+1)] = ''
        
        if chk != 0:
            break
        
        answer = tmp
        cnt += 1

    if chk != 0:
        print(f"Shortest Path: {cnt}")
    
    else:
        print("No Exit")