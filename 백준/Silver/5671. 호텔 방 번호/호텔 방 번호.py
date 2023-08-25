while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    rooms = list(map(str, range(n, m+1)))
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = 0

    for i in rooms:
        for j in numbers:
            if i.count(j) >= 2:
                break
        else:
            answer += 1

    print(answer)