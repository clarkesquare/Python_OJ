def solution(a, b, n):
    answer = 0
    
    while n >= a:
        empty = n % a
        n = (n//a) * b
        answer += n
        n += empty
        
    return answer