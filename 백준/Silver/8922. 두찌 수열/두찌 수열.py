for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    pattern = []
    answer = ""

    while True:
        tmp = []
        for i in range(n):
            if i != n - 1:
                tmp.append(abs(numbers[i+1] - numbers[i]))
            
            else:
                tmp.append(abs(numbers[i] - numbers[0]))
        
        if tmp == [0] * n:
            answer = "ZERO"
            break

        if tmp not in pattern:
            pattern.append(tmp)
        
        else:
            answer = "LOOP"
            break

        numbers = tmp
    
    print(answer)