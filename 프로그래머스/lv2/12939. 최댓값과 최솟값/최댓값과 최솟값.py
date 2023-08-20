def solution(s):
    s = s.split()
    answer = ''
    temp = []
    
    for i in s:
        temp.append(int(i))
    
    answer = str(min(temp)) + ' ' + str(max(temp))
    return answer