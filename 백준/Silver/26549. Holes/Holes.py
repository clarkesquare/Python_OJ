for _ in range(int(input())):
    n, m = map(int, input().split())
    pattern = []
    answer = {}
    tmp = {}
    cnt = 0
    total = [0]

    pattern.append(['#'] * (m+2))
    for _ in range(n):
        pattern.append(['#'] + list(input()) + ['#'])
    
    pattern.append(['#'] * (m+2))
    for i in range(1, n+1):
        for j in range(1, m+1):
            cnt = 0
            if pattern[i][j] == '.':
                cnt += 1
                pattern[i][j] = '#'
                if pattern[i-1][j] == '.':
                    answer[(i-1, j)] = ''
                
                if pattern[i+1][j] == '.':
                    answer[(i+1, j)] = ''
                
                if pattern[i][j-1] == '.':
                    answer[(i, j-1)] = ''
                
                if pattern[i][j+1] == '.':
                    answer[(i, j+1)] = ''

                while len(answer) != 0:
                    tmp = {}
                    for a, v in answer.items():
                        cnt += 1
                        pattern[a[0]][a[1]] = '#'
                        if pattern[a[0] - 1][a[1]] == '.' and (a[0]-1, a[1]) not in tmp:
                            tmp[(a[0]-1, a[1])] = ''
                        
                        if pattern[a[0] + 1][a[1]] == '.' and (a[0]+1, a[1]) not in tmp:
                            tmp[(a[0]+1, a[1])] = ''
                        
                        if pattern[a[0]][a[1] - 1] == '.' and (a[0], a[1]-1) not in tmp:
                            tmp[(a[0], a[1]-1)] = ''
                        
                        if pattern[a[0]][a[1] + 1] == '.' and (a[0], a[1]+1) not in tmp:
                            tmp[(a[0], a[1]+1)] = ''
                    
                    answer = tmp
            
            if cnt != 0:
                if total[0] == 0:
                    total[0] = cnt
            
                else:
                    total.append(cnt + total[-1])

    if len(total) == 1:
        if total[0] == 0:
            print("0 sections, 0 spaces")
        
        else:
            if len(total) == 1:
                if total[0] == 1:
                    print(f"1 section, {total[0]} space")
                
                else:
                    print(f"1 section, {total[0]} spaces")
    
    else:
        print(f"{len(total)} sections, {total[-1]} spaces")