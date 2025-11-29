for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    answer = 0
    minimum = 100
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            answer += numbers[i]
            if minimum > numbers[i]:
                minimum = numbers[i]
        
    
    print(answer, minimum)