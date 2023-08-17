board = [['?', '?', '?'], ['?', '?', '?'], ['?', '?', '?']]
mark = ''
winner = 0

def game():
    # 가로 검사
    global winner
    winner = 0
    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2]) and board[i][0] != '?':
            winner = 1 if mark == 'O' else 2
    # 세로 검사
    for i in range(3):
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i]) and board[0][i] != '?':
            winner = 1 if mark == 'O' else 2
    # 대각 검사
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != '?':
        winner = 1 if mark == 'O' else 2
    elif (board[2][0] == board[1][1] and board[1][1] == board[0][2]) and board[2][0] != '?':
        winner = 1 if mark == 'O' else 2

n = int(input())
for _ in range(9):
    mark = 'X' if n % 2 == 0 else 'O'
    a, b = map(int, input().split())
    board[a-1][b-1] = mark
    game()
    if winner != 0:
        break
    n += 1

print(winner)