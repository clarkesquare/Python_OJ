def solution(brown, yellow):
    total = brown + yellow
    answer = [0, 0]

    for i in range(2, int(total ** (1/2))+1):
        if total // i == int(total // i):
            if (i - 2) * ((total // i) - 2) == yellow:
                answer = [(total // i), i]
                break
    
    return answer