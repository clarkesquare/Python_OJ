def solution(t, p):
    answer = 0
    temp = []
    
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(str(p))]) <= int(p):
            answer += 1
            
    return answer