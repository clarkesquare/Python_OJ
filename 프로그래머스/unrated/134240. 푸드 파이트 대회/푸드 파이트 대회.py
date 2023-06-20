def solution(food):
    answer = ''
    temp = ''
    
    for i in range(len(food)):
        if food[i] // 2 != 0:
            temp += str(i) * (food[i] // 2)
    
    answer = temp + '0' + temp[::-1]
    return answer