def solution(s):
    answer = ''
    lower, upper = [], []
    
    for i in s:
        lower.append(i) if i.islower() else upper.append(i)
    
    lower.sort(reverse=True)
    upper.sort(reverse=True)
    
    for i in lower:
        answer += i
    
    for i in upper:
        answer += i
    return answer