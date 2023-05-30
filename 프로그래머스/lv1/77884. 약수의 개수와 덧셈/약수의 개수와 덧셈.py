def solution(left, right):
    answer = 0
    temp = []
    
    for i in range(left, right+1):
        temp = []
        for j in range(1, i+1):
            if i % j == 0:
                temp.append(j)
        if len(temp) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer