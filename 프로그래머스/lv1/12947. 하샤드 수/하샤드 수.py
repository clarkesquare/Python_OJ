def solution(x):
    answer = True
    temp = 0
    
    for i in str(x):
        temp += int(i)
    
    answer = True if x%temp==0 else False
    
    return answer