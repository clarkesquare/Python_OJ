def solution(n):
    answer = 0
    fibo1, fibo2 = 0, 1
    for _ in range(n-1):
        fibo1, fibo2 = fibo2 % 1234567, (fibo1+fibo2) % 1234567
    
    answer = fibo2
    return answer