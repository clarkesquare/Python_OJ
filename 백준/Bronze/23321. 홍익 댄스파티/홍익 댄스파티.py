dance = []

for _ in range(5):
    dance.append(list(input()))

for i in range(len(dance[0])):
    if dance[0][i] == '.' and dance[1][i] == 'o' and dance[2][i] == 'm' and dance[3][i] == 'l' and dance[4][i] == 'n':
        dance[0][i], dance[1][i], dance[2][i], dance[3][i], dance[4][i] = 'o', 'w', 'l', 'n', '.'
    elif dance[0][i] == 'o' and dance[1][i] == 'w' and dance[2][i] == 'l' and dance[3][i] == 'n' and dance[4][i] == '.':
        dance[0][i], dance[1][i], dance[2][i], dance[3][i], dance[4][i] = '.', 'o', 'm', 'l', 'n'

for k in dance:
    print(*k, sep='')