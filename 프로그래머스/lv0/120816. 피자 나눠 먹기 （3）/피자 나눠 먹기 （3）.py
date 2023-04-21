def solution(slice, n):
    answer = 0
    
    if slice>= n:
        answer = 1
    else:
        while answer * slice < n:
            answer += 1
    return answer