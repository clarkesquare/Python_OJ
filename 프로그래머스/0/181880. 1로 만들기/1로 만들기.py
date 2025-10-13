def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        tmp = num_list[i]
        while tmp != 1:
            if tmp % 2 == 0:
                tmp //= 2

            else:
                tmp = (tmp - 1) // 2

            answer += 1
    
    return answer