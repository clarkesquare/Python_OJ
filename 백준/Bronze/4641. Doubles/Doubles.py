while True:
    numbers = list(map(int, input().split()))
    if numbers != [-1]:
        numbers = numbers[:-1:]
        cnt = 0
        for i in numbers:
            if i*2 in numbers:
                cnt += 1
        print(cnt)
    else:
        break