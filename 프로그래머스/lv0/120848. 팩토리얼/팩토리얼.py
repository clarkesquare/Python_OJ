def solution(n):
    answer = 0
    i = 1
    temp = n
    while temp / i > 1:
        i += 1
        temp /= i
        
    answer = i
    return answer