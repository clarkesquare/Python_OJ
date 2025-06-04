for _ in range(int(input())):
    answer = 0
    numbers = list(map(int, input().split()))
    cnt = numbers[0]
    numbers = numbers[1:]
    chk = []
    while True:
        chk = [numbers[0]]
        repeat = 0
        for i in range(1, 20):
            for j in range(len(chk)):
                if chk[j] > numbers[i]:
                    answer += i-j
                    numbers = chk[:j] + [numbers[i]] + chk[j:] + numbers[i+1:]
                    repeat = 1
                    break
            
            else:
                chk.append(numbers[i])
                    
            if repeat == 1:
                break
        
        if len(chk) == 20:
            break

    print(cnt, answer)