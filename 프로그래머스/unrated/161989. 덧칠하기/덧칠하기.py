def solution(n, m, section):
    answer = 0
    wall = list('1' * n) + list('1' * (m-1))
    paint = list('1' * m)
    
    for i in section:
        wall[i-1] = '0'
    
    for j in range(n):
        if wall[j] == '0':
            wall[j:j+m] = paint
            answer += 1

    return answer