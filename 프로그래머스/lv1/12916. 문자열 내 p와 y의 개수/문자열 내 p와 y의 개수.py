def solution(s):
    answer = True
    total_p = 0
    total_y = 0
    
    for i in s:
        if i == 'p' or i == 'P':
            total_p += 1
        elif i == 'y' or i == 'Y':
            total_y += 1
    
    answer = True if total_p == total_y else False

    return answer