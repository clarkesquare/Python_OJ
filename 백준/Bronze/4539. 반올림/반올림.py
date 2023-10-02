for _ in range(int(input())):
    number = list(map(int, input()))
    answer = ''
    for i in range(len(number)-1, 0, -1):
        if number[i] >= 5:
            number[i], number[i-1] = 0, number[i-1]+1
        elif number[i] < 5:
            number[i] = 0
    
    for j in number:
        answer += str(j)
    
    print(answer)