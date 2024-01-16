while True:
    numbers = list(input())
    if len(numbers) == 1 and numbers[0] == '0':
        break
        
    while len(numbers) != 1:
        numbers = list(str(sum(map(int, numbers))))
    
    print(numbers[0])