def solution(price, money, count):
    answer = money
    
    for i in range(1, count+1):
        answer -= price * i
    
    answer = 0 if answer >= 0 else abs(answer)
    
    return answer