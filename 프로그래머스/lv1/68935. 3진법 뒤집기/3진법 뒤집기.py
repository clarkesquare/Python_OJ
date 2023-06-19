def solution(n):
    temp = ''
    answer = 0
    
    while n // 3 != 0:
        temp += str(n % 3)
        n //= 3
    temp += str(n)
    temp = temp[::-1]
    
    for i in range(len(temp)):
        answer += int(temp[i]) * (3 ** i)

    return answer