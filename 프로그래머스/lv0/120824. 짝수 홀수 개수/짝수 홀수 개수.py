def solution(num_list):
    answer = []
    count_odd = 0
    count_even = 0
    for i in num_list:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    answer = [count_even, count_odd]
    return answer