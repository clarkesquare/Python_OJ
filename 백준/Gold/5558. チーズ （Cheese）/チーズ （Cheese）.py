n, m, s = map(int, input().split())
cnt = 0
pattern = [['X'] * (m + 2)]
start = [0, 0]
number = 0
chk = 0
total = {}
answer = {}
tmp = {}

for i in range(1, n+1):
    word = list(input())
    if 'S' in word:
        for j in word:
            if 'S' in word:
                answer[(i, word.index('S')+1)] = ''
                break
    
    pattern.append(['X'] + word + ['X'])

pattern.append(['X'] * (m + 2))

while number != s:
    chk = 0
    total = {}
    while chk == 0:
        tmp = {}
        for k in answer:
            total[k[0], k[1]] = ''
            if pattern[k[0]][k[1]] == str(number + 1):
                chk = 1
                break

            if pattern[k[0]-1][k[1]] != 'X' and (k[0]-1, k[1]) not in total and (k[0]-1, k[1]) not in tmp:
                tmp[(k[0]-1, k[1])] = ''
            
            if pattern[k[0]+1][k[1]] != 'X' and (k[0]+1, k[1]) not in total and (k[0]+1, k[1]) not in tmp:
                tmp[(k[0]+1, k[1])] = ''
            
            if pattern[k[0]][k[1]-1] != 'X' and (k[0], k[1]-1) not in total and (k[0], k[1]-1) not in tmp:
                tmp[(k[0], k[1]-1)] = ''
            
            if pattern[k[0]][k[1]+1] != 'X' and (k[0], k[1]+1) not in total and (k[0], k[1]+1) not in tmp:
                tmp[(k[0], k[1]+1)] = ''
        
        if chk == 1:
            break

        answer = tmp
        cnt += 1

    answer = {}
    answer[k[0], k[1]] = ''
    number += 1
    if number == s:
        break

print(cnt)