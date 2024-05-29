while True:
    n, m = map(int, input().split())
    if n != 0 and m != 0:
        numbers = list(map(int, input().split()))
        max = 0
        for i in range(n - 1):
            for j in range(i+1, n):
                if numbers[i] + numbers[j] <= m and numbers[i] + numbers[j] > max:
                    max = numbers[i] + numbers[j]
        
        print(max if max != 0 else "NONE")
    
    else:
        break