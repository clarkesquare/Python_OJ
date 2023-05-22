def solution(board):
    area = []
    temp = []
    answer = 0
    
    for i in range(len(board[0])+2):
        temp = []
        for j in range(len(board[0])+2):
            temp.append(0)
        area.append(temp)
        
    for j in range(len(board)):
        for k in range(len(board[j])):
            if board[j][k] == 1:
                area[j][k:k+3:] = [1, 1, 1]
                area[j+1][k:k+3:] = [1, 1, 1]
                area[j+2][k:k+3:] = [1, 1, 1]
    
    for i in area[1:-1:]:
        answer += i[1:-1].count(0)
    
    return answer