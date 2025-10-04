n = int(input())

pattern = ['  *  ', '  *  ', '*****', ' *** ', ' * * ']
answer = ['*']
total_tmp = []
tmp = ['', '', '', '', '']

for _ in range(n):
    total_tmp = []
    for i in range(len(answer)):
        tmp = ['', '', '', '', '']
        for j in range(len(answer[i])):
            if answer[i][j] == ' ':
                tmp[0] += '     '
                tmp[1] += '     '
                tmp[2] += '     '
                tmp[3] += '     '
                tmp[4] += '     '
            
            else:
                tmp[0] += pattern[0]
                tmp[1] += pattern[1]
                tmp[2] += pattern[2]
                tmp[3] += pattern[3]
                tmp[4] += pattern[4]
        
        total_tmp += tmp
    
    answer = total_tmp

for cnt in answer:
    print(*cnt, sep='')