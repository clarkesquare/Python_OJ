while True:
    n = int(input())
    answer = ''
    if n != -1:
        temp = []
        for i in range(1, n):
            if n % i == 0:
                temp.append(i)
        if sum(temp) == n:
            for j in temp:
                answer += str(j)
                answer += ' + '
            answer = answer[:-3:]
            print(n, '=', answer)
        else:
            print(n, 'is NOT perfect.')

    else:
        break