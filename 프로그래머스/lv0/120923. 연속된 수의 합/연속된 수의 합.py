def solution(num, total):
    answer = []
    temp = total//num
    answer.append(temp)
    i = 1
    
    for j in range(num-1):
        if j % 2 == 0:
            answer.append(temp+i)
        else:
            answer.append(temp-i)
        if len(answer) % 2 == 1:
            i += 1
    
    answer = sorted(answer)
    return answer