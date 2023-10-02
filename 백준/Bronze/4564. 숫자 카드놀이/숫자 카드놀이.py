while True:
    n = int(input())
    if n != 0:
        answer = []
        answer.append(n)
        n = str(n)
        while len(n) != 1:
            temp = 1
            for i in n:
                temp *= int(i)

            answer.append(temp)
            n = str(temp)

        print(*answer)
        
    else:
        break