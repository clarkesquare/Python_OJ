for _ in range(3):
    length, maximum = 1, 1
    number = input()
    for i in range(1, len(number)):
        if number[i] == number[i-1]:
            length += 1
        else:
            length = 1
        
        if length > maximum:
            maximum = length
    
    print(maximum)