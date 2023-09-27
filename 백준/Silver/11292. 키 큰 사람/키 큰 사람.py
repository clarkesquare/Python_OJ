while True:
    n = int(input())
    if n != 0:
        max = 0
        answer = []
        for _ in range(n):
            n, m = input().split()
            m = float(m)
            if m >= max:
                if m > max:
                    max = m
                    answer.clear()
                answer.append(n)
        print(*answer)
        
    else:
        break