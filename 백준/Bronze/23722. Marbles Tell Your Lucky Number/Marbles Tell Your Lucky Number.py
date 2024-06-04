while True:
    numbers = list(map(int, input().split()))
    if numbers[0] != 0 or numbers[1] != 0 or numbers[2] != 0 or numbers[3] != 0:
        tmp = 100
        for i in numbers:
            if i != 0 and i < tmp:
                tmp = i

        answer = 1
        for j in range(2, tmp+1):
            if numbers[0] % j == 0 and numbers[1] % j == 0 and numbers[2] % j == 0 and numbers[3] % j == 0:
                answer = j
        
        print(answer)
    
    else:
        break