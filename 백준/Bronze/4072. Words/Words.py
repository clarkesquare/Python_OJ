while True:
    answer = []
    word = list(input().split())
    if word != ['#']:
        for i in word:
            answer.append(i[::-1])
        
        print(*answer, sep=' ')

    else:
        break