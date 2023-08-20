def solution(s):
    answer = ''
    
    for i in s:
        if len(answer) == 0:
            if i.islower():
                i = i.upper()
        elif answer[-1] == ' ':
            i = i.upper()
        elif i.isupper():
            i = i.lower()
        answer += i
                
    return answer