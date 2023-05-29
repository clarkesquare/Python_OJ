def solution(s):
    answer = ''
    s = list(s)
    s.sort(reverse = True)
    
    for i in s:
        answer += i
    return answer