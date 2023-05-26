def solution(num):
    answer = 0
    cnt = 0
    
    while cnt < 500 and num != 1.0:
        cnt += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    
    answer = -1 if cnt == 500 else cnt
    return answer