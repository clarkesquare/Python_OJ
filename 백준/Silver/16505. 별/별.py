n = int(input())
answer = ['*']
lines = ['', '']
tmp = []

for _ in range(n):
    tmp = []
    for i in range(len(answer)):
        lines = ['', '']
        for j in range(len(answer[i])):
            if answer[i][j] == '*':
                lines[0] += '**'
                lines[1] += '* '
            
            else:
                lines[0] += '  '
                lines[1] += '  '
        
        tmp += lines

    answer = tmp

for i in range(len(answer)):
    print(answer[i].rstrip(' '))