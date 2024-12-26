r, c = map(int, input().split())
pattern = []
answer = {}
tmp = {}
wns_total = {"o": 0, "v": 0}
wns_tmp = {"o": 0, "v": 0}

pattern.append(['#'] * (c+2))
for _ in range(r):
    pattern.append(['#'] + list(input()) + ['#'])

pattern.append(['#'] * (c+2))

for i in range(1, r+1):
    for j in range(1, c+1):
        if pattern[i][j] != '#':
            wns_tmp = {"v": 0, "o": 0}
            if pattern[i][j] != '.':
                wns_tmp[pattern[i][j]] += 1
            
            pattern[i][j] = '#'

            if pattern[i-1][j] != '#':
                answer[(i-1, j)] = ''
            
            if pattern[i+1][j] != '#':
                answer[(i+1, j)] = ''
            
            if pattern[i][j-1] != '#':
                answer[(i, j-1)] = ''
            
            if pattern[i][j+1] != '#':
                answer[(i, j+1)] = ''
            
            while len(answer) != 0:
                tmp = {}
                for k, v in answer.items():
                    if pattern[k[0]][k[1]] == 'v':
                        wns_tmp["v"] += 1
                    
                    elif pattern[k[0]][k[1]] == 'o':
                        wns_tmp["o"] += 1

                    pattern[k[0]][k[1]] = '#'
                    if pattern[k[0]-1][k[1]] != '#' and (k[0]-1, k[1]) not in tmp:
                        tmp[(k[0]-1, k[1])] = ''
                    
                    if pattern[k[0]+1][k[1]] != '#' and (k[0]+1, k[1]) not in tmp:
                        tmp[(k[0]+1, k[1])] = ''
                    
                    if pattern[k[0]][k[1]-1] != '#' and (k[0], k[1] -1) not in tmp:
                        tmp[(k[0], k[1]-1)] = ''
                    
                    if pattern[k[0]][k[1]+1] != '#' and (k[0], k[1] +1) not in tmp:
                        tmp[(k[0], k[1]+1)] = ''

                answer = tmp

            if wns_tmp["v"] < wns_tmp["o"]:
                wns_total["o"] += wns_tmp["o"]
            
            else:
                wns_total["v"] += wns_tmp["v"]

for i in wns_total:
    print(wns_total[i], end=' ')