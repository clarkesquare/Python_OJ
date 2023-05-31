def solution(s):
    answer = ''
    n = 0
    
    for i in s:
        if i == ' ':
            n = 0
            answer += i
        else:
            n += 1
            if n % 2 == 1:
                answer += i.upper()
            else:
                answer += i.lower()
            
    return answer