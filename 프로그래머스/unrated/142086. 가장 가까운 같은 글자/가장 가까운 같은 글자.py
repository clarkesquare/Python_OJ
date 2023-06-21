def solution(s):
    answer = []
    temp = []
    
    for i in range(len(s)):
        if s[i] not in temp:
            answer.append(-1)
        else:
            answer.append(i - int(s[:i].rfind(s[i])))
        temp.append(s[i])
        
    return answer