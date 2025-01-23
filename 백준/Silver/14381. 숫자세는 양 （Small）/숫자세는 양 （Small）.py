for i in range(int(input())):
    answer = "INSOMNIA"
    numbers = {}
    n = int(input())
    cnt = 0
    while n != 0:
        cnt += 1
        for j in range(len(str(n * cnt))):
            if str(n * cnt)[j] not in numbers:
                numbers[str(n*cnt)[j]] = ''
        
        if len(numbers) == 10:
            answer = n * cnt
            break

    print(f"Case #{i+1}: {answer}")