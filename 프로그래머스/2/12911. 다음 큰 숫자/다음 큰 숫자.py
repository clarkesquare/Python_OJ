def solution(n):
    num = bin(n)[2:]
    check = num.count('1')
    answer = 0
    for i in range(n+1, 1000001):
        if bin(i)[2:].count('1') == check:
            answer = i
            break
        
    return answer