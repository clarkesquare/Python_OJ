for _ in range(int(input())):
    answer = 1
    pattern = []
    tmp = ""

    # 패턴 입력
    tmp += input()
    tmp += input()[::-1]
    tmp = tmp[:-2] + tmp[-1]
    tmp = tmp[:-1:] + input()[::-1] + tmp[-1]

    for i in range(8):
        if tmp[0] == "O" and tmp[-1] == "O":
            tmp = tmp[-1] + tmp[:-1]
        
        else:
            break
    
    n = 0
    for i in range(8):
        if tmp[i] == "O":
            n += 1
            if i == 7:
                pattern.append(n)
        
        else:
            if n != 0:
                pattern.append(n)
            
            n = 0

    # 체크    
    numbers = list(map(int, input().split()))
    if numbers[0] != len(pattern):
        answer = 0
    
    else:
        if pattern != numbers[1:]:
            for i in range(numbers[0]):
                pattern = [pattern[-1]] + pattern[:-1]
                if pattern == numbers[1:]:
                    break
            
            else:
                answer = 0

    print(answer)